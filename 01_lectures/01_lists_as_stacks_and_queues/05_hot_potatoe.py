# from collections import deque
#
# names = deque(input().split())
# count = int(input())
#
# while len(names) > 1:
#     for _ in range(count - 1):
#         current_name = names.popleft()
#         names.append(current_name)
#
#     else:
#         name_to_remove = names.popleft()
#         print(f'Removed {name_to_remove}')
#
# print(f'Last is {names[0]}')

from collections import deque

kids = deque(input().split())
n = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-n)
    removed_kid = kids.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {kids[0]}")
