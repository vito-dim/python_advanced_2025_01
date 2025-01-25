# text = input().split()
#
# while text:
#     last_element = text.pop()
#     print(last_element[::-1], end=" ")


text = list(input())

while text:
    print(text.pop(), end="")
