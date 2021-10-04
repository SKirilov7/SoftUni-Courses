string = input()
stack = []

for index in range(len(string)):
    if string[index] == '(':
        stack.append(index)
    elif string[index] == ')':
        if stack:
            first_index = stack.pop()
            print(string[first_index:index+1])