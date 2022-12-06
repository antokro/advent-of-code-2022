# https://adventofcode.com/2022/day/1

from calorie_counting import calorie_counting


with open('/Users/antonia/Documents/advent-of-code-2022/src/day_one/input.txt') as f:
    input_sections = f.read().splitlines()
    
result = calorie_counting(input_sections)

print("Elf carrying most calories: ", result[0])
print("Top 3 Elfs carrying most calories", result[1])