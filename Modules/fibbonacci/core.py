def create_fibb(n):
    seq = [0,1]
    for _ in range(2,n):
        result = seq[-1] + seq[-2]
        seq.append(result)
    return seq

def locate(num,seq):
    if num in seq:
        index = seq.index(num)
        return f"The number - {num} is at index {index}"
    return f"The number {num} is not in the sequence"