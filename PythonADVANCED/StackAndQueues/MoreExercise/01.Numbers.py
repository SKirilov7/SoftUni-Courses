first_line = set(map(int,input().split()))
second_line = set(map(int,input().split()))
n = int(input())

for _ in range(n):
    full_command = input().split()
    command_name = full_command[0]
    command_parameter = full_command[1]
    if command_name == 'Add' and command_parameter == 'First':
        [first_line.add(int(num)) for num in full_command[2:]]
    elif command_name == 'Add' and command_parameter == 'Second':
        [second_line.add(int(num)) for num in full_command[2:]]
    elif command_name == 'Remove' and command_parameter == 'First':
        [first_line.remove(int(num)) for num in full_command[2:] if int(num) in first_line]
    elif command_name == 'Remove' and command_parameter == 'Second':
        [second_line.remove(int(num)) for num in full_command[2:] if int(num) in second_line]
    else:
        print(first_line.issubset(second_line) or second_line.issubset(first_line))

print(', '.join([str(num) for num in sorted(first_line)]))
print(', '.join([str(num) for num in sorted(second_line)]))