# size = int(input())
# matrix = []
# ship = []
# fuel = 100
# planet_reached = False
# is_stranded = False
# is_lost = False
#
# for r in range(size):
#     matrix.append(input().split())
#     for c in range(size):
#         if matrix[r][c] == 'S':
#             ship = [r, c]
#             matrix[r][c] = '.'
#
# directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
#
# while True:
#     command = input()
#     fuel -= 5
#     move = directions[command]
#     new_r = ship[0] + move[0]
#     new_c = ship[1] + move[1]
#     if 0 <= new_r < size and  0 <= new_c < size:
#         if matrix[new_r][new_c] == 'R':
#             fuel += 10
#             if fuel > 100:
#                 fuel = 100
#         elif matrix[new_r][new_c] == 'M':
#             fuel -= 5
#         elif matrix[new_r][new_c] == 'P':
#             if matrix[ship[0]][ship[1]] not in ('R', 'P'):
#                 matrix[ship[0]][ship[1]] = '.'
#             planet_reached = True
#
#         if planet_reached:
#             break
#
#         if fuel == 0:
#             if matrix[ship[0]][ship[1]] not in ('R', 'P'):
#                 matrix[ship[0]][ship[1]] = '.'
#
#             if matrix[new_r][new_c] not in ('R', 'P'):
#                 matrix[new_r][new_c] = 'S'
#             is_stranded = True
#             break
#
#         if matrix[ship[0]][ship[1]] not in ('R', 'P'):
#             matrix[ship[0]][ship[1]] = '.'
#
#         if matrix[new_r][new_c] not in ('R', 'P'):
#             matrix[new_r][new_c] = 'S'
#
#         ship = [new_r, new_c]
#     else:
#         is_lost = True
#         break
#
# if planet_reached and fuel >= 0:
#     print(f'Mission accomplished! The spaceship reached Planet B with {fuel} resources left.')
# elif fuel < 0 or is_stranded:
#     print('Mission failed! The spaceship was stranded in space.')
# elif is_lost:
#     print('Mission failed! The spaceship was lost in space.')
#
# for row in matrix:
#     print(*row)

size = int(input())
matrix = []
ship = []
resources = 100
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for r in range(size):
    matrix.append(input().split())
    for c in range(size):
        if matrix[r][c] == 'S':
            ship = [r, c]
            matrix[r][c] = '.'

while True:
    if resources < 5:
        print('Mission failed! The spaceship was stranded in space.')
        break

    command = input()
    resources -= 5
    move = directions[command]
    new_r = ship[0] + move[0]
    new_c = ship[1] + move[1]
    if 0 <= new_r < size and 0 <= new_c < size:
        ship = [new_r, new_c]
        if matrix[new_r][new_c] == 'M':
            resources -= 5
            matrix[new_r][new_c] = '.'
        elif matrix[new_r][new_c] == 'R':
            resources = min(100, resources + 10)
        elif matrix[new_r][new_c] == 'P':
            print(f'Mission accomplished! The spaceship reached Planet B with {resources} resources left.')
            break
    else:
        print('Mission failed! The spaceship was lost in space.')
        break

if matrix[ship[0]][ship[1]] not in "RP":
    matrix[ship[0]][ship[1]] = 'S'

for row in matrix:
    print(*row)
