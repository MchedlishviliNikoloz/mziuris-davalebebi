class Book:
    def __init__(self,  title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__is_available = True

    def __str__(self):
        available = "Available" if self.__is_available else "Not Available"
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"ISBN: {self.isbn}\n"
                f"Status: {available}")

    @property
    def status(self):
        available = "Available" if self.__is_available else "Not Available"
        return available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            return True
        return False

    @staticmethod
    def is_valid_isbn(isbn: str):
        return isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()

    @classmethod
    def create_textbook(cls, title, isbn):
        author = "School Text book"
        if not cls.is_valid_isbn(isbn):
            raise ValueError("Invalid ISBN")
        return cls(title, author, isbn)


class Member:
    def __init__(self, name: str,  member_id: str, borrowed_books: list = None):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books
        if borrowed_books == None:
            self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                return True
        return False

    @property
    def books_count(self):
        return len(self.borrowed_books)


class PremiumMember(Member):
    def __init__(self, name: str,  member_id: str, borrowed_books: list):
        super().__init__(name,  member_id, borrowed_books,)
        self.max_books = 5

    def borrow_book(self, book):
        if self.books_count >= self.max_books:
            return False
        return super().borrow_book(book)
