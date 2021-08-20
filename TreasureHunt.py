initial_loot = input().split('|')
command_data = input()
while not command_data == "Yohoho!":
    current_command = command_data.split()
    command = current_command[0]
    if command == 'Loot':
        for item in range(1, len(current_command)):
            current_item = current_command[item]
            if not current_item in initial_loot:
                initial_loot.insert(0, current_item)
    elif command == 'Drop':
        index = int(current_command[1])
        if not index >= len(initial_loot):
            item_removed = initial_loot[index]
            initial_loot.pop(index)
            initial_loot.append(item_removed)
    elif command == 'Steal':
        count = int(current_command[1])
        if len(initial_loot) < count:
            print(', '.join(initial_loot))
            initial_loot = []
        else:
            indexes_needed = len(initial_loot) - count
            items_stolen = initial_loot[indexes_needed:]
            del initial_loot[indexes_needed:]
            print(', '.join(items_stolen))

    command_data = input()

total_sum = 0
if initial_loot:
    for item in initial_loot:
        total_sum += len(item)
    average_sum = total_sum / len(initial_loot)
    print(f"Average treasure gain: {average_sum:.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")

