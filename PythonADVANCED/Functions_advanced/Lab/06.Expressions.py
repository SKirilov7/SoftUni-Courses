def expressions(nums,result=0,expression='',index=0):
    if index == len(nums):
        print(f"{expression}={result}")
        return

    expressions(nums, result + nums[index], expression + f'+{nums[index]}', index+1)
    expressions(nums, result - nums[index], expression + f'-{nums[index]}', index+1)


numbers = [int(num) for num in input().split(', ')]
expressions(numbers)