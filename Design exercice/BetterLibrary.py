# This code implements a simple library system with classes for Book, User, and Library.
# its better than the design in the faultyLibraryDesign.puml
# but the exercice is to spot the design flaws in the code and improve it.


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True

    def mark_as_borrowed(self):
        self.is_available = False

    def mark_as_returned(self):
        self.is_available = True


class User:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books: list[Book] = []

    def borrow(self, book: Book):
        if book.is_available:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}'")


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.users: list[User] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def register_user(self, user: User):
        self.users.append(user)

    def checkout(self, book: Book, user: User):
        user.borrow(book)

    def return_book(self, book: Book, user: User):
        user.return_book(book)



