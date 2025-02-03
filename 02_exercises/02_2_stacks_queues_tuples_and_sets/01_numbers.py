# def gen_num_seq(cmd_name: str, cmd: str) -> set:
#     _, nums = cmd.split(cmd_name)
#     num_seq = [int(el) for el in nums.split() if el != ' ']
#     return set(num_seq)
#
#
# first_seq = {int(num) for num in input().split()}
# second_seq = {int(num) for num in input().split()}
# cmd_count = int(input())
#
# for _ in range(cmd_count):
#     current_command = input()
#     if 'Add First' in current_command:
#         num_sequence = gen_num_seq('Add First', current_command)
#         first_seq = first_seq.union(num_sequence)
#     elif 'Add Second' in current_command:
#         num_sequence = gen_num_seq('Add Second', current_command)
#         second_seq = second_seq.union(num_sequence)
#     elif 'Remove First' in current_command:
#         num_sequence = gen_num_seq('Remove First', current_command)
#         first_seq = first_seq.difference(num_sequence)
#     elif 'Remove Second' in current_command:
#         num_sequence = gen_num_seq('Remove Second', current_command)
#         second_seq = second_seq.difference(num_sequence)
#     elif 'Check Subset' in current_command:
#         if first_seq <= second_seq or first_seq >= second_seq:  # set1.issubset(set2) or set1.issuperset(set2)
#             print('True')
#         else:
#             print('False')
#
# print(*sorted(first_seq), sep=', ')
# print(*sorted(second_seq), sep=', ')


first_sequence = set([int(num) for num in input().split()])
second_sequence = set([int(num) for num in input().split()])
cmd_count = int(input())

for _ in range(cmd_count):
    command_details = input().split()
    command_name = command_details[0] + ' ' + command_details[1]
    numbers = [int(num) for num in command_details[2:]]
    if command_name == 'Add First':
        first_sequence.update(numbers)
    elif command_name == 'Add Second':
        second_sequence.update(numbers)
    elif command_name == 'Remove First':
        first_sequence.difference_update(numbers)
    elif command_name == 'Remove Second':
        second_sequence.difference_update(numbers)
    elif command_name == 'Check Subset':
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
