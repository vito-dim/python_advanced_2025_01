def accommodate(*args, **kwargs):
    available_rooms = dict(sorted(kwargs.items(), key=lambda kvp: (kvp[1], kvp[0])))
    result = []
    hotel = {
        "accommodated": {},
        "unaccommodated": {}
    }

    for guests in args:
        for room, space in available_rooms.items():
            if space >= guests:
                hotel['accommodated'][room] = guests
                del available_rooms[room]
                break
        else:
            hotel['unaccommodated'][room] = space

    if hotel['accommodated']:
        result.append(f'A total of {len(hotel["accommodated"])} accommodations were completed!')

        for curr_room, curr_guests in sorted(hotel['accommodated'].items(), key=lambda kvp: kvp[0]):
            curr_room = curr_room.replace('room_', '')
            result.append(f'<Room {curr_room} accommodates {curr_guests} guests>')
    else:
        result.append('No accommodations were completed!')

    if hotel['unaccommodated']:
        result.append(f'Guests with no accommodation: {sum(args) - sum(hotel["accommodated"].values())}')
    if available_rooms:
        result.append(f'Empty rooms: {len(available_rooms)}')

    return "\n".join(result)


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
