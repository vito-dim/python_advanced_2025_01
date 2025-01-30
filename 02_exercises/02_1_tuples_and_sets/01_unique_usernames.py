# names_count = int(input())
# unique_collection = set()
#
# for _ in range(names_count):
#     name = input()
#     unique_collection.add(name)
#
# print(*unique_collection, sep='\n')

names = set()

for _ in range(int(input())):
    names.add(input())

print('\n'.join(names))
