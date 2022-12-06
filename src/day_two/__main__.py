# https://adventofcode.com/2022/day/2

from rock_paper_scissor import rock_paper_scissor_part_one, rock_paper_scissor_part_two

with open('/Users/antonia/Documents/advent-of-code-2022/src/day_two/input.txt') as f:
    strategy= f.read().splitlines()

strategy_two = strategy.copy()
    
result_part_one = rock_paper_scissor_part_one(strategy)
result_part_two = rock_paper_scissor_part_two(strategy_two)

print("Result if X,Y,Z means rock, paper or scissor:", result_part_one)
print("Result if X,Y,Z means draw,win or loss: ", result_part_two)