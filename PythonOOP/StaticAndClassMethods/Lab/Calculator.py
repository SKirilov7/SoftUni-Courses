class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @ staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(initial_sum, *args):
        for number in args:
            initial_sum /= number
        return initial_sum

    @staticmethod
    def subtract(initial_sum, *args):
        for number in args:
            initial_sum -= number
        return initial_sum


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
