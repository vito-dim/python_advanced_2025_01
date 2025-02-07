# def grocery_store(**kwargs):
#     receipt = []
#     for product_name, quantity in sorted(kwargs.items(), key=lambda kvp: (-kvp[-1], -len(kvp[0]), kvp[0])):
#         receipt.append(f'{product_name}: {quantity}')
#     return '\n'.join(receipt)


# def grocery_store(**kwargs):
#     receipt = sorted(kwargs.items(), key=lambda  kvp: (-kvp[-1], -len(kvp[0]), kvp[0]))
#     result = []
#     for name, quantity in receipt:
#         result.append(f'{name}: {quantity}')
#     return '\n'.join(result)


def grocery_store(**kwargs):
    receipt = sorted(kwargs.items(), key=lambda  kvp: (-kvp[-1], -len(kvp[0]), kvp[0]))
    return '\n'.join(f'{name}: {quantity}' for name, quantity in receipt)

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))