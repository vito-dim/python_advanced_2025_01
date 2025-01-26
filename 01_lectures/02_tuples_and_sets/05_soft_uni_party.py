# total_guests = int(input())
# guest_reservations = set()
#
# for _ in range(total_guests):
#     reservation_code = input()
#     if len(reservation_code) == 8:
#         guest_reservations.add(reservation_code)
#
# guest = input()
# while guest != 'END':
#     if guest in guest_reservations:
#         guest_reservations.remove(guest)
#     guest = input()
#
# sorted_reservations = sorted(reservation for reservation in guest_reservations)
# print(len(sorted_reservations))
# for reservation in sorted_reservations:
#     print(reservation)


total_guests = int(input())
guest_reservations = set()

for _ in range(total_guests):
    reservation_code = input()
    if len(reservation_code) == 8:
        guest_reservations.add(reservation_code)

guest = input()
while guest != 'END':
    if guest in guest_reservations:
        guest_reservations.remove(guest)
    guest = input()

print(len(guest_reservations))
for reservation in sorted(guest_reservations):
    print(reservation)