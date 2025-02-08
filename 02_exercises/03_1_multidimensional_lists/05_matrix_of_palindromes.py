rows, columns = [int(num) for num in input().split()]
start_index = ord('a')

for row in range(rows):
    for col in range(columns):
        print(f'{chr(start_index + row)}{chr(start_index + row + col)}{chr(start_index + row)}', end=' ')
    print()
