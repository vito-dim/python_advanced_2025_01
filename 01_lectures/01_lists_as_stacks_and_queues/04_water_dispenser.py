from collections import deque

water_amount = int(input())
people = deque()

name = input()
while name != 'Start':
    people.append(name)
    name = input()

command = input()
while command != 'End':
    if 'refill' in command:
        _, liters = command.split()
        water_amount += int(liters)
    else:
        liters = int(command)
        if liters <= water_amount:
            print(f'{people.popleft()} got water')
            water_amount -= liters
        else:
            print(f'{people.popleft()} must wait')
    command = input()

print(f'{water_amount} liters left')
