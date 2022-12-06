import unittest
from day_one.calorie_counting import calorie_counting

sections = [
'1000',
'',
'2000',
'3000',
'',
'4000',
'',
'5000',
'6000',
'',
'7000',
'8000',
'9000',
'',
'10000',
]

class TestCampCleanup(unittest.TestCase):
    def test_calorie_counting(self):
        actual = calorie_counting(sections)
        expected = (24000, 45000)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()