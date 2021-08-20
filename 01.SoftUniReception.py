first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
student_count = int(input())
hours_needed = 0
while student_count > 0:
    hours_needed += 1
    student_count -= (first_employee_per_hour + second_employee_per_hour + third_employee_per_hour)
    if hours_needed % 4 == 0:
        hours_needed += 1
print(f"Time needed: {hours_needed}h.")