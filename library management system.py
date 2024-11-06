class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def display_details(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nStatus: {status}\n")

    # Method to update book details
    def update_details(self, title=None, author=None, isbn=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn
        print("Book details updated successfully.\n")

    # Method to borrow a book
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} has been borrowed.\n")
        else:
            print(f"{self.title} is already borrowed and cannot be borrowed again.\n")

    # Method to return a book
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} has been returned.\n")
        else:
            print(f"{self.title} is already available.\n")

    # Class method to search books by title or author
    @staticmethod
    def search_books(books, search_term):
        results = [book for book in books if
                   search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]
        if results:
            print(f"Books found matching '{search_term}':")
            for book in results:
                book.display_details()
        else:
            print(f"No books found for the search term: {search_term}\n")


# Demonstrating the functionality of the Book class

# Creating instances of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee", "1234567890")
book2 = Book("1984", "George Orwell", "2345678901")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "3456789012")

# Displaying book details
print("Displaying book details:")
book1.display_details()
book2.display_details()

# Updating book details
print("Updating book details:")
book1.update_details(title="To Kill a Mockingbird (Updated Edition)")

# Borrowing and returning books
print("Borrowing and returning books:")
book1.borrow()  # Successful borrow
book1.borrow()  # Should show that the book is already borrowed
book1.return_book()  # Returning the book
book1.borrow()  # Borrowing again after returning

# Searching for books by title or author
print("Searching for books:")
books = [book1, book2, book3]
Book.search_books(books, "george")  # Searching by author
Book.search_books(books, "Gatsby")  # Searching by title
