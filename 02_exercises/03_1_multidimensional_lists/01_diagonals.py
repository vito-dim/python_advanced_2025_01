# rows = int(input())
# matrix = [input().split(', ') for _ in range(rows)]
# primary_diagonal = []
# secondary_diagonal = []
# for row in range(len(matrix)):
#     for column in range(len(matrix)):
#         if row == column:
#             primary_diagonal.append(int(matrix[row][column]))
#
# for row in range(len(matrix)):
#     for column in range(len(matrix)):
#         if (row + column) == (len(matrix) - 1):
#             secondary_diagonal.append(int(matrix[row][column]))
#
# sum_primary = sum(primary_diagonal)
# sum_secondary = sum(secondary_diagonal)
#
# print(f'Primary diagonal: {", ".join([str(num) for num in primary_diagonal])}. Sum: {sum_primary}')
# print(f'Secondary diagonal: {", ".join([str(num) for num in secondary_diagonal])}. Sum: {sum_secondary}')

matrix = [[int(num) for num in input().split(', ')] for _ in range(int(input()))]
primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][-1 - i] for i in range(len(matrix))]

print(f'Primary diagonal: {", ".join(str(num) for num in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(num) for num in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')
