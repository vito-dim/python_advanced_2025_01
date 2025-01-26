matrix_size = int(input())
matrix = []

for row_index in range(matrix_size):
    row_data = [el for el in input()]
    matrix.append(row_data)

target = input()
for row_index in range(matrix_size):
    for col_index in range(matrix_size):
        if target in matrix[row_index][col_index]:
            print(f'({row_index}, {col_index})')
            exit()

print(f'{target} does not occur in the matrix')
