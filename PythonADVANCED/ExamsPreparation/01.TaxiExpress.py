from collections import deque

customers = deque(map(int, input().split(', ')))
taxis = deque(map(int, input().split(', ')))

total_time = 0

while customers and taxis:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()

    if not current_taxi >= current_customer:
        customers.appendleft(current_customer)
        continue

    total_time += current_customer


if not customers:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(num) for num in customers)}")


