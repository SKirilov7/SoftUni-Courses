def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        list_nums = []
        for i in range(n):
            list_nums.append(next(seq))
        return list_nums

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
