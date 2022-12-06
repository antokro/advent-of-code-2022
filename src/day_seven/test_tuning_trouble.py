import unittest

from day_seven.tuning_trouble import tuning_trouble


class TestTuningTrouble(unittest.TestCase):
    def test_one_tuning_trouble(self):
        buffer = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        actual = tuning_trouble(buffer,4)
        expected = 7
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()