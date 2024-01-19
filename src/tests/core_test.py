"""Integration tests
Simulates CLI usage

Run:
    python3 -m unittest src/tests/core_test.py -vb
"""

import os
import pathlib
import sys
import unittest
from collections import namedtuple
from io import StringIO

# need to import pnk in case of testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pnk import core


class Permutation(unittest.TestCase):
    def setUp(self):
        TestData = namedtuple('TestData', ['increment', 'wordlist'])
        # no --increment or --wordlist option given
        self.args = TestData("", "")
        self.original_stdout, sys.stdout = sys.stdout, StringIO()

    def test_two_permutation(self):
        with open(pathlib.Path(__file__).parent / 'one.txt', 'r', encoding='UTF-8') as file:
            core.Formula(self.args, [file]).run()
        self.assertEqual(
            sys.stdout.getvalue(),
            "1a-2b3c.4tutu.google.com\n4tutu.1a-2b3c.google.com\n",
        )

    def tearDown(self):
        sys.stdout = self.original_stdout

if __name__ == '__main__':
    unittest.main()