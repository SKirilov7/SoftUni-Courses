def permutate(values, index=0,comb=[]):
    if index == len(values):
        return

    if ''.join(values) not in comb:
        comb.append(''.join(values))

    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permutate(values, index + 1)
        values[i], values[index] = values[index], values[i]

    return comb


list = input().split()
print(*permutate(list),sep='\n')