# text = input()
# count_dict = dict()
#
# for char in text:
#     if char not in count_dict.keys():
#         char_count = text.count(char)
#         count_dict[char] = f'{char_count} time/s'
#
# for char in sorted(count_dict):
#     print(f'{char}: {count_dict[char]}')

# text = input()
# unique_symbols = {char for char in text}
#
# for ch in sorted(unique_symbols):
#     print(f'{ch}: {text.count(ch)} time/s')

text = input()
unique_symbols = sorted(set(text))

for ch in unique_symbols:
    print(f'{ch}: {text.count(ch)} time/s')
