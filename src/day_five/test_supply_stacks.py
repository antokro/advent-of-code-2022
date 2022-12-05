#     [D]     2
# [N] [C]     1 
# [Z] [M] [P] 0
#  0   1   2 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2


import unittest

from day_five.supply_stacks import supply_stacks

movements = [
    'move 1 from 2 to 1',
    'move 3 from 1 to 3',
    'move 2 from 2 to 1',
    'move 1 from 1 to 2',
    ]

class TestCampCleanup(unittest.TestCase):
    def test_supply_stacks_9000(self):
        stacks= [['Z', 'N'],['M','C','D'],['P']]
        actual = supply_stacks(stacks,movements,9000)
        expected = 'CMZ'
        self.assertEqual(actual, expected)
    def test_supply_stacks_9001(self):
        stacks= [['Z', 'N'],['M','C','D'],['P']]
        actual = supply_stacks(stacks,movements,9001)
        expected = 'MCD'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()