def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    print(sorted_data)
    result = ''
    for cheese, quantity in sorted_data:
        result += cheese + '\n'
        # reversed(sorted(quantity))
        for count in sorted(quantity, reverse=True):
            result += f'{count}\n'
    return result[:-1]

# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)