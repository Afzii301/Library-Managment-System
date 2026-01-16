import json
import os

BOOK_FILE = "library_books.json"
MEMBER_FILE = "library_members.json"

# Agar files nahi hai to empty list ke sath create karo
for file in [BOOK_FILE, MEMBER_FILE]:
    if not os.path.exists(file): 
        with open(file, "w") as f:
            json.dump([], f)

# Library class
class Library:
    # 1 Add Book
    def add_book(self, name, author):
        with open(BOOK_FILE, "r") as file:
            books = json.load(file)
        books.append({"Book Name": name, "Author": author, "Issued To": None})
        with open(BOOK_FILE, "w") as file:
            json.dump(books, file, indent=4)
        print("Book added successfully!")

    # 2 Show All Books
    def show_books(self):
        with open(BOOK_FILE, "r") as file:
            books = json.load(file)
        if not books:
            print("No books available")
        else:
            print("\nAll Books:")
            for i, book in enumerate(books, start=1):
                status = f"Issued to {book['Issued To']}" if book["Issued To"] else "Available"
                print(i, book["Book Name"], "-", book["Author"], "-", status)

    # 3 Update Book
    def update_book(self, old_name, new_name, new_author):
        with open(BOOK_FILE, "r") as file:
            books = json.load(file)
        found = False
        for book in books:
            if book["Book Name"].lower() == old_name.lower():
                book["Book Name"] = new_name
                book["Author"] = new_author
                found = True
                break
        if found:
            with open(BOOK_FILE, "w") as file:
                json.dump(books, file, indent=4)
            print(f"Book '{old_name}' updated successfully!")
        else:
            print(f"Book '{old_name}' not found!")

    # 4 Delete Book
    def delete_book(self, name):
        with open(BOOK_FILE, "r") as file:
            books = json.load(file)
        new_books = [book for book in books if book["Book Name"].lower() != name.lower()]
        if len(new_books) == len(books):
            print(f"Book '{name}' not found!")
        else:
            with open(BOOK_FILE, "w") as file:
                json.dump(new_books, file, indent=4)
            print(f"Book '{name}' deleted successfully!")

    
        # 5 Register Member with duplicate check
    def register_member(self, name, member_id):
        with open(MEMBER_FILE, "r") as file:
            members = json.load(file)

        # Check duplicate member ID
        if any(m["Member ID"] == member_id for m in members):
            print(f"Error: Member ID '{member_id}' already exists! Cannot register duplicate.")
            return

        # Add new member
        members.append({"Name": name, "Member ID": member_id})

        with open(MEMBER_FILE, "w") as file:
            json.dump(members, file, indent=4)

        print(f"Member '{name}' registered successfully!")


    # 6 Show Members
    def show_members(self):
        with open(MEMBER_FILE, "r") as file:
            members = json.load(file)
        if not members:
            print("No members registered")
        else:
            print("\nRegistered Members:")
            for i, member in enumerate(members, start=1):
                print(i, member["Name"], "-", member["Member ID"])

    # 7 Issue Book
    def issue_book(self, book_name, member_id):
        with open(BOOK_FILE, "r") as file:
            books = json.load(file)
        with open(MEMBER_FILE, "r") as file:
            members = json.load(file)

        member_exists = any(m["Member ID"] == member_id for m in members)
        if not member_exists:
            print(f"No member with ID {member_id} found!")
            return

        for book in books:
            if book["Book Name"].lower() == book_name.lower():
                if book["Issued To"]:
                    print(f"Book '{book_name}' is already issued to {book['Issued To']}")
                else:
                    book["Issued To"] = member_id
                    with open(BOOK_FILE, "w") as file:
                        json.dump(books, file, indent=4)
                    print(f"Book '{book_name}' issued to member ID {member_id}")
                return
        print(f"Book '{book_name}' not found!")

    # 8 Return Book
    def return_book(self, book_name):
        with open(BOOK_FILE, "r") as file:
            books = json.load(file)

        for book in books:
            if book["Book Name"].lower() == book_name.lower():
                if book["Issued To"]:
                    print(f"Book '{book_name}' returned from member ID {book['Issued To']}")
                    book["Issued To"] = None
                    with open(BOOK_FILE, "w") as file:
                        json.dump(books, file, indent=4)
                else:
                    print(f"Book '{book_name}' was not issued")
                return
        print(f"Book '{book_name}' not found!")

    # 9 Show Available Books
    def show_available_books(self):
        with open(BOOK_FILE, "r") as file:
            books = json.load(file)
        available = [b for b in books if b["Issued To"] is None]
        if not available:
            print("No books available")
        else:
            print("\nAvailable Books:")
            for i, book in enumerate(available, start=1):
                print(i, book["Book Name"], "-", book["Author"])

    #  Show Issued Books
    def show_issued_books(self):
        with open(BOOK_FILE, "r") as file:
            books = json.load(file)
        issued = [b for b in books if b["Issued To"]]
        if not issued:
            print("No books are currently issued")
        else:
            print("\nIssued Books:")
            for i, book in enumerate(issued, start=1):
                print(i, book["Book Name"], "-", book["Author"], "- Issued to", book["Issued To"])


# Object create
lib = Library()

# Menu loop
while True:
    print("\n........ Library Management System ........")
    print("1. Add Book")
    print("2. Show All Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Register Member")
    print("6. Show Members")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Show Available Books")
    print("10. Show Issued Books")
    print("11. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        author = input("Enter author name: ")
        lib.add_book(name, author)

    elif choice == "2":
        lib.show_books()

    elif choice == "3":
        old_name = input("Enter book name to update: ")
        new_name = input("Enter new book name: ")
        new_author = input("Enter new author name: ")
        lib.update_book(old_name, new_name, new_author)

    elif choice == "4":
        name = input("Enter book name to delete: ")
        lib.delete_book(name)

    elif choice == "5":
        name = input("Enter member name: ")
        member_id = input("Enter member ID: ")
        lib.register_member(name, member_id)

    elif choice == "6":
        lib.show_members()

    elif choice == "7":
        book_name = input("Enter book name to issue: ")
        member_id = input("Enter member ID: ")
        lib.issue_book(book_name, member_id)

    elif choice == "8":
        book_name = input("Enter book name to return: ")
        lib.return_book(book_name)

    elif choice == "9":
        lib.show_available_books()

    elif choice == "10":
        lib.show_issued_books()

    elif choice == "11":
        print("Program exited")
        break

    else:
        print("Invalid choice")


