# def pos_is_valid(r1, c1, r2, c2, rs, cls):
#     return 0 <= r1 < rs and 0 <= r2 < rs and 0 <= c1 < cls and 0 <= c2 < cls
#
#
# rows, columns = map(int, input().split())
# matrix = [input().split() for _ in range(rows)]
#
# command = input()
# while command != 'END':
#     current_command = command.split()
#     if current_command[0] != 'swap' or len(current_command) != 5:
#         print('Invalid input!')
#         command = input()
#         continue
#
#     row1, col1, row2, col2 = [int(i) for i in current_command[1:]]
#     if pos_is_valid(row1, col1, row2, col2, rows, columns):
#         matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#         [print(*row) for row in matrix]
#     else:
#         print('Invalid input!')
#
#     command = input()



def pos_is_valid(r1, c1, r2, c2, rs, cls):
    return 0 <= r1 < rs and 0 <= r2 < rs and 0 <= c1 < cls and 0 <= c2 < cls


rows, columns = map(int, input().split())
matrix = [input().split() for _ in range(rows)]


while True:
    line = input()
    if line == 'END':
        break

    command = line.split()
    if command[0] != 'swap' or len(command) != 5:
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(i) for i in command[1:]]
    if pos_is_valid(row1, col1, row2, col2, rows, columns):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print('Invalid input!')
