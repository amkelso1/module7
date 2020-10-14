import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_list.search_list', return_value=[2])
    def test_item_found(self, input):
        self.assertEqual(sort_and_search_list.search_list(), [2])


class TestList(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_list.search_list', return_value='-1')
    def test_item_not_found(self, input):
        self.assertEqual(sort_and_search_list.search_list(), '-1')


if __name__ == '__main__':
    unittest.main()
