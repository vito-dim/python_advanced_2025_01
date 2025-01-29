rows = int(input())
even_matrix = []

for row_index in range(rows):
    row_numbers = [int(num) for num in input().split(', ') if int(num) % 2 == 0]
    even_matrix.append(row_numbers)

print(even_matrix)

# one-liner:
# print([[int(element) for element in input().split(", ") if int(element) % 2 == 0] for _ in range(int(input()))])