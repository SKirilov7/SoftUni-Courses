text = input()

try:
    number_of_repeating = int(input())
    print(number_of_repeating * text)
except ValueError:
    print('Variable times must be an integer')