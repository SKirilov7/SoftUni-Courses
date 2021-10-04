command = input()
numbers = [int(num) for num in input().split()]

odd_or_even = 0 if command == 'Even' else 1
result = sum([num for num in numbers if num % 2 == odd_or_even])

print(result * len(numbers))