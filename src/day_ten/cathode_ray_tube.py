def cathode_ray_tube(program):
    formatted_program = []
    for x in range(len(program)):
        splitted = program[x].split()
        if(len(splitted) == 2):
            formatted_program.append((splitted[0], int(splitted[1])))
        else:
            formatted_program.append((splitted[0], 0))
    X = 1
    cycles = []
    cycle_count = 0
    for command, length in formatted_program:
        if command == 'addx':
            for _ in range(0,2):
                cycle_count += 1
                cycles.append((cycle_count, X))
        elif command == 'noop':
            cycle_count += 1
            cycles.append((cycle_count, X))
            
        X += length

    interesting_cycles = [20,60,100,140,180,220]
    total = 0

    for c in interesting_cycles:
        total += [tup for tup in cycles if tup[0] == c][0][1] * c

    # screen = [['.']*40 for _ in range(6)]



    # for row in screen:
    #     for r in row:
    #         print(r, end=' ')
        
    #     print()

    
    return total


##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....

# # # # # . . # # . . # # # . . . # # . . . . # # . # # # # . . . # # . # # # # . 
# . . . # . # . . # . # . . # . # . . # . . . . # . # . . . . . . . # . . . . # . 
# . . # . . # . . . . # # # . . # . . # . . . . # . # # # . . . . . # . . . # . . 
# . # . . . # . . . . # . . # . # # # # . . . . # . # . . . . . . . # . . # . . . 
# # . . . . # . . # . # . . # . # . . # . # . . # . # . . . . # . . # . # . . . . 
# # # # # . . # # . . # # # . . # . . # . . # # . . # . . . . . # # . . # # # # . 

    # # get the inputs
    # inputs = read_input()    

    # # get the screen
    # screen = [['.']*40 for _ in range(6)]

    # # go through the inputs
    # x_register = 1
    # for cycle, (instruction, value) in enumerate(inputs, 1):

    #     # check whether cycle is value of x register minus one/ equal / plus one
    #     rx, cx = divmod(cycle-1, 40)
    #     if x_register - 1 <= cx <= x_register + 1:
    #         screen[rx][cx] = '#'

    #     # update the signal
    #     x_register += value

    # print('The result for solution 2 is:')
    # for row in screen:
    #     for ele in row:
    #         print(ele, end=' ')
    #     print()