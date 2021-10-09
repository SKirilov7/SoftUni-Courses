from collections import deque

bombs_effects = deque(map(int, input().split(', ')))
bombs_casing = deque(map(int, input().split(', ')))

datura_bombs, cherry_bombs, smoke_decoy_bombs = 0, 0, 0
is_enough_bombs = False
while bombs_effects and bombs_casing:
    current_bomb_effect = bombs_effects.popleft()
    current_bomb_casing = bombs_casing.pop()
    result = current_bomb_casing + current_bomb_effect

    if result == 120:
        smoke_decoy_bombs += 1
    elif result == 60:
        cherry_bombs += 1
    elif result == 40:
        datura_bombs += 1
    else:
        bombs_casing.append(current_bomb_casing - 5)
        bombs_effects.appendleft(current_bomb_effect)

    if smoke_decoy_bombs >= 3 and cherry_bombs >= 3 and datura_bombs >= 3:
        is_enough_bombs = True
        break

if is_enough_bombs:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join(str(bomb) for bomb in bombs_effects)}") if bombs_effects else print("Bomb Effects: empty")
print(f"Bomb Casings: {', '.join(str(bomb) for bomb in bombs_casing)}") if bombs_casing else print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")