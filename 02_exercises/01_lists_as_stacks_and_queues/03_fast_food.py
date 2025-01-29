# from collections import deque
#
# food_quantity = int(input())
# food_per_order = deque([int(element) for element in input().split()])
# biggest_order = max(food_per_order)
#
# for _ in range(len(food_per_order)):
#     if food_per_order[0] <= food_quantity:
#         current_order = food_per_order.popleft()
#         food_quantity -= current_order
#     else:
#         break
#
# print(biggest_order)
#
# if food_per_order:
#     print(f'Orders left:', *food_per_order, end=' ')
# else:
#     print('Orders complete')


from collections import deque

food_quantity = int(input())
orders = deque(int(order) for order in input().split())
print(max(orders))

while orders and food_quantity >= orders[0]:
    food_quantity -= orders.popleft()

if orders:
    print('Orders left:', *orders)
else:
    print('Orders complete')
