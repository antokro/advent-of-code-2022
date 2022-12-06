def supply_stacks(stacks, movements, moverType):
    transformed_movements = []
    for x in range(len(movements)):
        amount = int(movements[x].split(' ')[1])
        from_stack = int(movements[x].split(' ')[3])-1
        to_stack = int(movements[x].split(' ')[5])-1

        transformed_movements.append((amount, from_stack, to_stack))

    for amount, from_stack, to_stack in transformed_movements:
        length = len(stacks[from_stack])
        cut_start = length - amount
        stacks_to_move = stacks[from_stack][cut_start:length]
        if moverType == 9000:
            stacks_to_move.reverse()
        stacks[from_stack] = stacks[from_stack][0:cut_start]

        for s in stacks_to_move:
            stacks[to_stack].append(s)

    top_boxes = []

    for s in stacks:
        top_boxes.append(s[-1:][0])

    return ''.join(top_boxes)


