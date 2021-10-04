from collections import deque

cups = deque(map(int,input().split()))
bottles = deque(map(int,input().split()))

waters_liters_wasted = 0
number_bottles = 0

while cups and bottles:
    first_cup = cups.popleft()
    first_bottle = bottles.pop()
    first_cup -= first_bottle
    if first_cup < 0:
        waters_liters_wasted += abs(first_cup)
    elif first_cup > 0:
        cups.appendleft(first_cup)
    number_bottles += 1

if cups:
    print(f"Cups: {' '.join([str(cup) for cup in cups])}")
elif bottles:
    print(f"Bottles: {' '.join([str(bottle) for bottle in bottles])}")\

print(f"Wasted litters of water: {waters_liters_wasted}")



