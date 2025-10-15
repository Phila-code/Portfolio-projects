from book import Book 
from member import Member
from library import Library

def menu():
    library = Library()

    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Search Book")
        print("4. Checkout Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                isbn= input("Enter ISBN: ")
                library.add_book(Book(title, author, isbn))
                print("Book added.")

            elif choice == "2":
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                library.add_member(Member(name, email))
                print("Member registered.")

            elif choice == "3":
                query = input("Enter search query: ")
                results = library.search_books(query)
                if results:
                    for b in results:
                        status = "Available" if b.IsAvailable else "Checked out"
                        print(f"{b.title} by {b.author} | {status}")
                else:
                    print("No books found.")
            
            elif choice == "5":
                email = input("Enter Member Email: ")
                isbn = input("Enter Book ISBN: ")
                library.return_book(isbn, email)
                print("Book returned successfully.")
            
            elif choice == "6":
                print("Goodbye!!")
                break
            else:
                print("Invalid option.")

        except Exception as e:
          print(f"Error: {e}")   
if __name__ == "__main__" :
    menu()    