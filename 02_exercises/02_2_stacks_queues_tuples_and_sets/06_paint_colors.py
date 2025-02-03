from collections import deque

data = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["blue", "yellow"]
}

collected_colors = []

while data:
    first_str = data.popleft()
    last_str = data.pop() if data else ""
    if (first_str + last_str) in main_colors or (first_str + last_str) in secondary_colors:
        collected_colors.append(first_str + last_str)
    elif (last_str + first_str) in main_colors or (last_str + first_str) in secondary_colors:
        collected_colors.append(last_str + first_str)
    else:
        if len(first_str) > 1:
            string_middle = len(data) // 2
            data.insert(string_middle, first_str[:-1])
        if len(last_str) > 1:
            string_middle = len(data) // 2
            data.insert(string_middle, last_str[:-1])

for color in collected_colors:
    if color in secondary_colors:
        for c in secondary_colors[color]:
            if c not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)
