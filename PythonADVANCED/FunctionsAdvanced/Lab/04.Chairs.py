def chairs_combination(people, count, comb=[]):
    if count == len(comb):
        print(', '.join(comb))
        return

    for index in range(len(people)):
        comb.append(people[index])
        chairs_combination(people[index+1:], count, comb)
        comb.pop()


names = input().split(', ')
count = int(input())
chairs_combination(names,count)