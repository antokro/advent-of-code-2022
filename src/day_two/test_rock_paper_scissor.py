import unittest

from day_two.rock_paper_scissor import rock_paper_scissor_part_one, rock_paper_scissor_part_two

class TestCampCleanup(unittest.TestCase):
    def test_rock_paper_scissor_part_one(self):
        strategy = ['A Y','B X','C Z']
        actual = rock_paper_scissor_part_one(strategy)
        expected = 15
        self.assertEqual(actual, expected)
    def test_rock_paper_scissor_part_two(self):
        strategy = ['A Y','B X','C Z']
        actual = rock_paper_scissor_part_two(strategy)
        expected = 12
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()