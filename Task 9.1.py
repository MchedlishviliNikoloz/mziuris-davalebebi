users = [
    {"id": 1, "name": "ნუგო"},
    {"id": 2, "age": 21},
    {"id": 1, "age": 30},
    {"id": 3, "name": "ხრუსტალი"},
    {"id": 2, "name": "ზალიკო"}
]

new_users = {}

for user in users:
    if user["id"] not in new_users:
        new_users[user["id"]] = user

    for key, value in user.items():
        new_users[user["id"]][key] = value

print(new_users)