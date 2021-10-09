from collections import deque

males = deque([int(num) for num in input().split() if int(num) > 0])
females = deque([int(num) for num in input().split() if int(num) > 0])

matching_couples = 0
while males and females:
    current_female = females.popleft()
    current_male = males.pop()

    if current_female % 25 == 0 and females:
        females.popleft()
        males.append(current_male)
    if current_male % 25 == 0 and males:
        males.pop()
        females.appendleft(current_female)
    if current_female % 25 == 0 or current_male % 25 == 0:
        continue

    if current_male == current_female:
        matching_couples += 1
    elif (current_male > current_female or current_male < current_female) and current_male > 2:
        males.append(current_male - 2)

print(f"Matches: {matching_couples}")

print(f"Males left: {', '.join(str(num) for num in reversed(males))}") if males else print("Males left: none")
print(f"Females left: {', '.join(str(num) for num in females)}") if females else print("Females left: none")

