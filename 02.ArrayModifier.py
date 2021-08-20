list_of_int_as_str = input().split()
list_of_int = [int(x) for x in list_of_int_as_str]
command_data = input()

while not command_data == 'end':
    current_command = command_data.split()
    command = current_command[0]
    if command == 'swap':
        index_one = int(current_command[1])
        index_two = int(current_command[2])
        list_of_int[index_one],list_of_int[index_two] = list_of_int[index_two], list_of_int[index_one]
    elif command == 'multiply':
        index_one = int(current_command[1])
        index_two = int(current_command[2])
        list_of_int[index_one] = list_of_int[index_one] *  list_of_int[index_two]
    elif command == 'decrease':
        for el in range(len(list_of_int)):
            list_of_int[el] = list_of_int[el] - 1

    command_data = input()
list_for_print = [str(x) for x in list_of_int]
print(', '.join(list_for_print))

