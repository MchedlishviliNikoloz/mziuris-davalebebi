from library_item import Book, Magazine
from member import Member

def display_items(items: list):
    for item in items:
        print (f"[{item.get_type()}] {item.get_info()} - {'✅ ხელმისაწვდომი' if item.is_available else '❌ გატანილია'}")

member1 = Member("ABC")
member2 = Member("DEF")
book1 = Book("Title", "Author", 120)
book2 = Book("Title 2", "Author 2", 150)
magazine1 = Magazine("Title", "Author", 200)

try:
    # ელემენტის გატანა
    member1.borrow_item(book1)

    # იგივე ელემენტის ხელმეორედ გატანის მცდელობა
    member1.borrow_item(book1)  # ← უნდა დააგდოს ValueError!

    member1.library_info()

    print(member1)

    # ელემენტის გატანა
    member2.borrow_item(book2)

    print(member1.borrowed_items)
    print(member2.borrowed_items)

    print(member1 < member2)
    print(member1 == member2)

    print(book1.get_type())

    display_items([book1, book2, magazine1])

except ValueError as e:
    print(f"❌ შეცდომა: {e}")
