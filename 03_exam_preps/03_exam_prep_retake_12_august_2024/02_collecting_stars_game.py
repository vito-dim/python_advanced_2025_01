size = int(input())
field = []
player = []
stars = 2
total_stars = 0
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1), }
counter = 0
for r in range(size):
    field.append(input().split())
    for c in range(size):
        if field[r][c] == 'P':
            player = [r, c]
            field[r][c] = '.'
        if field[r][c] == '*':
            total_stars += 1

while stars != 0 and stars != 10:
    if total_stars == 0:
        break
    counter += 1
    command = input()
    move = directions[command]
    new_r = player[0] + move[0]
    new_c = player[1] + move[1]
    if 0 <= new_r < size and 0 <= new_c < size:
        if field[new_r][new_c] == '*':
            stars += 1
            total_stars -= 1
            field[new_r][new_c] = '.'
            player = [new_r, new_c]
        elif field[new_r][new_c] == '#':
            stars -= 1
        else:
            player = [new_r, new_c]
    else:
        player = [0, 0]
        if field[0][0] == '*':
            field[0][0] = '.'
            stars += 1
            total_stars -= 1
        elif field[0][0] == '#':
            stars -= 1

field[player[0]][player[1]] = 'P'

if stars == 10:
    print('You won! You have collected 10 stars.')
else:
    print('Game over! You are out of any stars.')

print(f'Your final position is [{player[0]}, {player[1]}]')

[print(*row) for row in field]
