size = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(size)]

while True:
    line = input().split()
    command = line[0]
    cords = [int(num) for num in line[1:]]
    if command == 'END':
        break
    if cords[0] in range(0, len(matrix)) and cords[1] in range(len(matrix)):
        if command == 'Add':
            matrix[cords[0]][cords[1]] += cords[2]
        elif command == 'Subtract':
            matrix[cords[0]][cords[1]] -= cords[2]
    else:
        print('Invalid coordinates')

for row in matrix:
    print(*row)
