from collections import deque


def next_second(h,m,s):
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
    return h,m,s


robots_input = input().split(';')

robots_info = {}
available_robots = deque()
waiting_robots = deque()

for robot in robots_input:
    name,time_to_process = robot.split('-')
    robots_info[name] = int(time_to_process)
    available_robots.append(name)

hour,minutes,seconds = [int(num) for num in input().split(':')]
element = input()
elements = deque()

while not element == 'End':
    elements.append(element)
    element = input()

while elements:
    hour,minutes,seconds = next_second(hour,minutes,seconds)
    if waiting_robots:
        for ind in range(len(waiting_robots)):
            waiting_robots[ind][1] -= 1
            if waiting_robots[ind][1] <= 0:
                available_robots.append(waiting_robots[ind][0])
        waiting_robots = [robot for robot in waiting_robots if robot[1] > 0]

    if available_robots:
        current_robot_to_work = available_robots.popleft()
        print(f'{current_robot_to_work} - {elements.popleft()} [{hour:02d}:{minutes:02d}:{seconds:02d}]')
        waiting_robots.append([current_robot_to_work,robots_info[current_robot_to_work]])

    else:
        elements.append(elements.popleft())

