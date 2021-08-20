sequence_of_numbers_as_str = input().split()
sequence_of_numbers = [int(x) for x in sequence_of_numbers_as_str]

sum_of_numbers = sum(sequence_of_numbers)
average_num = sum_of_numbers / len(sequence_of_numbers)
list_greater_than_average = []
for number in sequence_of_numbers:
    if number > average_num:
        list_greater_than_average.append(number)
list_sorted = sorted(list_greater_than_average,reverse= True)
numbers_needed = list_sorted[:5]
for el in range(len(numbers_needed)):
    numbers_needed[el] = str(numbers_needed[el])
if not numbers_needed:
    print('No')
else:
    print(' '.join(numbers_needed))