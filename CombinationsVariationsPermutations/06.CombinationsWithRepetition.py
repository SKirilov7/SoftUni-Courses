def combination(list_elements, count, comb=[], index=0):
    if len(comb) == count:
        print(' '.join(comb))
        return
    for i in range(index, len(list_elements)):
        comb.append(list_elements[i])
        combination(list_elements, count, comb, index)
        comb.pop()
        index += 1


elements = input().split()
counter = int(input())
combination(elements, counter)