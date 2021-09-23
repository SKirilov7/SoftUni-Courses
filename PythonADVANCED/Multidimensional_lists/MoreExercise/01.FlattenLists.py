list = input().split('|')
flatten_list = []
for elements in reversed(list):
    nums = elements.split()
    flatten_list.extend(nums)

print(*flatten_list)