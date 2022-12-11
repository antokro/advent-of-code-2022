import unittest

from day_eleven.monkey_in_the_middle import monkey_in_the_middle

monkeys = [
    [[79, 98],('multiply', 19),(23, 2, 3)],
    [[54, 65, 75, 74],('add', 6),(19, 2, 0)],
    [[79, 60, 97],('square'),(13, 1, 3)],
    [[74],('add',3),(17, 0, 1)]
    ]


class TestMonkeyInTheMiddle(unittest.TestCase):
    def test_monkey_in_the_middle(self):
        copy = monkeys[:]
        actual = monkey_in_the_middle(copy)
        expected = (10605)
        self.assertEqual(actual, expected)
    def test_monkey_in_the_middle_part_two(self):
        copy = monkeys[:]
        actual = monkey_in_the_middle(copy,500,False)
        expected = (6721050)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()