# 1.
# users = [
#     {"id": 1, "name": "ნინო"},
#     {"id": 2, "tags": ["admin"]},
#     {"id": 1, "tags": ["vip"]},
#     {"id": 2, "name": "გიორგი"},
#     {"id": 1, "tags": ["vip", "active"]}
# ]
#
# new_users = {}
#
# for user in users:
#     if user['id'] not in new_users:
#         new_users[user['id']] = user
#
#     for key, value in user.items():
#         new_users[user['id']][key] = value
#
# for user in new_users:
#     print(new_users[user])
#
#
# 2.
# nums = [5, 2, 9, 2, 1, 5, 4, 2]
#
# for i, num in enumerate(nums):
#     for j, num2 in enumerate(nums):
#         if num == num2 and i != j and j != len(nums)-1:
#             nums.remove(num2)
#
# nums.sort()
# print(nums)
#
#
# 3.
# text = "hello world hello python world test test test"
# cnt = 0
# for i in text:
#     if i == ' ':
#         cnt += 1
#
# print(f'There are {cnt+1} words in text')
#
#
# 4.
# emails = [
#     "nugo@gmail.com",
#     "lia@yahoo.com",
#     "nino@gmail.com",
#     "gio@protonmail.com",
#     "dato@yahoo.com"
# ]
#
# new_emails = {}
# for email in emails:
#     email_type = ""
#     for i,ch in enumerate(email):
#         if ch == "@":
#             for ch1 in email[i+1:]:
#                 email_type += ch1
#     email_name = ""
#     for i, ch in enumerate(email):
#         if ch != "@":
#             email_name += ch
#         else:
#             break
#     if email_type not in new_emails:
#         new_emails[email_type] = [email_name]
#     else:
#         new_emails[email_type] += [email_name]
#
# print(new_emails)
#
#
# 5.
# students = [
#     {"name": "Nika", "score": 68},
#     {"name": "Ana", "score": 95},
#     {"name": "Gio", "score": 81},
#     {"name": "Luka", "score": 90}
# ]
#
# string = '123'
# for student in students:
#     if student["score"] >= 80:
#         if len(student["name"]) > 3:
#             print(student)

