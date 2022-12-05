# https://adventofcode.com/2022/day/3

from camp_cleanup import camp_cleanup


with open('/Users/antonia/Documents/advent-of-code-2022/src/day_four/input.txt') as f:
    input_sections = f.read().splitlines()
    
camp_cleanup(input_sections)