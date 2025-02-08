# 90 / 100
# def is_valid_pos(r, c, max_row, max_col) -> bool:
#     return 0 <= r < max_row and 0 <= c < max_col
#
#
# rows, columns = [int(num) for num in input().split(', ')]
# matrix = [list(input()) for _ in range(rows)]
# counter = 16
# bomb_defused = False
# ct_start = []
# ct_move = []
# generic_error = 'Terrorists win!'
#
# movement = {
#     'up': lambda x, y: [x - 1, y],
#     'down': lambda x, y: [x + 1, y],
#     'right': lambda x, y: [x, y + 1],
#     'left': lambda x, y: [x, y - 1]
# }
#
# for row in range(rows):
#     if 'C' in matrix[row]:
#         col_index = matrix[row].index('C')
#         ct_start = [row, col_index]
#         ct_move = ct_start.copy()
#         break
#
# while True:
#     if counter == 0 or bomb_defused:
#         if not bomb_defused:
#             print(generic_error)
#             print('Bomb was not defused successfully!')
#             print(f'Time needed: {abs(counter)} second/s.')
#         break
#
#     current_cords = ct_move
#     command = input()
#     if command in movement:
#         new_cords = movement[command](current_cords[0], current_cords[1])
#         if is_valid_pos(new_cords[0], new_cords[1], rows, columns):
#             if matrix[new_cords[0]][new_cords[1]] == 'T':
#                 print(generic_error)
#                 matrix[new_cords[0]][new_cords[1]] = '*'
#                 break
#             ct_move = new_cords
#         else:
#             counter -= 1
#             continue
#
#     if command == 'defuse':
#         if matrix[current_cords[0]][current_cords[1]] == 'B':
#             counter -= 4
#             if counter > 0:
#                 matrix[current_cords[0]][current_cords[1]] = 'D'
#                 print('Counter-terrorist wins!')
#                 print(f'Bomb has been defused: {counter} second/s remaining.')
#                 bomb_defused = True
#             else:
#                 matrix[current_cords[0]][current_cords[1]] = 'X'
#                 print(generic_error)
#                 print('Bomb was not defused successfully!')
#                 print(f'Time needed: {abs(counter)} second/s.')
#                 break
#         else:
#             counter -= 1
#
#     counter -= 1
#
# [print(''.join(row)) for row in matrix]

# 100/ 100
rows, columns = [int(num) for num in input().split(', ')]
matrix = []
ct_position = []

for r in range(rows):
    matrix.append(list(input()))
    for c in range(columns):
        if matrix[r][c] == 'C':
            ct_position = [r, c]
            break

moves = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
time = 16
bomb_defused = False
ct_killed = False

while time:
    time -= 1

    command = input()
    if command == 'defuse':
        if matrix[ct_position[0]][ct_position[1]] != 'B':
            time -= 1
        else:
            time -= 3
            if time >= 0:
                matrix[ct_position[0]][ct_position[1]] = 'D'
                bomb_defused = True
            else:
                matrix[ct_position[0]][ct_position[1]] = 'X'
            break
    else:
        move = moves[command]
        new_r = ct_position[0] + move[0]
        new_c = ct_position[1] + move[1]
        if 0 <= new_r < rows and 0 <= new_c < columns:
            if matrix[new_r][new_c] == 'T':
                matrix[new_r][new_c] = '*'
                ct_killed = True
                break
            else:
                ct_position = [new_r, new_c]

if bomb_defused:
    print('Counter-terrorist wins!')
    print(f'Bomb has been defused: {time} second/s remaining.')
else:
    print('Terrorists win!')
    if not ct_killed:
        print('Bomb was not defused successfully!')
        print(f'Time needed: {abs(time)} second/s.')

[print(''.join(row)) for row in matrix]
