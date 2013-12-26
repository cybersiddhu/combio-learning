"""Unit tests for all sorting algorithm"""
import unittest
from sort import (insertionsort_ascending,
                  selectionsort_ascending, shellsort_ascending)


# pylint: disable=R0904
class SortingTestCase(unittest.TestCase):
    """Unit test class"""

    def test_selectionsort_ascending(self):
        """test insertionsort algorithm"""
        alist = [9, 2, 15, 4, 3, 1, 7]
        newlist = alist[:5]
        self.assertTrue(selectionsort_ascending(alist),
                        'should run insertionsort')
        self.assertListEqual(alist, [1, 2, 3, 4, 7, 9, 15],
                             'should sorted uneven list')
        self.assertTrue(selectionsort_ascending(newlist),
                        'should run insertionsort')
        self.assertListEqual(newlist, [2, 3, 4, 9, 15],
                             'should sorted even list')

    def test_insertionsort_ascending(self):
        """test insertionsort algorithm"""
        alist = [9, 2, 15, 4, 3, 1, 7]
        newlist = alist[:5]
        self.assertTrue(insertionsort_ascending(alist),
                        'should run insertionsort')
        self.assertListEqual(alist, [1, 2, 3, 4, 7, 9, 15],
                             'should sorted uneven list')
        self.assertTrue(insertionsort_ascending(newlist),
                        'should run insertionsort')
        self.assertListEqual(newlist, [2, 3, 4, 9, 15],
                             'should sorted even list')


    def test_shellsort_ascending(self):
        """test shellsort algorithm"""
        alist = [9, 2, 15, 4, 3, 1, 7, 90, 75, 65, 85, 55]
        self.assertTrue(shellsort_ascending(alist),
                        'should run insertionsort')
        self.assertListEqual(alist, [1, 2, 3, 4, 7, 9, 15, 55, 65, 75, 85, 90],
                             'should run shell sort')


if __name__ == '__main__':
    unittest.main()
