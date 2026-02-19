new_list = ['btu', 'test', 12, True, 'btu', 'python is best']
a = input('Enter string to find in list: ')
new_list_ind = []
for i in range(len(new_list)):
    if a == new_list[i]:
        new_list_ind.append(i)

print(f'შეყვანილი ელემენტი {a} მოიძებნა ინდექსებზე: {new_list_ind}')
