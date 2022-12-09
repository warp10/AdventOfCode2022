#!/usr/bin/env python3

import unittest

from solution import main


class TestPuzzle(unittest.TestCase):
    def test_main_1(self):
        self.assertEqual(main("test_input_1.txt"), 1)
    def test_main_2(self):
        self.assertEqual(main("test_input_2.txt"), 36)


if __name__ == "__main__":
    unittest.main()
