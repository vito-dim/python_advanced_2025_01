# def recursive_power(num: int, power: int) -> int:
#     return num ** power

def recursive_power(num: int, power: int) -> int:
    if power == 1:
        return num
    return num * recursive_power(num, power - 1)


print(recursive_power(2, 10))

# a = {"a": {1: [{'f': 1}]}, "b": [1, 2, 3], "c": {0: {1: {2: {"c": [{"k": 3}]}}}}}
# def obtain_softuni_courses(n=3):
#     res = requsts.get("https://softuni.bg/trainings/4839/python-advanced-january-2025")
#     if res.status in (500, 503):
#         if n != 0:
#             obtain_softuni_courses()
#
#         else:
#             return "Softuni is not available"
#     else:
#         return res.data
