from collections import deque

children = deque(input().split())
count_tosses = int(input())

while len(children) > 1:
    children.rotate(-count_tosses)
    print(f'Removed {children.pop()}')

print(f"Last is {''.join(children)}")