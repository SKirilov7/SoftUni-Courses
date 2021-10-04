def combination(list_elements, count, comb=[]):
    if len(comb) == count:
        print(' '.join(comb))
        return

    for i in range(len(list_elements)):
        comb.append(list_elements[i])
        combination(list_elements[i+1:], count, comb)
        comb.pop()


elements = input().split()
count_comb = int(input())
combination(elements, count_comb)