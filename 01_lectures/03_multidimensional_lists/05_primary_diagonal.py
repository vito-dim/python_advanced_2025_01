# matrix_size = int(input())
# matrix = []
# primary_diagonal = 0
#
# for _ in range(matrix_size):
#     row_data = [int(num) for num in input().split()]
#     matrix.append(row_data)
#
# for row_index in range(matrix_size):
#     for col_index in range(matrix_size):
#         if row_index == col_index:
#             primary_diagonal += matrix[row_index][col_index]
#         else:
#             continue
#
# print(primary_diagonal)

matrix_size = int(input())
primary_diagonal = 0

for index in range(matrix_size):
    row_data = [int(num) for num in input().split()]
    primary_diagonal += row_data[index]

print(primary_diagonal)
