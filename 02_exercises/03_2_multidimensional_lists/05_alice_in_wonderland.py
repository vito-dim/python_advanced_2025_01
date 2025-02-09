size = int(input())
matrix = []
alice = []
tea = 0

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append([int(el) if el.isdigit() else el for el in input().split()])
    for col in range(size):
        if matrix[row][col] == 'A':
            matrix[row][col] = '*'
            alice = [row, col]

while tea < 10:
    command = input()
    new_row = alice[0] + moves[command][0]
    new_col = alice[1] + moves[command][1]
    if new_row < 0 or new_row >= size or new_col < 0 or new_col >= size:
        break
    if matrix[new_row][new_col] == 'R':
        matrix[new_row][new_col] = '*'
        break
    if type(matrix[new_row][new_col]) is int:
        tea += matrix[new_row][new_col]
    matrix[new_row][new_col] = '*'
    alice = [new_row, new_col]

if tea >= 10:
    print('She did it! She went to the party.')
else:
    print('Alice didn\'t make it to the tea party.')

[print(*row) for row in matrix]
