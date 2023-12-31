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
        self.host = self.get_host()
        self.subdomains = self.get_subdomains()

    def get_host(self):
        url = urlparse(self.args.domain)
        host = url.hostname or url.geturl()
        log.debug(f"{host=}")
        return host

    def pnk(self):
        """Sequence of permutations wordlist on domain name"""
        log.debug("Permutation...")
        combined_words = itertools.chain(self.produce_wordlist(), self.subdomains)
        perms = itertools.permutations(combined_words, len(list(self.subdomains)))
        for p in perms:
            print(p, flush=True)
            print(".".join(p), flush=True)
            # print(".".join(p) + "." + self.args.domain, flush=True)

        log.debug("Done!")

    def produce_wordlist(self):
        """Read the wordlist and returns lines generator"""
        wordlist = self.args.wordlist if self.args.wordlist else pathlib.Path(__file__).parent / 'wordlist.txt'
        with open(wordlist, 'r', encoding='UTF-8') as file:
            for line in file:
                yield line.strip()

    def get_subdomains(self):
        """Extract the subdomains from the input"""
        # TODO: remove starting `www` and handle `co.uk`-like hostnames
        subdomains = self.host.split('.')[:-2]
        log.debug(len(subdomains))
        log.debug(subdomains)
        if subdomains:
            return subdomains
        else:
            sys.stderr.write(f"No subdomains found for {self.host}")
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
