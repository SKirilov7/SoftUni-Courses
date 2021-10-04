from collections import deque

chocolates = deque([int(num) for num in input().split(', ')])
milk = deque([int(num) for num in input().split(', ')])

milkshakes = 0
while chocolates and milk and milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_milk = milk.popleft()

    if current_milk <= 0 and current_chocolate <= 0:
        continue
    if current_chocolate <= 0:
        milk.appendleft(current_milk)
        continue
    if current_milk <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        milkshakes += 1
    else:
        milk.append(current_milk)
        chocolates.append(current_chocolate-5)


if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')

print(*[f'Chocolate: {", ".join([str(num) for num in chocolates])}' if chocolates else 'Chocolate: empty'])
print(*[f'Milk: {", ".join([str(num) for num in milk])}' if milk else 'Milk: empty' ])
