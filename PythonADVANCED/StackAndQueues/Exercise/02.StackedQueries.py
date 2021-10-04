from collections import deque

stack = deque()
number_of_commands = int(input())


for _ in range(number_of_commands):
    current_command_data = input()
    if current_command_data.startswith('1'):
        number_to_append = int(current_command_data.split()[1])
        stack.append(number_to_append)
    elif current_command_data == '2':
        if stack:
            stack.pop()
    elif current_command_data == '3':
        if stack:
            print(max(stack))
    elif current_command_data == '4':
        if stack:
            print(min(stack))


while stack:
    if not len(stack) == 1:
        print(stack.pop(),end = ', ')
    else:
        print(stack.pop())
