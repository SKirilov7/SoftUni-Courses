status_of_the_pirate_ship = [int(num) for num in input().split('>')]
status_of_the_warship = [int(num) for num in input().split('>')]
maximum_health_of_section = int(input())
command_data = input()
lost_or_won = False
while not command_data == 'Retire':
    current_command = command_data.split()
    command = current_command[0]
    if command == 'Fire':
        index_attack = int(current_command[1])
        damage = int(current_command[2])
        if 0 <= index_attack < len(status_of_the_warship):
            status_of_the_warship[index_attack] -= damage
            if status_of_the_warship[index_attack] <= 0:
                print(f"You won! The enemy ship has sunken.")
                lost_or_won = True
                break
    elif command == 'Defend':
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        damage = int(current_command[3])
        if 0 <= start_index <= end_index < len(status_of_the_pirate_ship):
            for dmg in range(start_index, end_index+1):
                status_of_the_pirate_ship[dmg] -= damage
                if status_of_the_pirate_ship[dmg] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    lost_or_won = True
                    break
    elif command == 'Repair':
        index = int(current_command[1])
        health = int(current_command[2])
        if 0 <= index < len(status_of_the_pirate_ship):
            if health + status_of_the_pirate_ship[index] > maximum_health_of_section:
                status_of_the_pirate_ship[index] = maximum_health_of_section
            else:
                status_of_the_pirate_ship[index] += health
    elif command == 'Status':
        count_sectors_for_repair = 0
        for sector in status_of_the_pirate_ship:
            if sector < (0.20 * maximum_health_of_section):
                count_sectors_for_repair += 1
        print(f"{count_sectors_for_repair} sections need repair.")
    command_data = input()

if not lost_or_won:
    print(f"Pirate ship status: {sum(status_of_the_pirate_ship)}")
    print(f"Warship status: {sum(status_of_the_warship)}")