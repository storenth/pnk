#!/usr/bin/python3

import argparse
import os
import sys

# need to import pnk in case of testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pnk import __version__
from pnk.core import Formula


def setup_argparse():
    """Read arguments from cli"""
    parser = argparse.ArgumentParser(
        description="Generates a new subdomains on provided input"
    )
    # optional argument
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-i",
        "--increment",
        action="store_true",
        help="increment any one or two digits on subdomains",
    )
    group.add_argument(
        "-c",
        "--cartesian",
        action="store_true",
        help="increment digits on subdomains creating their Cartesian product",
    )
    parser.add_argument(
        "-d", "--data", action="store_true", help="generate test data from the stdin"
    )
    parser.add_argument(
        "-r", "--replace",
        action="store_true",
        help="replace underscores and dashes with dots",
    )
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        default="",
        help="target domain to find subs for (which will not be processed)",
    )
    parser.add_argument(
        "-w",
        "--wordlist",
        type=argparse.FileType('r', encoding='UTF-8'),
        help="mixed subdomains with wordlist",
    )
    # positional argument
    parser.add_argument(
        "file",
        nargs="*",
        type=argparse.FileType("r", encoding="UTF-8"),
        default=[sys.stdin],
        metavar="FILE",
        help="list of subdomains/hosts to process",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    args = parser.parse_args()
    if not args.file:
        parser.print_help(sys.stderr)
        parser.exit(1)
    return args


def main():
    """Entry point for the programm"""
    args = setup_argparse()
    frml = Formula(args, args.file)
    frml.run()


if __name__ == "__main__":
    main()
