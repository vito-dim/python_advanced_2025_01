# total_queries = int(input())
# stack = []
#
# for _ in range(total_queries):
#     current_query = input().split()
#
#     if current_query[0] == '1':
#         stack.append(int(current_query[1]))
#     elif stack:
#         if current_query[0] == '2':
#             stack.pop()
#         if current_query[0] == '3':
#             print(max(stack))
#         if current_query[0] == '4':
#             print(min(stack))
#
# while stack:
#     if len(stack) > 1:
#         print(stack.pop(), end=', ')
#     else:
#         print(stack.pop(), end='')


# total_queries = int(input())
# stack = []
#
# for _ in range(total_queries):
#     current_query = input().split()
#
#     if current_query[0] == '1':
#         stack.append(int(current_query[1]))
#     elif stack:
#         if current_query[0] == '2':
#             stack.pop()
#         if current_query[0] == '3':
#             print(max(stack))
#         if current_query[0] == '4':
#             print(min(stack))
#
# while stack:
#     print(stack.pop(), end='')
#     if stack:
#         print(', ', end='')


total_queries = int(input())
stack = []

mapper = {
    '1': lambda num: stack.append(int(num)),
    '2': lambda: stack.pop() if stack else None,
    '3': lambda: print(max(stack)) if stack else None,
    '4': lambda: print(min(stack)) if stack else None,
}

for _ in range(total_queries):
    current_query = input().split()
    mapper[current_query[0]](*current_query[1:])
    # if len(current_query) > 1:
    #     mapper[current_query[0]](int(current_query[1]))
    # else:
    #     mapper[current_query[0]]()

print(*reversed(stack), sep=', ')
# while stack:
#     print(stack.pop(), end='')
#     if stack:
#         print(', ', end='')
