def plant_garden(space, *allowed_plants, **requested_plants):
    sorted_requests = sorted(requested_plants.items(), key=lambda kvp: kvp[0])
    planted_flowers = []
    result = []
    successful_gardening = True

    for plant, quantity in sorted_requests:
        for p, p_space in allowed_plants:
            if plant == p:
                planted_quantity = min(quantity, int(space // p_space))
                if planted_quantity < quantity:
                    successful_gardening = False
                if planted_quantity > 0:
                    planted_flowers.append((plant, planted_quantity))
                    planted_space = planted_quantity * p_space
                    space -= planted_space
                if space <= 0:
                    break

    if successful_gardening:
        result.append(f'All plants were planted! Available garden space: {space:.1f} sq meters.')
    else:
        result.append('Not enough space to plant all requested plants!')

    if planted_flowers:
        result.append('Planted plants:')
        for p, q in planted_flowers:
            result.append(f'{p}: {q}')

    return '\n'.join(result)


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
