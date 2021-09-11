def triangle_maker(n):
    triangle = []
    for row in range(1,n+1):
        current_form = []
        for col in range(1,row+1):
            print(col, end=' ')
        print()
    for row in range(n - 1,0,-1):
        current_form = []
        for col in range(1,row+1):
            print(col,end= ' ')
        print()


def print_triangle(n):
    triangle_maker(n)

