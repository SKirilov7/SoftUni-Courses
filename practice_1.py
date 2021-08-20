def exchange_func(numbers_list, ind):
    exchanged_list = []
    if ind > len(numbers_list) -1 or ind < 0:
        print('Invalid index')
        return numbers_list
    else:
        first_side = numbers_list[:ind+1]
        second_side = numbers_list[ind+1:]
        exchanged_list = second_side + first_side
        return exchanged_list

def max_number_index(number_list, odd_or_even):
    list_of_odd_or_even = []
    if odd_or_even == 'odd':
        for el in number_list:
            if not el % 2 == 0:
                list_of_odd_or_even.append(el)
    else:
        for el in number_list:
            if el % 2 == 0:
                list_of_odd_or_even.append(el)
    if not list_of_odd_or_even:
        return "No matches"
    max_number = max(list_of_odd_or_even)
    index_number = len(number_list) - number_list[::-1].index(max_number) - 1
    return index_number

def min_number_index(number_list, odd_or_even):
    list_of_odd_or_even = []
    if odd_or_even == 'odd':
        for el in number_list:
            if not el % 2 == 0:
                list_of_odd_or_even.append(el)
    else:
        for el in number_list:
            if el % 2 == 0:
                list_of_odd_or_even.append(el)
    if not list_of_odd_or_even:
        return "No matches"
    min_number = min(list_of_odd_or_even)
    index_number = len(number_list) - number_list[::-1].index(min_number) - 1
    return index_number

def first_count_elements(number_list, count, odd_or_even):
    list_of_odd_or_even = []
    if odd_or_even == 'odd':
        for el in number_list:
            if not el % 2 == 0:
                list_of_odd_or_even.append(el)
    else:
        for el in number_list:
            if el % 2 == 0:
                list_of_odd_or_even.append(el)
    if count > len(number_list):
        return "Invalid count"
    if count > len(list_of_odd_or_even):
        return list_of_odd_or_even
    wanted_list = list_of_odd_or_even[:count]
    return wanted_list

def last_count_even_or_odd_nums(number_list, count, odd_or_even):
    list_of_odd_or_even = []
    if odd_or_even == 'odd':
        for el in number_list:
            if not el % 2 == 0:
                list_of_odd_or_even.append(el)
    else:
        for el in number_list:
            if el % 2 == 0:
                list_of_odd_or_even.append(el)
    if count > len(number_list):
        return "Invalid count"
    if count > len(list_of_odd_or_even):
        return list_of_odd_or_even
    needed_index = len(list_of_odd_or_even) - count
    wanted_list = list_of_odd_or_even[needed_index:]
    return wanted_list


numbers_as_str_list = input().split()
nums = [int(x) for x in numbers_as_str_list]
command_data = input()

while not command_data == 'end':
    command_data = command_data.split()
    current_command = command_data[0]
    if current_command == 'exchange':
        index = int(command_data[1])
        nums = exchange_func(nums, index)
    elif current_command == 'max':
        odd_or_even = command_data[1]
        print(max_number_index(nums, odd_or_even))
    elif current_command == 'min':
        odd_or_even = command_data[1]
        print(min_number_index(nums, odd_or_even))
    elif current_command == 'first':
        count = int(command_data[1])
        odd_or_even = command_data[2]
        print(first_count_elements(nums,count,odd_or_even))
    elif current_command == 'last':
        count = int(command_data[1])
        odd_or_even = command_data[2]
        print(last_count_even_or_odd_nums(nums,count,odd_or_even))

    command_data = input()
print(nums)