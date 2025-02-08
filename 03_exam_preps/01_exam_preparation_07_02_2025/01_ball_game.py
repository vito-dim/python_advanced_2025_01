from collections import deque

strength = [int(num) for num in input().split()]
accuracy = deque(int(num) for num in input().split())
goals = 0

while strength and accuracy:
    current_sum = strength[-1] + accuracy[0]
    if current_sum == 100:
        strength.pop()
        accuracy.popleft()
        goals += 1
    elif current_sum < 100:
        if strength[-1] < accuracy[0]:
            strength.pop()
        elif strength[-1] > accuracy[0]:
            accuracy.popleft()
        elif strength[-1] == accuracy[0]:
            modified_strength = strength.pop() + accuracy.popleft()
            strength.append(modified_strength)
    elif current_sum > 100:
        decreased_strength = strength.pop() - 10
        strength.append(decreased_strength)
        accuracy.rotate(-1)

if goals == 3:
    print('Paul scored a hat-trick!')
elif goals == 0:
    print('Paul failed to score a single goal.')
elif goals > 3:
    print('Paul performed remarkably well!')
elif 0 < goals < 3:
    print('Paul failed to make a hat-trick.')

if goals:
    print(f'Goals scored: {goals}')
if strength:
    print(f'Strength values left: {", ".join(str(num) for num in strength)}')
if accuracy:
    print(f'Accuracy values left: {", ".join(str(num) for num in accuracy)}')
