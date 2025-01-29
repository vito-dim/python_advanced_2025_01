# data = input()
#
# opening_parentheses = '([{'
# closing_parentheses = ')]}'
#
# my_stack = []
#
# for element in data:
#     if element in opening_parentheses:
#         my_stack.append(element)
#     elif element in closing_parentheses:
#         if not my_stack:
#             print('NO')
#             break
#         last_parenthesis = my_stack.pop()
#         if opening_parentheses.index(last_parenthesis) != closing_parentheses.index(element):
#             print('NO')
#             break
# else:
#     if my_stack:
#         print('NO')
#     else:
#         print('YES')

data = input()
mapper = {
    '(': ')',
    '{': '}',
    '[': ']'
}
my_stack = []

for element in data:
    if element in mapper.keys():
        my_stack.append(element)
    else:
        if not my_stack:
            print('NO')
            exit()
        last_element = my_stack.pop()
        if mapper[last_element] != element:
            print('NO')
            exit()

print('YES')
