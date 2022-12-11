# {monkey: [[items],(operation, number),(test, if true, if false) ] }
import math

def monkey_in_the_middle(monkeys: list, rounds = 20, divide_worry_level = True):
    inspections = [0] * len(monkeys)
    for _ in range(0,rounds):
        for x in range(len(monkeys)):
            copied_items = monkeys[x][0][:]
            for i in copied_items:
                if monkeys[x][1][0] == 'multiply':
                    worry_level = i * monkeys[x][1][1]
                elif monkeys[x][1][0] == 'add':
                    worry_level = i + monkeys[x][1][1]
                else:
                    worry_level = i**2
                if divide_worry_level:
                    new_worry_level = math.trunc(worry_level / 3)
                else: 
                    new_worry_level = worry_level

                if divmod(new_worry_level, monkeys[x][2][0])[1] == 0:
                    monkeys[x][0].remove(i)
                    monkeys[monkeys[x][2][1]][0].append(new_worry_level)
                else: 
                    monkeys[x][0].remove(i)
                    monkeys[monkeys[x][2][2]][0].append(new_worry_level)
                inspections[x] = inspections[x] + 1

    
    inspections.sort(reverse=True)

    return inspections[0] * inspections[1]

