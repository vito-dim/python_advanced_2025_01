# numbers = [int(num) for num in input().split()]
#
# for _ in range(len(numbers)):
#     print(numbers.pop(), end=' ')

# numbers = [int(num) for num in input().split()]
# while numbers:
#     print(numbers.pop(),end=' ')

numbers = input().split()
while numbers:
    last_number = numbers.pop()
    print(last_number[::-1], end=' ')
