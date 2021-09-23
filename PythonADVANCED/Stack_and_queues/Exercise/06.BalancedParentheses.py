from collections import deque

sequence = list(input())
stack = deque()
is_balanced = True

for element in sequence:
    if element in '([{':
        stack.append(element)
    else:
        if not stack:
            is_balanced = False
            break
        current_parentheses_duo = f'{stack.pop()}{element}'
        if not current_parentheses_duo in '[]{}()':
            is_balanced = False
            break
if is_balanced:
    print('YES')
else:
    print('NO')
