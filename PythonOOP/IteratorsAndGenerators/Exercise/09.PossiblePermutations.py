def all_permutations(elements):
    if len(elements) <= 1:
        return [elements]

    list_permutations = []
    for i in range(len(elements)):
        first_element = elements[i]

        other_elements = elements[:i] + elements[i + 1:]

        for perm in all_permutations(other_elements):
            list_permutations.append([first_element] + perm)

    return list_permutations


def possible_permutations(list_of_elements):
    for permutation in all_permutations(list_of_elements):
        yield permutation


[print(n) for n in possible_permutations([1, 2, 3])]
