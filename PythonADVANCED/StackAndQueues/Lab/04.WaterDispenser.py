from collections import deque
amount_water = int(input())

queue = deque()
name = input()

while not name == 'Start':
    queue.append(name)
    name = input()

command = input()

while not command == 'End':
    if command.startswith('refill'):
        amount_to_refill = int(command.split()[1])
        amount_water += amount_to_refill
    else:
        water_wanted = int(command)
        name = queue.popleft()
        if water_wanted > amount_water:
            print(f"{name} must wait")
        else:
            amount_water -= water_wanted
            print(f"{name} got water" )

    command = input()

print(f"{amount_water} liters left")