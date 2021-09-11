from fibbonacci.core import *

command_data = input()
seq = None
while not command_data == 'Stop':
    command, *rest  = command_data.split()
    if command == 'Create':
        seq = create_fibb(int(rest[-1]))
        print(*seq)

    else:
        print(locate(int(rest[-1]),seq))

    command_data = input()
