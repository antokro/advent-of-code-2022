import unittest

sections = [
'2-4,6-8',
'2-3,4-5',
'5-7,7-9',
'2-8,3-7',
'6-6,4-6',
'2-6,4-8',
]

from day_four.camp_cleanup import camp_cleanup

test_rucksacks = ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw']

class TestCampCleanup(unittest.TestCase):
    def test_camp_cleanup(self):
        actual = camp_cleanup(sections)
        expected = (2,4)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()