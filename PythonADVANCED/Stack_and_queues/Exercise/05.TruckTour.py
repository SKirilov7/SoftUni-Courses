from collections import deque

number_pumps = int(input())

pumps = deque()
for _ in range(number_pumps):
    pumps.append([int(num) for num in input().split()])

for index in range(number_pumps):
    is_completed = True
    current_fuel = 0

    for pump in pumps:
        current_fuel += pump[0]
        current_fuel -= pump[1]
        if current_fuel < 0:
            is_completed = False
            break
    if is_completed:
        print(index)
        break
    pumps.append(pumps.popleft())



