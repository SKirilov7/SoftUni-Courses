def stock_availability(boxes, command, *args):
    if command == 'delivery':
        return boxes + list(args)
    elif command == 'sell' and not args:
        return boxes[1:]
    elif command == 'sell' and isinstance(args[0], int):
        return boxes[args[0]:]
    for box in set(args):
        while box in boxes:
            boxes.remove(box)
    return boxes
