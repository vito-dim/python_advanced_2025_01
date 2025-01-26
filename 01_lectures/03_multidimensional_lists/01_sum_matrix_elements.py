rows, columns = input().split(', ')
matrix = []
sum_matrix = 0

for row_index in range(int(rows)):
    data_row = [int(el) for el in input().split(', ')]
    sum_row = sum(data_row)
    matrix.append(data_row)
    sum_matrix += sum_row

print(sum_matrix)
print(matrix)
