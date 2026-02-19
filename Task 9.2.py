categories = {
    "ხილი": ["ვაშლი", "ბანანი"],
    "ბოსტნეული": ["სტაფილო", "ხახვი"],
    "საკონდიტრო": ["ბანანი", "ტორტი"]
}

new_categories = {}

for key, values in categories.items():
    for value in values:
        if value not in new_categories:
            new_categories[value] = [key]
        else:
            new_categories[value].append(key)

print(new_categories)