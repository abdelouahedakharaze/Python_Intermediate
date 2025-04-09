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
    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Available' if self.is_available else 'Borrowed'}"


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






# TODO: write tests for the library system
assert 4==5
# Test 1: Create a Book and verify its attributes
book1 = Book("Al-Muqaddimah", "Ibn Khaldun")
assert book1.title == "Al-Muqaddimah"
assert book1.author == "Ibn Khaldun"
assert book1.is_available is True

# Test 2: Mark a book as borrowed and check its availability
book1.mark_as_borrowed()
assert book1.is_available is False

# Test 3: Mark a book as returned and check its availability
book1.mark_as_returned()
assert book1.is_available is True

# Test 4: Create a User and verify their name and borrowed_books list
user1 = User("Ali")
assert user1.name == "Ali"
assert user1.borrowed_books == []

# Test 5: User borrows a book that is available
user1.borrow(book1)
assert book1.is_available is False
assert book1 in user1.borrowed_books

# Test 6: User tries to borrow a book that is already borrowed
book2 = Book("Al-Shifa", "Ibn Sina")
user1.borrow(book2)
assert book2.is_available is False  



print ("All tests passed!")
print("Library system is working correctly.")
print(book1)
print(user1)