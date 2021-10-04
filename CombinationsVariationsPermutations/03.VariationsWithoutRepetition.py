def variation(elements,count,bool_elements,var=[]):
    if len(var) == count:
        print(' '.join(var))
        return

    for i in range(len(elements)):
        if not bool_elements[i]:
            bool_elements[i] = True
            var.append(elements[i])
            variation(elements, count, boolean_elements, var)
            bool_elements[i] = False
            var.pop()


elements = input().split()
num_elements_allowed = int(input())
boolean_elements = [False] * len(elements)
variation(elements, num_elements_allowed, boolean_elements)

