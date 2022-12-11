# https://adventofcode.com/2022/day/11

from monkey_in_the_middle import monkey_in_the_middle

monkeys = [
[[65, 58, 93, 57, 66],('multiply',7 ), (19, 6, 4)],
[[76, 97, 58, 72, 57, 92, 82],('add',4 ) , (3, 7, 5)],
[[90, 89, 96],('multiply', 5 ) , (13, 5, 1)],
[[72, 63, 72, 99],('square',0) , (17, 0, 4)],
[[65],('add',1 ) , (2, 6, 2)],
[[97, 71],('add', 8) , (11, 7, 3)],
[[83, 68, 88, 55, 87, 67],('add', 2) , (5, 2, 1)],
[[64, 81, 50, 96, 82, 53, 62, 92],('add', 5) , (7, 3, 0)]
]

result = monkey_in_the_middle(monkeys)
result_part_two = monkey_in_the_middle(monkeys,1000, False)

print(f"The level of monkey business after 20 rounds is {result}")
print(f"The level of monkey business after 1000 rounds is {result}")