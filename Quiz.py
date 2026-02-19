# 1.
# scores = [54, 81, 23, 90, 45, 77, 88, 39, 100, 67]
# more_then_70 = [n for n in scores if n > 70]
# print(more_then_70)
#
# from_50_to_70 = [n for n in scores if 50 < n < 70]
# print(from_50_to_70)
#
# a = scores[0]
# for i in scores:
#     if i < a:
#         a = i
# print(a)

# 2.
# users = ["Zezva", "GrishaOniani", "Mzia", "Ana", "GrishaOniani", "Zezva"]
# permissions = ["read", "write", "read", "execute", "write", "write"]
#
# user_permissions = {}
# for ind, user in enumerate(users):
#     if user not in user_permissions:
#         user_permissions[user] = []
#         user_permissions[user].append(permissions[ind])
#     else:
#         if permissions[ind] not in user_permissions[user]:
#             user_permissions[user].append(permissions[ind])
#
# print(user_permissions)
#
# for user, permission in user_permissions.items():
#     if len(permission) > 1:
#         print(user, permission)

# 3.
# matrix = [
#     [3, 5, 1],
#     [7, 2, 9],
#     [4, 6, 8]
# ]
#
# column_sums = []
# for row in range(0,3):
#     column = 0
#     for col in range(0,3):
#         column += matrix[col][row]
#     column_sums.append(column)
#
# print(column_sums)
#
# new_matrix = []
# for row in range(0,3):
#     row1 = []
#     for col in range(0,3):
#         row1.append(matrix[row][col]*2)
#     new_matrix.append(row1)
#
# print(new_matrix)