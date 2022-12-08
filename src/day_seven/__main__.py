# https://adventofcode.com/2022/day/7

from no_space_left_on_device import no_space_left_on_device


# with open('/Users/antonia/Documents/advent-of-code-2022/src/day_seven/input.txt') as f:
#     filesystem = f.read().splitlines()

filesystem = [
'$ cd /',
'$ ls',
'dir a',
'14848514 b.txt',
'8504156 c.dat',
'dir d'
 '$ cd a',
 '$ ls',
 'dir e',
 '29116 f',
 '2557 g',
 '62596 h.lst',
 '$ cd e',
 '$ ls',
 '584 i',
 '$ cd ..',
 '$ cd ..',
 '$ cd d',
 '$ ls',
 '4060174 j',
 '8033020 d.log',
 '5626152 d.ext',
 '7214296 k'
 ]

result = no_space_left_on_device(filesystem)

print("Sum total sizes directories: " , result[0])
print("Sum total sizes directories: " , result[1])


