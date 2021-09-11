from Math_operations.core import operation_mapper

first_num,operator,second_num = input().split()
first_num = float(first_num)
second_num = float(second_num)


print(f"{(operation_mapper[operator](first_num,second_num)):.2f}")