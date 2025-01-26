matrix_size = input().split(', ')
rows = int(matrix_size[0])
col = int(matrix_size[1])
matrix = []

for row_index in range(rows):
    row_data = [int(num) for num in input().split()]
    matrix.append(row_data)

for col_index in range(col):
    column_sum = 0
    for row_index in range(col):
        column_sum += matrix[row_index][col_index]
    print(column_sum)
