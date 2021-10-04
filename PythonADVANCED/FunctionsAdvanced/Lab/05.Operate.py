def operate(operator,*args):
    result = args[0]
    for num in args[1:]:
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        elif operator == '*':
            result *= num
        else:
            if not num == 0:
                result /= num
            else:
                return None
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 2, 0))