from collections import deque

jobs = deque(map(int, input().split(', ')))
ordered_jobs = deque(sorted(jobs))
index_searched = int(input())
searched_job = jobs[index_searched]

cycles_needed = 0
while True:
    current_job = ordered_jobs.popleft()
    cycles_needed += current_job
    if current_job == searched_job and current_job not in (list(jobs)[0:index_searched]):
        break
    if current_job == searched_job and current_job not in ordered_jobs:
        break

print(cycles_needed)


