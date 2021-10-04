def recursive_factorial(number):
    if number == 1:
        return 1
    return number * recursive_factorial(number - 1)

number_factorial = int(input())
print(recursive_factorial(number_factorial))