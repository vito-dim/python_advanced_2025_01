# ls = [item.split() for item in input().split('|')]
# flatten_list = []
#
# for i in range(len(ls) - 1, -1, -1):
#     for num in ls[i]:
#         flatten_list.append(num)
#
# print(*flatten_list)


ls = [item.split() for item in input().split('|')]
flatten_list = [num for i in range(len(ls)-1,-1,-1) for num in ls[i]]

print(*flatten_list)
