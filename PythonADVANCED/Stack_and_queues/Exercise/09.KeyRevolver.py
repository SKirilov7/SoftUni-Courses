from collections import deque

price_of_one_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = deque(map(int,input().split()))
locks = deque(map(int,input().split()))
value_of_intelligence = int(input())

current_gun_barrel = size_of_gun_barrel

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    current_gun_barrel -= 1
    value_of_intelligence -= price_of_one_bullet

    if current_bullet <= current_lock:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')

    if current_gun_barrel == 0 and bullets:
        print('Reloading!')
        current_gun_barrel = size_of_gun_barrel

if not locks:
    print(f'{len(bullets)} bullets left. Earned ${value_of_intelligence}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")



