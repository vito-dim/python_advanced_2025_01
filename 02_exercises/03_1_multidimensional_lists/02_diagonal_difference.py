# size = int(input())
# matrix = []
# for _ in range(size):
#     current_row = [int(num) for num in input().split()]
#     matrix.append(current_row)
#
# primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
# secondary_diagonal = [matrix[i][-i - 1] for i in range(len(matrix))]
# difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
#
# print(difference)


matrix = [[int(num) for num in input().split()] for _ in range(int(input()))]
primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][-i - 1] for i in range(len(matrix))]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
