# https://adventofcode.com/2022/day/7

from no_space_left_on_device import no_space_left_on_device

with open('/Users/antonia/Documents/advent-of-code-2022/src/day_seven/input.txt') as f:
    filesystem = f.read().splitlines()

result = no_space_left_on_device(filesystem)

print("Sum total sizes directories: " , result[0])
print("Sum total sizes directories: " , result[1])


