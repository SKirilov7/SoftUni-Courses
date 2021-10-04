def generate_vectors(vector,current_index=0):
    if current_index >= len(vector):
        print(''.join([str(num) for num in vector]))
        return

    for num in range(2):
        vector[current_index] = num
        generate_vectors(vector, current_index + 1)


number = int(input())
vector = [0] * number
generate_vectors(vector)