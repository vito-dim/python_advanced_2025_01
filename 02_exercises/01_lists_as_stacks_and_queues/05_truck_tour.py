from collections import deque

pumps_count = int(input())
pumps = deque()

start_position = 0
stops = 0

for _ in range(pumps_count):
    petrol, distance = input().split()
    pumps.append([int(petrol), int(distance)])

while stops < pumps_count:
    current_fuel = 0
    for index in range(pumps_count):
        current_fuel += pumps[index][0]
        distance = pumps[index][1]
        if current_fuel < distance:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        current_fuel -= distance
        stops += 1

print(start_position)
