sequence_of_elements = [num for num in input().split()]

command_data = input()
number_of_moves = 0
while not command_data == 'end':
    first_index,second_index = command_data.split()
    first_index = int(first_index)
    second_index = int(second_index)
    number_of_moves += 1
    if (first_index == second_index) or (first_index >= len(sequence_of_elements) or second_index >= len(sequence_of_elements))\
        or (first_index < 0 or second_index < 0):
        number_needed_to_append = '-' + str(number_of_moves) + 'a'
        index_for_appending = len(sequence_of_elements) // 2
        sequence_of_elements.insert(index_for_appending, number_needed_to_append)
        sequence_of_elements.insert(index_for_appending, number_needed_to_append)
        print(f"Invalid input! Adding additional elements to the board")
        command_data = input()
        continue

    if sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
        word = sequence_of_elements[first_index]
        sequence_of_elements.remove(word)
        sequence_of_elements.remove(word)
    elif not sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        print("Try again!")
    if len(sequence_of_elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        break
    command_data = input()
if len(sequence_of_elements) > 0:
    print(f"Sorry you lose :(")
    print(f"{' '.join(sequence_of_elements)}")
