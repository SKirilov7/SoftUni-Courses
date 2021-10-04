from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
command = input()

number_cars = 0
all_passed_successfully = True
current_car_full_name = None

while not command == 'END':
    current_green_timer = green_light
    current_free_window = free_window
    if not command == 'green':
        cars.append(list(command))
    else:
        if cars:
            current_car = deque(cars.popleft())
            current_car_full_name = ''.join(current_car)
            while current_green_timer > 0 and current_car:
                current_green_timer -= 1
                current_car.popleft()
                if not current_car and current_green_timer > 0 and cars:
                    current_car = deque(cars.popleft())
                    current_car_full_name = ''.join(current_car)
                    number_cars += 1

            if current_car and current_free_window > 0:
                while current_free_window and current_car:
                    current_car.popleft()
                    current_free_window -= 1
            if current_car:
                all_passed_successfully = False
                print(f'A crash happened!')
                print(f'{current_car_full_name} was hit at {current_car[0]}.')
                break
            number_cars += 1
    command = input()

if all_passed_successfully:
    print(f'Everyone is safe.')
    print(f'{number_cars} total cars passed the crossroads.')
