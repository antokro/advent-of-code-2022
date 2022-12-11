# https://adventofcode.com/2022/day/9

from rope_bridge import rope_bridge


with open('/Users/antonia/Documents/advent-of-code-2022/src/day_nine/input.txt') as f:
    moves = f.read().splitlines()

result = rope_bridge(moves, 2)
result_2 = rope_bridge(moves, 10)

print(f"There are {result} positions the tail visited at least once")
print(f"There are {result_2} positions the tail visited at least once if the rope as a length of 9 knots.")