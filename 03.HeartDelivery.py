string_of_int = input().split('@')
list_of_numbers = []
last_jump = 0
houses_with_valentines_day = 0
for el in string_of_int:
    el = int(el)
    list_of_numbers.append(el)

command = input()
while not command == 'Love!':
    command_depatched = command.split()
    jump_lenght = int(command_depatched[1])
    last_jump += jump_lenght
    if last_jump >= len(string_of_int):
        while last_jump >= len(string_of_int):
            last_jump = 0
    if not list_of_numbers[last_jump] == 0:
        list_of_numbers[last_jump] = list_of_numbers[last_jump] - 2
        if list_of_numbers[last_jump] == 0:
            print(f"Place {last_jump} has Valentine's day.")
            houses_with_valentines_day += 1
    else:
        print(f"Place {last_jump} already had Valentine's day.")
    command = input()
print(f"Cupid's last position was {last_jump}.")
if houses_with_valentines_day == len(list_of_numbers):
    print("Mission was successful.")
else:
    houses_failed = len(list_of_numbers) - houses_with_valentines_day
    print(f"Cupid has failed {houses_failed} places.")




