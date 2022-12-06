import unittest

from day_six.tuning_trouble import tuning_trouble


class TestTuningTrouble(unittest.TestCase):
    def test_one_tuning_trouble(self):
        buffer = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        actual = tuning_trouble(buffer,4)
        expected = 7
        self.assertEqual(actual, expected)
    def test_two_tuning_trouble(self):
        buffer ='bvwbjplbgvbhsrlpgdmjqwftvncz'
        actual = tuning_trouble(buffer,4)
        expected = 5
        self.assertEqual(actual, expected)
    def test_three_tuning_trouble(self):
        buffer ='nppdvjthqldpwncqszvftbrmjlhg' 
        actual = tuning_trouble(buffer,4)
        expected = 6
        self.assertEqual(actual, expected)
    def test_four_tuning_trouble(self):
        buffer ='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' 
        actual = tuning_trouble(buffer,4)
        expected = 10
        self.assertEqual(actual, expected)
    def test_five_tuning_trouble(self):
        buffer ='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' 
        actual = tuning_trouble(buffer,4)
        expected = 11
        self.assertEqual(actual, expected)
    def test_one_tuning_trouble(self):
        buffer = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        actual = tuning_trouble(buffer,14)
        expected = 19
        self.assertEqual(actual, expected)
    def test_two_tuning_trouble(self):
        buffer ='bvwbjplbgvbhsrlpgdmjqwftvncz' 
        actual = tuning_trouble(buffer,14)
        expected = 23
        self.assertEqual(actual, expected)
    def test_three_tuning_trouble(self):
        buffer ='nppdvjthqldpwncqszvftbrmjlhg' 
        actual = tuning_trouble(buffer,14)
        expected = 23
        self.assertEqual(actual, expected)
    def test_four_tuning_trouble(self):
        buffer ='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' 
        actual = tuning_trouble(buffer,14)
        expected = 29
        self.assertEqual(actual, expected)
    def test_five_tuning_trouble(self):
        buffer ='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' 
        actual = tuning_trouble(buffer,14)
        expected = 26
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()