data = tuple([float(num) for num in input().split()])
num_dict = {}

for element in data:
    num_dict[element] = data.count(element)

for num, occur in num_dict.items():
    print(f'{num:.1f} - {occur} times')
