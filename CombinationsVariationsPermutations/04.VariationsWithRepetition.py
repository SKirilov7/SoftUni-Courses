def variation(elements, count, var=[]):
    if len(var) == count:
        print(' '.join(var))
        return
    for i in range(len(elements)):
        var.append(elements[i])
        variation(elements, count, var)
        var.pop()


elements = input().split()
count = int(input())
variation(elements, count)