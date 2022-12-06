from supply_stacks import supply_stacks

# https://adventofcode.com/2022/day/5

# [N]     [Q]         [N]            
# [R]     [F] [Q]     [G] [M]        
# [J]     [Z] [T]     [R] [H] [J]    
# [T] [H] [G] [R]     [B] [N] [T]    
# [Z] [J] [J] [G] [F] [Z] [S] [M]    
# [B] [N] [N] [N] [Q] [W] [L] [Q] [S]
# [D] [S] [R] [V] [T] [C] [C] [N] [G]
# [F] [R] [C] [F] [L] [Q] [F] [D] [P]
#  1   2   3   4   5   6   7   8   9 

stacks = [
    ['F', 'D','B','Z','T','J','R','N'],
    ['R','S','N','J','H'],
    ['C', 'R','N','J','G','Z','F','Q'],
    ['F', 'V','N','G','R','T','Q'],
    ['L', 'T','Q','F'],
    ['Q', 'C','W','Z','B','R','G','N'],
    ['F', 'C','L','S','N','H','M'],
    ['D', 'N','Q','M','T','J'],
    ['P','G','S']
    ]

stacks_two = [
    ['F', 'D','B','Z','T','J','R','N'],
    ['R','S','N','J','H'],
    ['C', 'R','N','J','G','Z','F','Q'],
    ['F', 'V','N','G','R','T','Q'],
    ['L', 'T','Q','F'],
    ['Q', 'C','W','Z','B','R','G','N'],
    ['F', 'C','L','S','N','H','M'],
    ['D', 'N','Q','M','T','J'],
    ['P','G','S']
    ]


with open('/Users/antonia/Documents/advent-of-code-2022/src/day_five/input.txt') as f:
    movements = f.read().splitlines()

result_9000 = supply_stacks(stacks,movements, 9000)
print('The top boxes are: ',''.join(result_9000))

result_9001 = supply_stacks(stacks_two,movements, 9001)
print('The top boxes are: ',''.join(result_9001))
