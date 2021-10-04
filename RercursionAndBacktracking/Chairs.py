def chairs_combinations(people, num_chairs, combination=[]):
    if len(combination) == num_chairs:
        print(', '.join(combination))
        return
    for index in range(len(people)):
        combination.append(people[index])
        chairs_combinations(people[index + 1:], num_chairs, combination)
        combination.pop()


people = input().split(', ')
chairs = int(input())
chairs_combinations(people, chairs)