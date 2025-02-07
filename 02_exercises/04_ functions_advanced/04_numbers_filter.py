# def even_odd_filter(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         if key == 'even':
#             result[key] = [num for num in value if num % 2 == 0]
#         elif key == 'odd':
#             result[key] = [num for num in value if num % 2 != 0]
#
#     result = sorted(result.items(), key=lambda kvp: -len(kvp[1]))
#     return dict(result)


# def even_odd_filter(**kwargs):
#     result = dict()
#     for key, value in kwargs.items():
#         if key == 'even':
#             result[key] = [num for num in value if num % 2 == 0]
#         elif key == 'odd':
#             result[key] = [num for num in value if num % 2 != 0]
#
#     return dict(sorted(result.items(), key=lambda kvp: -len(kvp[1])))


def even_odd_filter(**kwargs):
    for key, numbers in kwargs.items():
        if key == 'even':
            kwargs[key] = [num for num in numbers if num % 2 == 0]
        else:
            kwargs[key] = [num for num in numbers if num % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda kvp: -len(kvp[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
