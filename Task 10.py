transactions = {
"t1": {"user": "Alice", "amount": 120},
"t2": {"user": "Bob", "amount": 75},
"t3": {"user": "Alice", "amount": 200},
"t4": {"user": "Charlie", "amount": 50},
"t5": {"user": "Bob", "amount": 130},
}

user_total = {}
for tr_id, data in transactions.items():
    if data["user"] not in user_total:
        user_total[data["user"]] = data["amount"]
    else:
        user_total[data["user"]] += data["amount"]

user_over_150 = []
for user,amount in user_total.items():
    if amount > 150:
        user_over_150.append(user)

user_150_one_tr = {}
for tr_id, data in transactions.items():
    if data["amount"] > 150:
        if data["user"] not in user_150_one_tr:
            user_150_one_tr[data["user"]] = [tr_id]
        else:
            user_150_one_tr[data["user"]].append(tr_id)

print(user_total)
print(user_over_150)
print(user_150_one_tr)