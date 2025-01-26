# commands_num = int(input())
# parking_lot = set()
#
# for _ in range(commands_num):
#     command, car_plate = input().split(', ')
#
#     if command == 'IN':
#         parking_lot.add(car_plate)
#     elif command == 'OUT':
#         parking_lot.remove(car_plate)
#
# if parking_lot:
#     print(*parking_lot, sep='\n')
# else:
#     print("Parking Lot is Empty")

commands_num = int(input())
parking_lot = set()

for _ in range(commands_num):
    command, car_plate = input().split(', ')

    if command == 'IN':
        parking_lot.add(car_plate)
    elif command == 'OUT':
        if car_plate not in parking_lot:
            continue
        parking_lot.remove(car_plate)

if parking_lot:
    for plate in parking_lot:
        print(plate)
else:
    print("Parking Lot is Empty")
