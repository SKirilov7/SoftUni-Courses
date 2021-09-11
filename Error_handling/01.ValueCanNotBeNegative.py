from Custom_errors import ValueCannotBeNegative

number_of_inputs = 5
list_of_nums = []

for _ in range(number_of_inputs):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative
    list_of_nums.append(number)


print(*list_of_nums)