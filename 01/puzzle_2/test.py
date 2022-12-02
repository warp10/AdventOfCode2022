#!/usr/bin/env python3

import unittest

from solution import main


class TestPuzzle(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main('test_input.txt'), 45000)


if __name__ == '__main__':
    unittest.main()
