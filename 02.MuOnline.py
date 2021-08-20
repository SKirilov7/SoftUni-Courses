initial_health = 100
initial_bitcoins = 0
dungeon_rooms = input().split('|')
rooms_managed = 0
all_monsters_defeated = True
for dungeon in range(len(dungeon_rooms)):
    current_dungeon = dungeon_rooms[dungeon].split()
    command = current_dungeon[0]
    number = int(current_dungeon[1])
    rooms_managed += 1
    if command == 'potion':
        health_gained = number
        if initial_health + health_gained > 100:
            health_gained = 100 - initial_health
        initial_health += health_gained
        print(f"You healed for {health_gained} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == 'chest':
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        current_monster = command
        monster_attack_amount = number
        initial_health -= monster_attack_amount
        if initial_health <= 0:
            print(f"You died! Killed by {current_monster}.")
            print(f"Best room: {rooms_managed}")
            all_monsters_defeated = False
            break
        elif initial_health > 0:
            print(f"You slayed {current_monster}.")
if all_monsters_defeated:
    print(f"You've made it!")
    print(f'Bitcoins: {initial_bitcoins}')
    print(f'Health: {initial_health}')
