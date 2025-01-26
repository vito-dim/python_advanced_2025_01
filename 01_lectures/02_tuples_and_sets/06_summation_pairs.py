numbers = [int(num) for num in input().split()]
target_number = int(input())

for i in range(len(numbers)):
    if numbers[i] == '*':
        continue
    for j in range(i + 1, len(numbers)):
        if numbers[j] == '*':
            continue
        if numbers[i] + numbers[j] == target_number:
            print(f'{numbers[i]} + {numbers[j]} = {target_number}')
            numbers[i] = '*'
            numbers[j] = '*'
            break

# numbers = list(map(int, input().split()))
# target = int(input())
#
# targets = set()
# values_map = dict()
#
# for value in numbers:
#     result_number = target - value
#     targets.add(result_number)
#     values_map[result_number] = value
#
# for value in numbers:
#     if value in targets:
#         targets.remove(value)
#         pair = values_map[value]
#         del values_map[value]
#         print(f'{pair} + {value} = {target}')
#     else:
#         result_number = target - value
#         targets.add(result_number)
#         values_map[result_number] = value
