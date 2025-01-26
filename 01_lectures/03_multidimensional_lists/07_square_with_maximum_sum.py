# matrix_size = input().split(', ')
# rows = int(matrix_size[0])
# columns = int(matrix_size[1])
# matrix = []
#
# for row_index in range(rows):
#     row_data = [int(num) for num in input().split(', ')]
#     matrix.append(row_data)
#
# sub_matrix = []
# max_sub_sum = float('-inf')
# for row_index in range(rows - 1):
#     for column_index in range(columns - 1):
#         up_left = matrix[row_index][column_index]
#         up_right = matrix[row_index][column_index + 1]
#         down_left = matrix[row_index + 1][column_index]
#         down_right = matrix[row_index + 1][column_index + 1]
#
#         current_sub_sum = up_left + up_right + down_left + down_right
#
#         if current_sub_sum > max_sub_sum:
#             max_sub_sum = current_sub_sum
#             sub_matrix = [
#                 [up_left, up_right],
#                 [down_left, down_right]
#             ]
#
# print(*sub_matrix[0])
# print(*sub_matrix[1])
# print(max_sub_sum)


import sys

data = input().split(", ")
rows_count = int(data[0])
cols_count = int(data[1])

matrix = []
for _ in range(rows_count):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

max_sum = -sys.maxsize
sub_matrix = []
for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[row_index]) - 1):
        current_el = matrix[row_index][col_index]
        next_to_current = matrix[row_index][col_index + 1]
        element_below_current = matrix[row_index + 1][col_index]
        element_diagonal_current = matrix[row_index + 1][col_index + 1]

        current_sum = current_el + next_to_current + element_below_current + element_diagonal_current

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [
                [current_el, next_to_current],
                [element_below_current, element_diagonal_current]
            ]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
