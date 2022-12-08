import unittest

from day_eight.treetop_tree_house import treetop_tree_house

trees = [
'30373',
'25512',
'65332',
'33549',
'35390',
]


class TestTreetopTreeHouse(unittest.TestCase):
    def test_treetop_tree_house(self):
        actual = treetop_tree_house(trees)
        expected = (21,8)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()