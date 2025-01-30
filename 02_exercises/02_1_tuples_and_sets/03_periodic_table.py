# num_elements = int(input())
# unique_elements = set()
#
# for _ in range(num_elements):
#     chem_compounds = input().split()
#     for el in chem_compounds:
#         unique_elements.add(el)
#
# print(*unique_elements, sep='\n')
from importlib.util import set_package

num_elements = int(input())
unique_elements = set()

for _ in range(num_elements):
    chem_compounds = input().split()
    unique_elements = unique_elements.union(chem_compounds)
    # unique_elements = unique_elements | set(chem_compounds)

print(*unique_elements, sep='\n')

# print(*{el for _ in range(int(input())) for el in input().split()}, sep='\n')