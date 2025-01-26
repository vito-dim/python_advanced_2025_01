# from functools import reduce
#
#
# def operate(operator: str, *args: int) -> int:
#     result = 0
#
#     if operator == '+':
#         for index in range(len(args)):
#             result = reduce(lambda x, y: x + y, args)
#
#     elif operator == '-':
#         result = reduce(lambda x, y: x - y, args)
#
#     elif operator == '*':
#         result = reduce(lambda x, y: x * y, args)
#     elif operator == '/':
#         result = reduce(lambda x, y: x / y, args)
#
#     return result

# from functools import reduce
#
#
# def sum_nums(*args):
#     return reduce(lambda x, y: x + y, args)
#
#
# def sub_nums(*args):
#     return reduce(lambda x, y: x - y, args)
#
#
# def mul_nums(*args):
#     return reduce(lambda x, y: x * y, args)
#
#
# def div_nums(*args):
#     return reduce(lambda x, y: x / y, args)
#
#
# mapper = {
#     "+": sum_nums,
#     "-": sub_nums,
#     "*": mul_nums,
#     "/": div_nums
# }
#
#
# def operate(operator, *args):
#     return mapper[operator](*args)


from functools import reduce


def operate(operator, *args):
    mapper = {
        "+": reduce(lambda x, y: x + y, args),
        "-": reduce(lambda x, y: x - y, args),
        "*": reduce(lambda x, y: x * y, args),
        "/": reduce(lambda x, y: x / y, args)
    }

    return mapper[operator]


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
