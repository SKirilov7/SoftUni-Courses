collecting_items = input().split(', ')
command = input()
list_commands = []
list_commands.append(command)
ind_for_list = 0
is_command_craft = False
while True:
    command_data = list_commands[ind_for_list].split(' - ')
    current_command = command_data[0]
    if current_command == 'Craft!':
        is_command_craft = True
        break
    if current_command == 'Collect':
        current_item = command_data[1]
        if current_item in collecting_items:
            continue
        else:
            collecting_items.append(current_item)
    elif current_command == 'Drop':
        current_item = command_data[1]
        if current_item in collecting_items:
            collecting_items.remove(current_item)
    elif current_command == 'Combine Items':
        list_items = command_data[1]
        string = ''.join(list_items)
        new_list = string.split(':')
        old_item = new_list[0]
        new_item = new_list[1]
        if old_item in collecting_items:
            index_searched = collecting_items.index(old_item)
            collecting_items.insert(index_searched+1, new_item)
    elif current_command == 'Renew':
        current_item = command_data[1]
        if current_item in collecting_items:
            item = current_item
            collecting_items.remove(current_item)
            collecting_items.append(item)
    command = input()
    ind_for_list += 1
    list_commands.append(command)
if is_command_craft:

    print(', '.join(collecting_items))

