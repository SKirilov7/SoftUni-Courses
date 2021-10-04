from collections import deque

operator_mapper = {
    '+': lambda a, b: a + b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b,
    '-': lambda a, b: a - b
}

working_bees = deque(map(int,input().split()))
nectar = deque(map(int,input().split()))
sequence_symbols = deque(map(str,input().split()))

nectar_made = 0
while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee and not current_nectar == 0:
        operator = sequence_symbols.popleft()
        nectar_made += abs(operator_mapper[operator](current_bee,current_nectar))
        # or because in the auto system Judge in SoftUni it's safe to use Eval, we can remove the mapper and
        # just use - nectar_made += eval(f'{current_bee} {operator} {current_nectar}'
    elif current_nectar < current_bee:
        working_bees.appendleft(current_bee)

print(f'Total honey made: {nectar_made}')

if working_bees:
    print(f'Bees left: {", ".join([str(num) for num in working_bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(num) for num in nectar])}')