initial_list = input().split('!')
command = input()
while not command == 'Go Shopping':
    if command == 'Go Shopping!':
        break
    command = command.split()
    current_command = command[0]
    if current_command == 'Urgent':
        current_item = command[1]
        if current_item in initial_list:
            command = input()
            continue
        else:
            initial_list.insert(0, current_item)
    elif current_command == 'Unnecessary':
        current_item = command[1]
        if current_item in initial_list:
            initial_list.remove(current_item)
        else:
            command = input()
            continue
    elif current_command == 'Correct':
        old_item = command[1]
        new_item = command[2]
        if old_item in initial_list:
            index_needed = initial_list.index(old_item)
            initial_list.remove(old_item)
            initial_list.insert(index_needed, new_item)
        else:
            command = input()
            continue
    elif current_command == 'Rearrange':
        current_item = command[1]
        item = current_item
        if current_item in initial_list:
            initial_list.remove(current_item)
            initial_list.append(item)
        else:
            command = input()
            continue
    command = input()
print(', '.join(initial_list))
