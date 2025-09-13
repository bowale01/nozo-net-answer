import unittest
from duplicates import find_duplicates


class TestFindDuplicates(unittest.TestCase):
    def test_happy_path(self):
        self.assertEqual(find_duplicates(['c','a','i','o','p','a']), ['a'])

    def test_empty(self):
        self.assertEqual(find_duplicates([]), [])

    def test_none(self):
        self.assertEqual(find_duplicates(None), [])

    def test_multiple_dupes_and_order(self):
        self.assertEqual(find_duplicates(['x','y','x','z','y','y','w','x']), ['x', 'y'])

    def test_unhashable_skipped(self):
        self.assertEqual(find_duplicates(['a', ['b'], 'a', {'c': 1}]), ['a'])


if __name__ == '__main__':
    unittest.main()
