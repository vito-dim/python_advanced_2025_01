from collections import deque

chocolates = list(map(int, input().split(', ')))
milk = deque(int(num) for num in input().split(', '))
milkshakes = 0

while milkshakes < 5 and chocolates and milk:
    if chocolates[-1] <= 0 and milk[0] <= 0:
        chocolates.pop()
        milk.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue

    if chocolates[-1] == milk[0]:
        milkshakes += 1
        chocolates.pop()
        milk.popleft()
    else:
        milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print(f'Chocolate: {", ".join(str(num) for num in chocolates) if chocolates else "empty"}')
print(f'Milk: {", ".join(str(num) for num in milk) if milk else "empty"}')
