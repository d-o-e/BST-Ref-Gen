import unittest

import main

from bst import Leaf


class MyTestCase(unittest.TestCase):
    def test_Leaf_neg(self):
        self.assertIsNone(Leaf(None).data)
        self.assertIsNone(print(Leaf()))


if __name__ == '__main__':
    unittest.main()