def even_parameters(func):
    def wrapper(*args):
        if all([(True if isinstance(arg, int) and arg % 2 == 0 else False) for arg in args]):
            return func(*args)
        return 'Please use only even numbers!'

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
