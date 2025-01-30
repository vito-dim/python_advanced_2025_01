# def calculate_name(name: str) -> int:
#     sum_in_ascii = 0
#     for i in range(len(name)):
#         sum_in_ascii += ord(name[i])
#     return sum_in_ascii
#
#
# name_count = int(input())
# odds = set()
# evens = set()
# row = 1
#
# for _ in range(name_count):
#     current_name = input()
#     name_sum = calculate_name(current_name)
#     final_result = int(name_sum / row)
#
#     if final_result % 2 == 0:
#         evens.add(final_result)
#     else:
#         odds.add(final_result)
#
#     row += 1
#
# if sum(evens) == sum(odds):
#     union_values = odds.union(evens)    # set1 | set2
#     print(*union_values, sep=', ')
# elif sum(evens) < sum(odds):
#     different_values = odds.difference(evens)   # set1 - set2
#     print(*different_values, sep=', ')
# elif sum(evens) > sum(odds):
#     symmetric_diffs = odds.symmetric_difference(evens)  # set1 ^ set2
#     print(*symmetric_diffs, sep=', ')


# from functools import reduce
#
#
# def calculate_name(name: str) -> int:
#     name_in_ascii = [ord(name[i]) for i in range(len(name))]
#     sum_in_ascii = reduce(lambda x,y: x + y, name_in_ascii)
#     return sum_in_ascii
#
#
# name_count = int(input())
# odds = set()
# evens = set()
# row = 1
#
# for _ in range(name_count):
#     current_name = input()
#     name_sum = calculate_name(current_name)
#     final_result = int(name_sum / row)
#
#     evens.add(final_result) if final_result % 2 == 0 else odds.add(final_result)
#
#     row += 1
#
# if sum(evens) == sum(odds):
#     union_values = odds.union(evens)    # set1 | set2
#     print(*union_values, sep=', ')
# elif sum(evens) < sum(odds):
#     different_values = odds.difference(evens)   # set1 - set2
#     print(*different_values, sep=', ')
# elif sum(evens) > sum(odds):
#     symmetric_diffs = odds.symmetric_difference(evens)  # set1 ^ set2
#     print(*symmetric_diffs, sep=', ')


names_count = int(input())

odds = set()
evens = set()

for row in range(1, names_count + 1):
    current_name = input()
    name_sum_ascii = sum(ord(char) for char in current_name)
    current_result = name_sum_ascii // row

    evens.add(current_result) if current_result % 2 == 0 else odds.add(current_result)

sum_odds = sum(odds)
sum_evens = sum(evens)

if sum_odds == sum_evens:
    print(*odds | evens, sep=', ')  # union
elif sum_odds > sum_evens:
    print(*odds - evens, sep=', ')  # difference
else:
    print(*odds ^ evens, sep=', ')  # symmetric diffs
