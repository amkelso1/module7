import unittest
from unittest.mock import patch
from fun_with_collections import basic_lists


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.basic_lists.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(basic_lists.make_list(), [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
