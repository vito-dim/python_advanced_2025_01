presents = int(input())
size = int(input())
matrix = []
santa = []
nice_kids = 0
presents_given = 0

for r in range(size):
    matrix.append(input().split())
    for c in range(size):
        if matrix[r][c] == 'S':
            santa = [r, c]
        elif matrix[r][c] == 'V':
            nice_kids += 1

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while presents > 0:
    command = input()
    if command == 'Christmas morning':
        break

    move = directions[command]
    new_r = santa[0] + move[0]
    new_c = santa[1] + move[1]
    if 0 <= new_r < size and 0 <= new_c < size:
        if matrix[new_r][new_c] == 'V':
            presents -= 1
            presents_given += 1
            matrix[new_r][new_c] = '-'
        elif matrix[new_r][new_c] == 'X':
            matrix[new_r][new_c] = '-'
        elif matrix[new_r][new_c] == 'C':
            for values in directions.values():
                current_move = values
                c_row = new_r + current_move[0]
                c_col = new_c + current_move[1]
                if matrix[c_row][c_col] in ('V', 'X') and presents > 0:
                    presents -= 1
                    if matrix[c_row][c_col] == 'V':
                        presents_given += 1
                    matrix[c_row][c_col] = '-'

        matrix[santa[0]][santa[1]] = '-'
        santa = [new_r, new_c]
        matrix[new_r][new_c] = 'S'

kids_to_presents_diff = nice_kids - presents_given
if presents < 1 and kids_to_presents_diff > 0:
    print('Santa ran out of presents!')

[print(*row) for row in matrix]

if kids_to_presents_diff > 0:
    print(f'No presents for {kids_to_presents_diff} nice kid/s.')
else:
    print(f'Good job, Santa! {presents_given} happy nice kid/s.')
