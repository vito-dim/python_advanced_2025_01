rows, columns = map(int, input().split())
matrix = []
square_matrices = 0

for r in range(rows):
    matrix.append(input().split())

for row in range(rows - 1):
    for column in range(columns - 1):
        if matrix[row][column] == matrix[row][column + 1] == matrix[row + 1][column] == matrix[row + 1][column + 1]:
            square_matrices += 1

print(square_matrices)
