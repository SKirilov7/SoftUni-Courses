def list_manipulator(numbers, command, beginning_or_end, *args):
    if command == 'add' and beginning_or_end == 'beginning':
        numbers = list(args) + numbers
    elif command == 'add' and beginning_or_end == 'end':
        [numbers.append(num) for num in args]
    elif command == 'remove' and beginning_or_end == 'beginning' and args:
        numbers = numbers[0 + args[0]:]
    elif command == 'remove' and beginning_or_end == 'beginning' and not args:
        numbers = numbers[1:]
    elif command == 'remove' and beginning_or_end == 'end' and args:
        numbers = numbers[:len(numbers) - args[0]]
    elif command == 'remove' and beginning_or_end == 'end' and not args:
        numbers.pop()

    return numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))