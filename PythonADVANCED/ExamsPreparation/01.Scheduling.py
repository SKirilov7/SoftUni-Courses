from collections import deque

jobs = deque(map(int, input().split(', ')))
ordered_jobs = deque(sorted([(number, index)for index, number in enumerate(jobs)]))
index_searched = int(input())
cycles_needed = 0

for number, index in ordered_jobs:
    cycles_needed += number
    if index == index_searched:
        break

print(cycles_needed)



