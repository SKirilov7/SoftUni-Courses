max_people_in_wagon = 4
people_waiting_to_get_on_lift = int(input())
list_of_wagons = [int(num) for num in input().split()]
empty_spaces = False
no_more_people = False
for wagon in range(len(list_of_wagons)):
    while list_of_wagons[wagon] < max_people_in_wagon:
        list_of_wagons[wagon] += 1
        people_waiting_to_get_on_lift -= 1
        if people_waiting_to_get_on_lift == 0:
            no_more_people = True
            break
    if no_more_people:
        break
for index in range(len(list_of_wagons)):
    if not list_of_wagons[index] == max_people_in_wagon and people_waiting_to_get_on_lift == 0:
        empty_spaces = True
list_of_wagons = [str(num) for num in list_of_wagons]
if empty_spaces:
    print(f"The lift has empty spots!")
    print(' '.join(list_of_wagons))
elif people_waiting_to_get_on_lift > 0:
    print(f"There isn't enough space! {people_waiting_to_get_on_lift} people in a queue!")
    print(' '.join(list_of_wagons))
elif people_waiting_to_get_on_lift == 0 and empty_spaces == False:
    print(' '.join(list_of_wagons))