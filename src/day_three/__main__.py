# https://adventofcode.com/2022/day/3

from rucksack_reorganisation import rucksack_reorganisation


with open('/Users/antonia/Documents/advent-of-code-2022/src/day_three/input.txt') as f:
    input_rucksacks = f.read().splitlines()

rucksack_reorganisation(input_rucksacks)