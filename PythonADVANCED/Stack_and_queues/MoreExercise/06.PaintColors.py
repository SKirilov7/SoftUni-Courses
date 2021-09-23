from collections import deque


def is_combination_color_formed(comb,main_col,secondary_col):
    if comb in main_col or comb in secondary_col:
        return True
    return False


def is_secondary_comb_color_formed(second_comb,main_col,secondary_col):
    if second_comb in main_col or second_comb in secondary_col:
        return True
    return False


main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

secondary_colors_requirement = {
    "orange": ["red","yellow"],
    "purple": ["red","blue"],
    "green": ["blue","yellow"]
}

strings = deque(map(str,input().split()))
colors_found = []

while strings:
    if len(strings) > 1:
        first_part = strings.popleft()
        last_part = strings.pop()

        combination = first_part + last_part
        second_combination = last_part + first_part

        if is_combination_color_formed(combination,main_colors,secondary_colors):
            colors_found.append(combination)
        elif is_secondary_comb_color_formed(second_combination,main_colors,secondary_colors):
            colors_found.append(second_combination)
        else:
            first_part = first_part[:-1]
            last_part = last_part[:-1]
            half_index = len(strings) // 2
            if last_part:
                strings.insert(half_index,last_part)
            if first_part:
                strings.insert(half_index,first_part)

    else:
        last_string = strings.pop()
        if last_string in main_colors or last_string in secondary_colors:
            colors_found.append(last_string)

for color in colors_found:
    if color in secondary_colors:
        is_all_requirements_fullfield = True
        for color_req in secondary_colors_requirement[color]:
            if not color_req in colors_found:
                is_all_requirements_fullfield = False
        if not is_all_requirements_fullfield:
            colors_found.remove(color)

print(colors_found)


