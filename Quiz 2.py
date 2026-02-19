def deposit(bal: float, am: float) -> float:
    if am < 0:
        raise ValueError("შესატანი თანხა არ უნდა იყოს უარყოფითი")
    return bal + am

def withdraw(bal: float, am: float) -> float:
    if am < 0:
        raise ValueError("გამოსატანი თანხა არ უნდა იყოს უარყოფითი")
    if am > bal:
        raise ValueError("ანგარიშზე არის არასაკმარისი თანხა")
    return bal - am

def get_balance(bal: float) -> float:
    return bal

def bank_menu() -> int:
    print("1. თანხის შეტანა")
    print("2. თანხის გამოტანა")
    print("3. ბალანსის ნახვა")
    print("4. გამოსვლა")
    return int(input("აირჩიეთ ოპერაცია: "))


while True:
    try:
        balance = float(input("შემოიყვანეთ საწყისი ბალანსი: "))
        if balance < 0:
            raise ValueError("საწყისი ბალანსი არ უნდა იყოს უარყოფითი")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        op = bank_menu()

        if op == 1:
            amount = float(input("შემოიყვანეთ შესატანი თანხა: "))
            balance = deposit(balance, amount)
            print(f"ოპერაცია წარმატებით შესრულდა. ბალანსზე არის: {balance}ლარი")
        elif op == 2:
            amount = float(input("შემოიყვანეთ გამოსატანი თანხა: "))
            balance = withdraw(balance, amount)
            print(f"ოპერაცია წარმატებით შესრულდა. ბალანსზე არის: {balance}ლარი")
        elif op == 3:
            print(f"თქვენი ბალანსი შეადგენს: {get_balance(balance)} ლარს")
        elif op == 4:
            print("პროგრამის დასრულება")
            break
        else:
            print("არასწორი მენიუს არჩევანი, აირჩიე თავიდან")

    except ValueError as e:
        print(e)
