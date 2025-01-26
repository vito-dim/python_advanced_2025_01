# rows = int(input())
# flat_matrix = []
#
# for _ in range(rows):
#     current_row = [int(num) for num in input().split(', ')]
#     flat_matrix.extend(current_row)
#
# print(flat_matrix)

rows = int(input())
flat_matrix = []

for _ in range(rows):
    for number in input().split(', '):
        flat_matrix.append(int(number))

print(flat_matrix)
