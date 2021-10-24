class Stack:
    def __init__(self):
        self.data = []

    def push(self,element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        return '[' + ', '.join(reversed(self.data)) + ']'


stack = Stack()

stack.push('1')
print(stack.pop())
stack.push('2')
stack.push('3')
print(stack.top())
print(stack.is_empty())
print(stack)


