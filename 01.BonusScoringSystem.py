import math
count_of_students = int(input())
count_of_lectures = int(input())
initial_bonus = int(input())
max_attendaces = 0
max_bonus_points = 0

for student in range(count_of_students):
    current_student_attendaces = int(input())

    current_student_bonus = current_student_attendaces / count_of_lectures * (5 + initial_bonus)
    if current_student_bonus > max_bonus_points:
        max_bonus_points = current_student_bonus
    if current_student_attendaces > max_attendaces:
        max_attendaces = current_student_attendaces

print(f"Max Bonus: {math.ceil(max_bonus_points)}.")
print(f"The student has attended {max_attendaces} lectures.")
