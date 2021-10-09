from collections import deque


def best_list_pureness(*args):
    numbers, k = deque(*args[:-1]), args[-1]
    best_result, best_rotation, rotation = 0, 0, 0

    while rotation <= k:
        sum = 0
        for index, number in enumerate(numbers):
            sum += index * number
        if sum > best_result:
            best_result = sum
            best_rotation = rotation
        last_num = numbers.pop()
        numbers.appendleft(last_num)
        rotation += 1

    return f"Best pureness {best_result} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)