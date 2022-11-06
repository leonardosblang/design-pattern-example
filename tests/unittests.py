from sorting_techniques.pysort import Sorting

from sorting import *
import unittest


class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        list_to_sort = [5, 3, 2, 1, 4]

        sorted_list = BubbleSort.selection(0, list_to_sort)

        self.assertEqual(sorted_list, [1, 2, 3, 4, 5])

    def test_quick_sort(self):
        list_to_sort = [5, 3, 2, 1, 4]

        sorted_list = QuickSort.selection(0, list_to_sort)

        self.assertEqual(sorted_list, [1, 2, 3, 4, 5])

    def test_heap_sort(self):
        list_to_sort = [5, 3, 2, 1, 4]

        sorted_list = HeapSort.selection(0, list_to_sort)

        self.assertEqual(sorted_list, [1, 2, 3, 4, 5])

    def test_insertion_sort(self):
        list_to_sort = [5, 3, 2, 1, 4]

        sorted_list = InsertionSort.selection(0, list_to_sort)

        self.assertEqual(sorted_list, [1, 2, 3, 4, 5])
