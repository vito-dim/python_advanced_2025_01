# from collections import deque
# from functools import reduce
#
#
# def operation(operator, num_list):
#     nums = [int(num) for num in num_list]
#
#     mapper = {
#         "*": reduce(lambda x, y: x * y, nums),
#         "+": reduce(lambda x, y: x + y, nums),
#         "-": reduce(lambda x, y: x - y, nums),
#         "/": reduce(lambda x, y: x // y, nums)
#     }
#     return mapper[operator]
#
#
# operators = ["*", "+", "-", "/"]
# default_input = input().split()
# expression = deque(int(el) if el not in operators else el for el in default_input)
#
# while len(expression) > 1:
#     current_numbers = []
#     current_operator = ''
#     for i in range(len(expression)):
#         if expression[i] not in operators:
#             current_numbers.append(expression[i])
#         else:
#             current_operator = expression[i]
#             break
#
#     for _ in range(len(current_numbers) + 1):
#         expression.popleft()
#
#     operation_result = operation(current_operator, current_numbers)
#     expression.appendleft(operation_result)
#
# print(*expression)


from collections import deque

expression = input().split()
numbers = deque()

operation = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}

for char in expression:
    if char not in operation.keys():
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            operation_result = operation[char](first_num, second_num)
            numbers.appendleft(operation_result)

print(*numbers)

# calculate using strings, but not a good practise = > result = eval(str(num1) + char.replace('/','//') + str(num2))