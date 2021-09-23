from collections import deque

presents_price = {
    150:'Doll',
    250:'Wooden train',
    300:'Teddy bear',
    400:'Bicycle'
}

boxes_materials = deque(map(int,input().split()))
magic_values = deque(map(int,input().split()))
presents_made = {}

while boxes_materials and magic_values:
    current_materials = boxes_materials.pop()
    current_magic_value = magic_values.popleft()
    result = current_materials * current_magic_value

    if result < 0:
        sum_both = current_materials + current_magic_value
        boxes_materials.append(sum_both)
        continue

    if result == 0 and current_magic_value == 0 and current_materials == 0:
        continue
    elif result == 0 and current_magic_value == 0:
        boxes_materials.append(current_materials)
        continue
    elif result == 0 and current_materials == 0:
        magic_values.appendleft(current_magic_value)
        continue

    if result in presents_price:
        current_present = presents_price[result]
        if current_present not in presents_made:
            presents_made[current_present] = 0
        presents_made[current_present] += 1
    else:
        boxes_materials.append(current_materials + 15)


if ('Doll' in presents_made and 'Wooden train' in presents_made) or ('Teddy bear' in presents_made and 'Bicycle' in presents_made):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes_materials:
    print(f'Materials left: {", ".join([str(num) for num in reversed(boxes_materials)])}')
elif magic_values:
    print(f'Magic left: {", ".join([str(num) for num in magic_values])}')

for present,amount in sorted(presents_made.items()):
    print(f'{present}: {amount}')


