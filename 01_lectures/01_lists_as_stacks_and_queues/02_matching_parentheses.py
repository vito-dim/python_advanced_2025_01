# text = list(input())
#
# stack = []
#
# for index in range(len(text)):
#     if text[index] == "(":
#         stack.append(index)
#     elif text[index] == ")":
#         start_index = stack.pop()
#         end_index = index
#         print("".join(text[start_index:end_index + 1]))

text = input()
stack = []

for index in range(len(text)):
    if text[index] == "(":
        stack.append(index)
    elif text[index] == ")":
        stack_index = stack.pop()
        end_index = index + 1
        print(text[stack_index:end_index])
