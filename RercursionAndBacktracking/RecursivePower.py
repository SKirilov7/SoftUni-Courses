def recursive_power(num, pow):
    if pow == 1:
        return num
    return num * recursive_power(num, pow-1)

print(recursive_power(2, 10))
print(recursive_power(10, 100))