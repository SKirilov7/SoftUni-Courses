string = list(input())
stack = []
while len(string) > 0:
    stack.append(string.pop())
print(''.join(stack))