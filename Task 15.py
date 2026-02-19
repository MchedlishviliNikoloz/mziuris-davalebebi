class Book:
    def __init__(self, title: str, author: str, pages: int, is_read: bool = False):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__is_read = is_read

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        if pages <= 0:
            raise ValueError("გვერდების რაოდენობა უნდა იყოს დადებითი რიცხვი")
        self.__pages = pages

    def mark_as_read(self):
        self.__is_read = True

    def get_info(self):
        status = "წაკითხულია" if self.__is_read else "არ არის წაკითხული"
        print(f"Title: {self.__title} \nAuthor: {self.__author} \nPages: {self.pages} \nStatus: {status}")
