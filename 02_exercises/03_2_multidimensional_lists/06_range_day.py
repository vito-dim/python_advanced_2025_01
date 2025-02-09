SIZE = 5
matrix = []
player_position = []
targets = 0
targets_down = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(SIZE):
    matrix.append(input().split())
    for c in range(SIZE):
        if matrix[r][c] == 'A':
            player_position = [r, c]
        elif matrix[r][c] == 'x':
            targets += 1

commands_count = int(input())
for _ in range(commands_count):
    command = input().split()
    if command[0] == 'shoot':
        row = player_position[0] + directions[command[1]][0]
        col = player_position[1] + directions[command[1]][1]

        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                targets -= 1
                targets_down.append([row, col])
                break
            row += directions[command[1]][0]
            col += directions[command[1]][1]

        if targets == 0:
            print(f'Training completed! All {len(targets_down)} targets hit.')
            break
    elif command[0] == 'move':
        steps = int(command[2])
        row = player_position[0] + directions[command[1]][0] * steps
        col = player_position[1] + directions[command[1]][1] * steps
        if 0 <= row < SIZE and 0 <= col < SIZE and matrix[row][col] == '.':
            matrix[row][col] = 'A'
            matrix[player_position[0]][player_position[1]] = '.'
            player_position = [row, col]

if targets > 0:
    print(f'Training not completed! {targets} targets left.')

for row in targets_down:
    print(row)
