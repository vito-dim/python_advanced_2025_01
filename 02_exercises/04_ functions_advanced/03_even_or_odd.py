# def even_odd(*args):
#     if args[-1] == 'even':
#         result = [num for num in args[:-1] if num % 2 == 0]
#         return result
#     elif args[-1] == 'odd':
#         result = [num for num in args[:-1] if num % 2 != 0]
#         return result


# def even_odd(*args):
#     if 'even' in args:
#         return [num for num in args[:-1] if num % 2 == 0]
#     elif 'odd' in args:
#         return [num for num in args[:-1] if num % 2 != 0]


# def even_odd(*args):
#     cmd = args[-1]
#     if cmd == 'even':
#         return [num for num in args[:-1] if num % 2 == 0]
#     return [num for num in args[:-1] if num % 2 != 0]


def even_odd(*args):
    cmd = args[-1]
    if cmd == 'even':
        return list(filter(lambda x: x % 2 == 0, args[:-1]))
    return list(filter(lambda x: x % 2 != 0, args[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
