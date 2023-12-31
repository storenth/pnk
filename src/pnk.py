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
        """Sequence of permutations wordlist on domain name"""
        log.debug("Permutation...")
        perms = itertools.permutations(itertools.chain(self.produce_wordlist(), self.produce_subdomains()), len(list(self.produce_subdomains())))
        for x in perms:
            print(x, flush=True)
            print(".".join(x), flush=True)
        log.debug("Done!")

        

    def produce_wordlist(self):
        """Read the wordlist and returns lines generator"""
        wordlist = self.args.wordlist if self.args.wordlist else pathlib.Path(__file__).parent / 'wordlist.txt'
        with open(wordlist, 'r', encoding='UTF-8') as file:
            for line in file:
                yield line.strip()

    def produce_subdomains(self):
        """Extract the subdomains from the input"""
        url = urlparse(self.args.domain)
        log.debug(url)
        log.debug(url.hostname)
        log.debug(url.netloc)
        log.debug(url.geturl())
        log.debug(url.path)
        host = url.hostname or url.geturl()
        log.debug(f"{host=}")

        # TODO: remove starting `www` and handle `co.uk`-like hostnames
        subdomains = host.split('.')[:-2]
        log.debug(len(subdomains))
        log.debug(subdomains)
        if subdomains:
            for sub in subdomains:
                yield sub
        else:
            sys.stderr.write(f"No subdomains found for {host}")
            sys.stderr.flush()
            sys.exit(1)



def setup_argparse():
    """Read arguments from cli"""
    parser = argparse.ArgumentParser(
        description="Set CLI args pnk works with")
    parser.add_argument(
        '-d', '--domain', help='hostname to get subdomains permutations for'
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
    if args.domain:
        log.debug(f"{args.domain}")

    frml = Formula(args)
    frml.pnk()

if __name__ == '__main__':
    args = setup_argparse()
    main(args)
