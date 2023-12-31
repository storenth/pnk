import sys
import argparse
import itertools
import pathlib
from helpers import logger
from urllib.parse import urlparse


log = logger.get_logger()


class Formula:
    def __init__(self, args) -> None:
        self.args = args

    def pnk(self):
        """sequence of permutations wordlist on domain name"""
        log.debug(list(itertools.permutations(self.produce_wordlist())))

    def produce_wordlist(self):
        """Read the wordlist and returns lines generator"""
        wordlist = self.args.wordlist if self.args.wordlist else pathlib.Path(__file__).parent / 'wordlist.txt'
        with open(wordlist, 'r', encoding='UTF-8') as file:
            for line in file:
                yield line.strip()

    def produce_subdomains(self):
        """Extract the subdomains from the input"""
        

def setup_argparse():
    """Read arguments from cli"""
    parser = argparse.ArgumentParser(
        description="Set CLI args pnk works with")
    parser.add_argument(
        '-d', '--domain', help='domain to get subdomains permutations for'
    )
    parser.add_argument('-w', '--wordlist', help='wordlist file')
    args = parser.parse_args()
    if args.domain is None:
        parser.print_help(sys.stderr)
        parser.exit(1)
    return args


def main(args):
    """Entry point for the programm"""
    if args.wordlist:
        log.debug(f"{args.wordlist}")
    if args.domain is None:
        log.debug(f"{args.domain}")

    frml = Formula(args)
    frml.pnk()

if __name__ == '__main__':
    args = setup_argparse()
    main(args)
