from collections import deque

pizza_orders = deque(map(int, input().split(', ')))
employees_making_capacity = deque(map(int, input().split(', ')))

total_pizzas = 0
while pizza_orders and employees_making_capacity:
    current_order = pizza_orders.popleft()
    if current_order > 10 or current_order <= 0:
        continue

    current_employee_capacity = employees_making_capacity.pop()

    if current_order > current_employee_capacity:
        pizza_orders.appendleft(current_order - current_employee_capacity)

    total_pizzas += current_order if current_order <= current_employee_capacity else current_employee_capacity

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    print(f"Employees: {', '.join([str(employee) for employee in employees_making_capacity])}")
else:
    print(f'Not all orders are completed.')
    print(f"Orders left: {', '.join([str(order) for order in pizza_orders])}")


