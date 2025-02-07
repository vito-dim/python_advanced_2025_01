# def negative_vs_positive(*args):
#     sum_n = 0
#     sum_p = 0
#
#     for number in args:
#         if number < 0:
#             sum_n += number
#         elif number > 0:
#             sum_p += number
#
#     if abs(sum_n) > sum_p:
#         return f'{sum_n}\n{sum_p}\nThe negatives are stronger than the positives'
#     return f'{sum_n}\n{sum_p}\nThe positives are stronger than the negatives'
#
#
# numbers = [int(num) for num in input().split()]
#
# print(negative_vs_positive(*numbers))

# def num_sums(*args):
#     n_sum = sum(num for num in args if num < 0)
#     p_sum = sum(num for num in args if num > 0)
#     return n_sum, p_sum
#
#
# nums = map(int, input().split())
# negative_sum, positive_sum = num_sums(*nums)
#
# if abs(negative_sum) > positive_sum:
#     print(f'{negative_sum}\n{positive_sum}\nThe negatives are stronger than the positives')
# else:
#     print(f'{negative_sum}\n{positive_sum}\nThe positives are stronger than the negatives')

def num_sums(*args):
    n_sum = sum(filter(lambda x: x < 0, args))
    p_sum = sum(filter(lambda x: x > 0, args))
    return n_sum, p_sum


nums = map(int, input().split())
negative_sum, positive_sum = num_sums(*nums)

if abs(negative_sum) > positive_sum:
    print(f'{negative_sum}\n{positive_sum}\nThe negatives are stronger than the positives')
else:
    print(f'{negative_sum}\n{positive_sum}\nThe positives are stronger than the negatives')
