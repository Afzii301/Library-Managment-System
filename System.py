import os
import json

class Library:
    def __init__(self, new_books="", update_books=""):
        self.new_books = new_books
        self.update_books = update_books
        
    def save_data(self):
        # Use "a" mode to append to file
        with open("Library.txt", "a") as file:
            file.write(f"{self.new_books}\n")  #  f-string

while True:
    print("...........Library Management System............")
    print("1. Add new book")
    print("2. Update book")
    
    choose = input("Choose option: ")
    
    if choose == "1":
        while True:
            name = input("Adding new book: ")
            
            
            if name and name.replace(" ","").isalpha():
                library_instance = Library(new_books=name)
                library_instance.save_data()  #  call method
                print(f"Book '{name}' saved successfully!")
                break
            else:
                print("Invalid book name. Please try again")
