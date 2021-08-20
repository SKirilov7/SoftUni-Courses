first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
total_people = int(input())
hour_counter = 0
while total_people > 0:
    hour_counter += 1
    total_people -= (first_employee_per_hour + second_employee_per_hour + third_employee_per_hour)
    if hour_counter % 4 == 0:
        hour_counter += 1
print(f"Time needed: {hour_counter}h.")
