import unittest

from day_three. rucksack_reorganisation import rucksack_reorganisation

test_rucksacks = ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw']

class TestRucksackReorganisation(unittest.TestCase):
    def test_rucksack_reorganisation(self):
        actual = rucksack_reorganisation(test_rucksacks)
        expected = (157,70)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()