# https://adventofcode.com/2022/day/8

from treetop_tree_house import treetop_tree_house

# with open('/Users/antonia/Documents/advent-of-code-2022/src/day_eight/input.txt') as f:
#     trees = f.read().split()

trees = [
'30373',
'25512',
'65332',
'33549',
'35390',
]

result = treetop_tree_house(trees)

print(f"There are {result[0]} visible trees.")
print(f"The highest scenic score is {result[1]}")