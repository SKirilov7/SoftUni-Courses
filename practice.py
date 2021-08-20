def exchange_func(list_of_int, index):
    new_list = []
    if index >= len(list_of_int) or index < 0:
        print("Invalid index")
        new_list = list_of_int
    else:
        first_side = list_of_int[:index+1]
        second_side = list_of_int[index+1:]
        new_list = second_side + first_side
    return new_list

def max_odd_or_even(list_of_int, odd_or_even):
    list_of_odd_or_even_nums = []
    if odd_or_even == 'odd':
        for el in list_of_int:
            if not el % 2 == 0:
                list_of_odd_or_even_nums.append(el)
    elif odd_or_even == 'even':
        for el in list_of_int:
            if el % 2 == 0:
                list_of_odd_or_even_nums.append(el)
    if not list_of_odd_or_even_nums:
        return 'No matches'
    max_number = max(list_of_odd_or_even_nums)
    index_needed = len(list_of_int) - list_of_int[::-1].index(max_number) - 1
    return index_needed

def min_odd_or_even(list_of_int, odd_or_even):
    list_of_odd_or_even_nums = []
    if odd_or_even == 'odd':
        for el in list_of_int:
            if not el % 2 == 0:
                list_of_odd_or_even_nums.append(el)
    elif odd_or_even == 'even':
        for el in list_of_int:
            if el % 2 == 0:
                list_of_odd_or_even_nums.append(el)
    if not list_of_odd_or_even_nums:
        return 'No matches'
    min_number = min(list_of_odd_or_even_nums)
    index_needed = len(list_of_int) - list_of_int[::-1].index(min_number) - 1
    return index_needed

def first_count_odd_or_even(list_of_int, count, odd_or_even):
    list_of_odd_or_even_nums = []
    if count > len(list_of_int):
        return 'Invalid count'
    if odd_or_even == 'odd':
        for el in list_of_int:
            if not el % 2 == 0:
                list_of_odd_or_even_nums.append(el)
    elif odd_or_even == 'even':
        for el in list_of_int:
            if el % 2 == 0:
                list_of_odd_or_even_nums.append(el)
    numbers_needed = []
    if count > len(list_of_odd_or_even_nums):
        numbers_needed = list_of_odd_or_even_nums
    else:
        numbers_needed = list_of_odd_or_even_nums[:count]
    return numbers_needed

def last_nums_odd_or_even(list_of_int, count, odd_or_even):
    list_of_odd_or_even_nums = []
    if count > len(list_of_int):
        return 'Invalid count'
    if odd_or_even == 'odd':
        for el in list_of_int:
            if not el % 2 == 0:
                list_of_odd_or_even_nums.append(el)
    elif odd_or_even == 'even':
        for el in list_of_int:
            if el % 2 == 0:
                list_of_odd_or_even_nums.append(el)
    numbers_needed = []
    if count > len(list_of_odd_or_even_nums):
        numbers_needed = list_of_odd_or_even_nums
    else:
        index = len(list_of_odd_or_even_nums) - count
        numbers_needed = list_of_odd_or_even_nums[index:]
    return numbers_needed


list_of_int = input().split()
nums = [int(x) for x in list_of_int]
command_data = input()

while not command_data == 'end':
    current_command = command_data.split()
    command = current_command[0]
    if command == 'exchange':
        number = int(current_command[1])
        nums = exchange_func(nums, number)
    elif command == 'max':
        odd_or_even = current_command[1]
        print(max_odd_or_even(nums, odd_or_even))
    elif command == 'min':
        odd_or_even = current_command[1]
        print(min_odd_or_even(nums, odd_or_even))
    elif command == 'first':
        count = int(current_command[1])
        odd_or_even = current_command[2]
        print(first_count_odd_or_even(nums, count, odd_or_even))
    elif command == 'last':
        count = int(current_command[1])
        odd_or_even = current_command[2]
        print(last_nums_odd_or_even(nums, count, odd_or_even))

    command_data = input()
print(nums)

