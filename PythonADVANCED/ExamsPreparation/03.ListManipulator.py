def list_manipulator(numbers, command,beginning_or_end, *args):
    if command == 'add' and beginning_or_end == 'beginning':
        return list(args) + numbers
    if command == 'add' and beginning_or_end == 'end':
        return numbers + list(args)
    if command == 'remove' and beginning_or_end == 'beginning':
        return numbers[args[0]:] if args else numbers[1:]
    return numbers[:-args[0]] if args else numbers[:-1]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))