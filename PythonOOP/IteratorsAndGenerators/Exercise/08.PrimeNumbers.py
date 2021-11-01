def get_primes(nums):
    for number in nums:
        if not len([divider for divider in range(2, number) if number % divider == 0]) > 0 and number not in [0, 1]:
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
