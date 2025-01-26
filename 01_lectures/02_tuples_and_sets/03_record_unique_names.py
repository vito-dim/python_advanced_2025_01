# name_count = int(input())
# unique_list = set()
#
# for _ in range(name_count):
#     name = input()
#     unique_list.add(name)
#
# for name in unique_list:
#     print(name)

name_count = int(input())
unique_list = set()

for _ in range(name_count):
    name = input()
    unique_list.add(name)

print(*unique_list, sep='\n')
