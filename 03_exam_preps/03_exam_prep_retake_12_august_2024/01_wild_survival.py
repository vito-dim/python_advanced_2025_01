from collections import deque

bees = deque(int(num) for num in input().split())
bee_eaters = [int(num) for num in input().split()]

while bees and bee_eaters:
    defenders = bees.popleft()
    attackers = bee_eaters.pop()
    while attackers and defenders:
        if defenders < 7:
            break
        defenders -= 7
        attackers -= 1
    if attackers:
        bee_eaters.append(attackers)
    elif defenders:
        bees.append(defenders)

print('The final battle is over!')

if len(bees) == 0 and len(bee_eaters) == 0:
    print('But no one made it out alive!')

if bees:
    print(f'Bee groups left: {", ".join([str(num) for num in bees])}')
elif bee_eaters:
    print(f'Bee-eater groups left: {", ".join([str(num) for num in bee_eaters])}')
