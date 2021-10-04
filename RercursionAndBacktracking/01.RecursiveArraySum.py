def recursive_array_sum(nums, index = 0):
    if index == len(nums):
        return 0
    return nums[index] + recursive_array_sum(nums, index + 1)

numbers = [int(num) for num in input().split()]
print(recursive_array_sum(numbers))