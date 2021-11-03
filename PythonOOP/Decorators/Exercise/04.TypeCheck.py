def type_check(type_):
    def decorator(func):
        def wrapper(*args):
            if all([(True if isinstance(arg, type_) else False) for arg in args]):
                return func(*args)
            return 'Bad Type'

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
