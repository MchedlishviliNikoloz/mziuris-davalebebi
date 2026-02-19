import random

class Member:
    def __init__(self, name: str):
        self.name = name
        self.member_id = random.randint(1000, 9999)
        self.__borrowed_items = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) - ნასესხები: {len(self.borrowed_items)} ელემენტი"

    def __lt__(self, other):
        return len(self.__borrowed_items) < len(other.__borrowed_items)

    def __eq__(self, other):
        return len(self.__borrowed_items) == len(other.__borrowed_items)

    @property
    def borrowed_items(self):
        return self.__borrowed_items

    def borrow_item(self, item):
        try:
            if not item.is_available:
                raise ValueError("ეს ელემენტი უკვე გატანილია!")
            self.__borrowed_items.append(item)
            item.is_available = False
        except ValueError as e:
            print(e)

    def return_item(self, item):
        try:
            if item not in self.__borrowed_items:
                raise ValueError("ეს ელემენტი არ გიგატანია!")
            self.__borrowed_items.remove(item)
            item.is_available = True
        except ValueError as e:
            print(e)

    @staticmethod
    def library_info():
        print("ბიბლიოთეკა გახსნილია 9:00-18:00")