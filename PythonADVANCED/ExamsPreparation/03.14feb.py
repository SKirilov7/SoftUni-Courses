def stock_availability(boxes, command, *args):
    if command == 'delivery':
        [boxes.append(arg) for arg in args]
        return boxes

    elif command == 'sell' and not args:
        return boxes[1:]

    for arg in args:
        try:
            boxes = boxes[int(arg):]
        except ValueError:
            while arg in boxes:
                boxes.remove(arg)
    return boxes




print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

