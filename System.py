from db import conn, cursor

class Library:

    # 1 Add Book
    def add_book(self, name, author):
        cursor.execute(
            "INSERT INTO books (name, author) VALUES (%s, %s)",
            (name, author)
        )
        conn.commit()
        print("Book added successfully!")

    # 2 Show All Books
    def show_books(self):
        cursor.execute("SELECT name, author, issued_to FROM books")
        books = cursor.fetchall()

        if not books:
            print("No books available")
            return

        for i, book in enumerate(books, 1):
            status = f"Issued to {book[2]}" if book[2] else "Available"
            print(i, book[0], "-", book[1], "-", status)

    # 3 Update Book
    def update_book(self, old_name, new_name, new_author):
        cursor.execute(
            "UPDATE books SET name=%s, author=%s WHERE LOWER(name)=LOWER(%s)",
            (new_name, new_author, old_name)
        )
        conn.commit()

        if cursor.rowcount:
            print("Book updated successfully!")
        else:
            print("Book not found!")

    # 4 Delete Book
    def delete_book(self, name):
        cursor.execute(
            "DELETE FROM books WHERE LOWER(name)=LOWER(%s)",
            (name,)
        )
        conn.commit()

        if cursor.rowcount:
            print("Book deleted successfully!")
        else:
            print("Book not found!")

    # 5 Register Member
    def register_member(self, name, member_id):
        try:
            cursor.execute(
                "INSERT INTO members (name, member_id) VALUES (%s, %s)",
                (name, member_id)
            )
            conn.commit()
            print("Member registered successfully!")
        except:
            conn.rollback()
            print("Member ID already exists!")

    # 6 Show Members
    def show_members(self):
        cursor.execute("SELECT name, member_id FROM members")
        members = cursor.fetchall()

        if not members:
            print("No members registered")
            return

        for i, m in enumerate(members, 1):
            print(i, m[0], "-", m[1])

    # 7 Issue Book
    def issue_book(self, book_name, member_id):
        cursor.execute(
            "SELECT member_id FROM members WHERE member_id=%s",
            (member_id,)
        )
        if not cursor.fetchone():
            print("Member not found!")
            return

        cursor.execute(
            """
            UPDATE books
            SET issued_to=%s
            WHERE LOWER(name)=LOWER(%s) AND issued_to IS NULL
            """,
            (member_id, book_name)
        )
        conn.commit()

        if cursor.rowcount:
            print("Book issued successfully!")
        else:
            print("Book not available or not found!")

    # 8 Return Book
    def return_book(self, book_name):
        cursor.execute(
            """
            UPDATE books
            SET issued_to=NULL
            WHERE LOWER(name)=LOWER(%s)
            """,
            (book_name,)
        )
        conn.commit()

        if cursor.rowcount:
            print("Book returned successfully!")
        else:
            print("Book not found!")

    # 9 Available Books
    def show_available_books(self):
        cursor.execute(
            "SELECT name, author FROM books WHERE issued_to IS NULL"
        )
        books = cursor.fetchall()

        if not books:
            print("No books available")
            return

        for i, b in enumerate(books, 1):
            print(i, b[0], "-", b[1])

    # 10 Issued Books
    def show_issued_books(self):
        cursor.execute(
            "SELECT name, author, issued_to FROM books WHERE issued_to IS NOT NULL"
        )
        books = cursor.fetchall()

        if not books:
            print("No issued books")
            return

        for i, b in enumerate(books, 1):
            print(i, b[0], "-", b[1], "- Issued to", b[2])
