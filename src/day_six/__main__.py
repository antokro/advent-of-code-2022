# https://adventofcode.com/2022/day/5
from tuning_trouble import tuning_trouble

with open('/Users/antonia/Documents/advent-of-code-2022/src/day_six/input.txt') as f:
    buffer = f.read()

result = tuning_trouble(buffer,4)
print(f"First market is found after {result} characters.")

result_part_two = tuning_trouble(buffer,14)
print(f"First market is found after {result_part_two} characters.")

