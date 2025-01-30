# intersect_count = int(input())
# longest_intersection = []
#
# for _ in range(intersect_count):
#     first_intersect, second_intersect = input().split('-')
#
#     first_start, first_end = [int(num) for num in first_intersect.split(',')]
#     second_start, second_end = [int(num) for num in second_intersect.split(',')]
#
#     first_range = {num for num in range(first_start, first_end + 1)}
#     second_range = {num for num in range(second_start, second_end + 1)}
#
#     current_intersection = first_range.intersection(second_range)
#
#     if len(current_intersection) > len(longest_intersection):
#         longest_intersection = list(current_intersection)
#
# print(f'Longest intersection is {longest_intersection} with length {len(longest_intersection)}')

# def calc_range(range_data: str) -> set:
#     range_start, range_end = [int(num) for num in range_data.split(',')]
#     calculated_range = {num for num in range(range_start, range_end + 1)}
#     return calculated_range
#
#
# ranges_count = int(input())
# longest_intersection = set()
#
# for _ in range(ranges_count):
#     first_range_data, second_range_data = input().split('-')
#     first_range = calc_range(first_range_data)
#     second_range = calc_range(second_range_data)
#     current_intersection = first_range & second_range
#
#     if len(current_intersection) > len(longest_intersection):
#         longest_intersection = current_intersection
#
# print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')

def calc_range(range_data: str) -> set:
    range_start, range_end = range_data.split(',')
    calculated_range = set(range(int(range_start), int(range_end) + 1))
    return calculated_range


ranges_count = int(input())
longest_intersection = set()

for _ in range(ranges_count):
    first_range_data, second_range_data = input().split('-')
    first_range = calc_range(first_range_data)
    second_range = calc_range(second_range_data)
    current_intersection = first_range & second_range

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection
    # longest_intersection = current_intersection if len(current_intersection) > len(longest_intersection) else longest_intersection

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')
