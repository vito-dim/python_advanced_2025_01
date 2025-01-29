# total_clothes = [int(element) for element in input().split()]
# rack_capacity = int(input())
#
# racks_used = 0
#
# while total_clothes:
#     racks_used += 1
#     current_capacity = 0
#     while total_clothes:
#         if current_capacity < rack_capacity:
#             if current_capacity + total_clothes[-1] == rack_capacity:
#                 current_capacity += total_clothes.pop()
#             elif current_capacity + total_clothes[-1] > rack_capacity:
#                 break
#             else:
#                 current_capacity += total_clothes.pop()
#         else:
#             break
#
# print(racks_used)


total_clothes = [int(el) for el in input().split()]
rack_capacity = int(input())

racks_used = 0

while total_clothes:
    racks_used += 1
    current_capacity = rack_capacity

    while total_clothes and total_clothes[-1] <= current_capacity:
        current_capacity -= total_clothes.pop()

print(racks_used)
