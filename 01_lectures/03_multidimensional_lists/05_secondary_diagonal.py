matrix_size = int(input())
matrix = []
secondary_diagonal = 0

for row_index in range(matrix_size):
    row_data = [int(num) for num in input().split()]
    matrix.append(row_data)

for row_index in range(matrix_size):
    for col_index in range(matrix_size):
        if (row_index + col_index) == (matrix_size - 1):
            secondary_diagonal += matrix[row_index][col_index]

print(secondary_diagonal)
