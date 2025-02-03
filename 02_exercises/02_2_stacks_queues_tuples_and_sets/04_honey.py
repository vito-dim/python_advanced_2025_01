# # 57%
# from collections import deque
#
# bees = deque(int(num) for num in input().split())
# nectar = [int(num) for num in input().split()]
# symbols = deque(input().split())
# honey = 0
#
# operations = {
#     '+': lambda x, y: x + y,
#     '-': lambda x, y: x - y,
#     '*': lambda x, y: x * y,
#     '/': lambda x, y: x // y
# }
#
# while bees and nectar:
#     matched_bee = 0
#     matched_nectar = 0
#     calc_honey = 0
#     while nectar:
#         if nectar[-1] >= bees[0]:
#             matched_bee = bees[0]
#             matched_nectar = nectar[-1]
#             break
#         else:
#             nectar.pop()
#             continue
#
#     if symbols[0] == '/' and matched_nectar == 0:
#         bees.popleft()
#         symbols.popleft()
#         nectar.pop()
#         continue
#     else:
#         calc_honey = operations[symbols[0]](matched_bee, matched_nectar)
#         honey += abs(calc_honey)
#         bees.popleft()
#         symbols.popleft()
#         nectar.pop()
#
# print(f'Total honey made: {honey}')
# if bees:
#     print(f'Bees left: {", ".join(str(num) for num in bees)}')
#
# if nectar:
#     print(f'Nectar left: {", ".join(str(num) for num in nectar)}')


from collections import deque

bees = deque(int(num) for num in input().split())
nectar = [int(num) for num in input().split()]
symbols = deque(input().split())
honey = 0

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else 0
}

while bees and nectar:
    if nectar[-1] >= bees[0]:
        honey += abs(operations[symbols[0]](bees[0], nectar[-1]))
        nectar.pop()
        bees.popleft()
        symbols.popleft()

    else:
        nectar.pop()


print(f'Total honey made: {honey}')
if bees:
    print(f'Bees left: {", ".join(str(num) for num in bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(num) for num in nectar)}')
