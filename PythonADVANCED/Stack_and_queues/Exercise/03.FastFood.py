from collections import deque

food = int(input())
customers = deque(list(map(int,input().split())))

print(max(customers))

while food > 0 and len(customers) > 0:
    first_customer = customers[0]
    if first_customer > food:
        break
    food -= customers.popleft()

if not customers:
    print('Orders complete')
else:
    print(f"Orders left: {' '.join([str(num) for num in customers])}")
