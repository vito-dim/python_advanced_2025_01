size = int(input())
matrix = []
bunny = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'B':
            bunny = [row, col]

moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
max_dir = ''
max_eggs = -float('inf')
max_eggs_matrix = []

for direction, move in moves.items():
    current_eggs = 0
    current_eggs_matrix = []
    current_row = bunny[0] + move[0]
    current_col = bunny[1] + move[1]
    while 0 <= current_row < size and 0 <= current_col < size:
        if matrix[current_row][current_col] == 'X':
            break
        current_eggs += int(matrix[current_row][current_col])
        current_eggs_matrix.append([current_row, current_col])
        current_row += move[0]
        current_col += move[1]

    if current_eggs > max_eggs and current_eggs_matrix:
        max_dir = direction
        max_eggs = current_eggs
        max_eggs_matrix = current_eggs_matrix

print(max_dir)
[print(row) for row in max_eggs_matrix]
print(max_eggs)
