# from collections import deque
#
# materials = [int(num) for num in input().split()]
# magic = deque([int(num) for num in input().split()])
#
# magic_to_present = {
#     150: 'Doll',
#     250: 'Wooden train',
#     300: 'Teddy bear',
#     400: 'Bicycle'
# }
#
# created_presents = {}
#
# while materials and magic:
#     craft_result = materials[-1] * magic[0]
#
#     if craft_result in magic_to_present:
#         present_crafted = magic_to_present[craft_result]
#         if present_crafted not in created_presents:
#             created_presents[present_crafted] = 0
#         created_presents[present_crafted] += 1
#         magic.popleft()
#         materials.pop()
#     else:
#         if craft_result < 0:
#             values_sum = materials.pop() + magic.popleft()
#             materials.append(values_sum)
#         elif craft_result not in magic_to_present and craft_result > 0:
#             magic.popleft()
#             materials[-1] += 15
#         elif magic[0] == 0 or materials[-1] == 0:
#             if magic[0] == 0:
#                 magic.popleft()
#             if materials[-1] == 0:
#                 materials.pop()
#
# if ('Doll' in created_presents and 'Wooden train' in created_presents) or \
#         ('Teddy bear' in created_presents and 'Bicycle' in created_presents):
#     print('The presents are crafted! Merry Christmas!')
# else:
#     print('No presents this Christmas!')
#
# if materials:
#     print(f'Materials left: {", ".join(str(num) for num in materials[::-1])}')  # reversed(materials)
#
# if magic:
#     print(f'Magic left: {", ".join(str(num) for num in magic)}')
#
# for present, quantity in sorted(created_presents.items()):
#     print(f'{present}: {quantity}')

from collections import deque

materials = [int(num) for num in input().split()]
magic = deque([int(num) for num in input().split()])

magic_to_present = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

created_presents = {}

while materials and magic:
    craft_result = materials[-1] * magic[0]

    if craft_result in magic_to_present:
        present_crafted = magic_to_present[craft_result]
        if present_crafted not in created_presents:
            created_presents[present_crafted] = 0
        created_presents[present_crafted] += 1
        magic.popleft()
        materials.pop()
    elif craft_result < 0:
        values_sum = materials.pop() + magic.popleft()
        materials.append(values_sum)
    elif craft_result not in magic_to_present and craft_result > 0:
        magic.popleft()
        materials[-1] += 15
    elif magic[0] == 0 or materials[-1] == 0:
        if magic[0] == 0:
            magic.popleft()
        if materials[-1] == 0:
            materials.pop()

if ('Doll' in created_presents and 'Wooden train' in created_presents) or \
        ('Teddy bear' in created_presents and 'Bicycle' in created_presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(str(num) for num in materials[::-1])}')  # reversed(materials)

if magic:
    print(f'Magic left: {", ".join(str(num) for num in magic)}')

for present, quantity in sorted(created_presents.items()):
    print(f'{present}: {quantity}')
