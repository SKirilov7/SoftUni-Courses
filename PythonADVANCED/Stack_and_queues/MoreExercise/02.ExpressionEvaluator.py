from collections import deque

stack = deque()
given_input = input().split()

operation_mapper = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '*': lambda a,b: a * b,
    '/': lambda a,b: a // b
}

for el in given_input:
    try:
        stack.append(int(el))
    except ValueError:
        operator = el
        result = stack.popleft()
        while stack:
            new_number = stack.popleft()
            result = operation_mapper[operator](result,new_number)

        current_number = result
        stack.append(current_number)

print(*stack)
