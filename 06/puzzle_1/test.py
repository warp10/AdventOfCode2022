#!/usr/bin/env python3

import unittest

from solution import main


class TestPuzzle(unittest.TestCase):
    def test_main_1(self):
        self.assertEqual(main("test_input_0.txt"), 19)

    def test_main_2(self):
        self.assertEqual(main("test_input_1.txt"), 23)

    def test_main_3(self):
        self.assertEqual(main("test_input_2.txt"), 23)

    def test_main_4(self):
        self.assertEqual(main("test_input_3.txt"), 29)

    def test_main_5(self):
        self.assertEqual(main("test_input_4.txt"), 26)


if __name__ == "__main__":
    unittest.main()
