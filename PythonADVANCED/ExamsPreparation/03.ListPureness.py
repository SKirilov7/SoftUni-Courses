from collections import deque


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    best_result = 0
    best_rotation = 0
    for rotation in range(k+1):
        current_result = sum([index * number for index, number in enumerate(numbers)])
        if current_result > best_result:
            best_result = current_result
            best_rotation = rotation
        numbers.rotate()
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