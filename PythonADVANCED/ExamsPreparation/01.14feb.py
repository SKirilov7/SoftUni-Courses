from collections import deque

firework_effects = deque([int(num) for num in input().split(', ') if int(num) > 0])
explosive_power = deque([int(num) for num in input().split(', ') if int(num) > 0])

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

enough_fireworks = False
while firework_effects and explosive_power:
    current_explosive_power = explosive_power.pop()
    current_firework_effect = firework_effects.popleft()

    result = current_firework_effect + current_explosive_power

    if result % 3 == 0 and result % 5 == 0:
        crossette_fireworks += 1
    elif result % 3 == 0:
        palm_fireworks += 1
    elif result % 5 == 0:
        willow_fireworks += 1
    else:
        explosive_power.append(current_explosive_power)
        if current_firework_effect - 1 > 0:
            firework_effects.append(current_firework_effect - 1)

    if crossette_fireworks >= 3 and palm_fireworks >= 3 \
            and willow_fireworks >= 3:
        enough_fireworks = True
        break

print(f"Congrats! You made the perfect firework show!") if enough_fireworks else print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(num) for num in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(num) for num in explosive_power)}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")


