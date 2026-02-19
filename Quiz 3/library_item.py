from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

class Book(LibraryItem):
    def __init__(self, title: str, author: str, pages: int):
        super().__init__(title, author)
        self.pages = pages

    def get_info(self):
        return f"📖 {self.title} - {self.author} ({self.pages} გვ.)"

    def get_type(self):
        return "წიგნი"

    def __str__(self):
        return self.get_info()

class Magazine(LibraryItem):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.issue_number = issue_number

    def get_info(self):
        return f"📰 {self.title} - {self.author} (სერია #{self.issue_number})"

    def get_type(self):
        return "ჟურნალი"

    def __str__(self):
        return self.get_info()