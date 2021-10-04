def expressions_recursive_func(nums, string='', index=0, current_sum=0):
    if index == len(nums):
        print(f'{string}={current_sum}')
        return

    expressions_recursive_func(nums, string + f'+{nums[index]}', index + 1, current_sum + nums[index])
    expressions_recursive_func(nums, string + f'-{nums[index]}', index + 1, current_sum - nums[index])


numbers = [int(num) for num in input().split(', ')]
expressions_recursive_func(numbers)