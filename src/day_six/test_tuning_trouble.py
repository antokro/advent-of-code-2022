import unittest

from day_six.tuning_trouble import tuning_trouble_part_one, tuning_trouble_part_two


class TestTuningTrouble(unittest.TestCase):
    def test_one_tuning_trouble_part_one(self):
        buffer = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        actual = tuning_trouble_part_one(buffer)
        expected = 7
        self.assertEqual(actual, expected)
    def test_two_tuning_trouble_part_one(self):
        buffer ='bvwbjplbgvbhsrlpgdmjqwftvncz'
        actual = tuning_trouble_part_one(buffer)
        expected = 5
        self.assertEqual(actual, expected)
    def test_three_tuning_trouble_part_one(self):
        buffer ='nppdvjthqldpwncqszvftbrmjlhg' 
        actual = tuning_trouble_part_one(buffer)
        expected = 6
        self.assertEqual(actual, expected)
    def test_four_tuning_trouble_part_one(self):
        buffer ='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' 
        actual = tuning_trouble_part_one(buffer)
        expected = 10
        self.assertEqual(actual, expected)
    def test_five_tuning_trouble_part_one(self):
        buffer ='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' 
        actual = tuning_trouble_part_one(buffer)
        expected = 11
        self.assertEqual(actual, expected)
    def test_one_tuning_trouble_part_two(self):
        buffer = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        actual = tuning_trouble_part_two(buffer)
        expected = 19
        self.assertEqual(actual, expected)
    def test_two_tuning_trouble_part_two(self):
        buffer ='bvwbjplbgvbhsrlpgdmjqwftvncz' 
        actual = tuning_trouble_part_two(buffer)
        expected = 23
        self.assertEqual(actual, expected)
    def test_three_tuning_trouble_part_two(self):
        buffer ='nppdvjthqldpwncqszvftbrmjlhg' 
        actual = tuning_trouble_part_two(buffer)
        expected = 23
        self.assertEqual(actual, expected)
    def test_four_tuning_trouble_part_two(self):
        buffer ='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' 
        actual = tuning_trouble_part_two(buffer)
        expected = 29
        self.assertEqual(actual, expected)
    def test_five_tuning_trouble_part_two(self):
        buffer ='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' 
        actual = tuning_trouble_part_two(buffer)
        expected = 26
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()