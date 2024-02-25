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


TestData = namedtuple(
    'TestData',
    [
        'increment',
        'cartesian',
        'data',
        'replace',
        'target',
        'wordlist',
    ]
)

class Permutation(unittest.TestCase):
    def setUp(self):
        # no --increment or --wordlist option given
        self.args = TestData("", "", "", "", "", "")
        self.original_stdout, sys.stdout = sys.stdout, StringIO()

    def test_two_permutation(self):
        with open(pathlib.Path(__file__).parent / 'one.txt', 'r', encoding='UTF-8') as file:
            core.Formula(self.args, [file]).run()
        self.assertEqual(
            sys.stdout.getvalue(),
            (
                "1a-2b3c.4tutu.google.com\n"
                "4tutu.1a-2b3c.google.com\n"
            ),
        )

    def tearDown(self):
        sys.stdout = self.original_stdout


class Incrementation(unittest.TestCase):
    def setUp(self):
        # --increment option enabled
        self.args = TestData("i", "", "", "", "", "")
        self.original_stdout, sys.stdout = sys.stdout, StringIO()

    def test_one_sub_increment(self):
        with open(pathlib.Path(__file__).parent / 'test_one_sub_increment.txt', 'r', encoding='UTF-8') as file:
            core.Formula(self.args, [file]).run()
        self.assertEqual(
            sys.stdout.getvalue().split(),
            [
                'dev.0a.tesla.com',
                'dev.1a.tesla.com',
                'dev.2a.tesla.com',
                'dev.3a.tesla.com',
                'dev.4a.tesla.com',
                'dev.5a.tesla.com',
                'dev.6a.tesla.com',
                'dev.7a.tesla.com',
                'dev.8a.tesla.com',
                'dev.9a.tesla.com',
                'dev.1a.tesla.com',
                '1a.dev.tesla.com'
            ]
        )

    def tearDown(self):
        sys.stdout = self.original_stdout

class Replace(unittest.TestCase):
    def setUp(self):
        # --replace option given
        self.args = TestData("", "", "", "r", "", "")
        self.original_stdout, sys.stdout = sys.stdout, StringIO()

    def test_replace(self):
        with open(pathlib.Path(__file__).parent / 'one.txt', 'r', encoding='UTF-8') as file:
            core.Formula(self.args, [file]).run()
        self.assertEqual(
            sys.stdout.getvalue(),
            (
                "1a-2b3c.4tutu.google.com\n"
                "1a_2b3c.4tutu.google.com\n"
                "1a.2b3c.4tutu.google.com\n"
                "1a-2b3c.4tutu.google.com\n"
                "4tutu.1a-2b3c.google.com\n"
            ),
        )

    def tearDown(self):
        sys.stdout = self.original_stdout


class Cartesian(unittest.TestCase):
    def setUp(self):
        # --increment option enabled
        self.args = TestData("", "c", "", "", "", "")
        self.original_stdout, sys.stdout = sys.stdout, StringIO()

    def test_one_sub_cartesian(self):
        """
        Notes: it removes original sub from output because
        pnk already produces it
        """
        with open(pathlib.Path(__file__).parent / 'test_one_sub_increment.txt', 'r', encoding='UTF-8') as file:
            core.Formula(self.args, [file]).run()
        self.assertEqual(
            sys.stdout.getvalue().split(),
            [
                'dev.0a.tesla.com',
                'dev.1a.tesla.com',
                'dev.2a.tesla.com',
                'dev.3a.tesla.com',
                'dev.4a.tesla.com',
                'dev.5a.tesla.com',
                'dev.6a.tesla.com',
                'dev.7a.tesla.com',
                'dev.8a.tesla.com',
                'dev.9a.tesla.com',
                'dev.1a.tesla.com',
                '1a.dev.tesla.com'
            ]
        )

    def tearDown(self):
        sys.stdout = self.original_stdout


if __name__ == '__main__':
    unittest.main()
