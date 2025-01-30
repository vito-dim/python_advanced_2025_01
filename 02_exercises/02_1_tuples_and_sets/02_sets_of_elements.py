# first_length, second_length = input().split()
#
# first_set = set()
# second_set = set()
#
# for _ in range(int(first_length)):
#     num = int(input())
#     first_set.add(num)
#
# for _ in range(int(second_length)):
#     num = int(input())
#     second_set.add(num)
#
# for num in first_set:
#     if num in second_set:
#         print(num)

# n, m = map(int, input().split())
# first_set = set()
# second_set = set()
#
# for _ in range(n):
#     first_set.add(int(input()))
#
# for _ in range(m):
#     second_set.add(int(input()))
#
# result = first_set.intersection(second_set)
# # result = first_set & second_set
#
# print(*result, sep='\n')

n, m = map(int, input().split())
first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

print(*first_set.intersection(second_set), sep='\n')
