def permutate(values, index=0):
    if index == len(values):
        print(*values, sep='')
        return

    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permutate(values, index + 1)
        values[i], values[index] = values[index], values[i]


permutate(list(input()))