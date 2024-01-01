import sys
import argparse
import itertools
import pathlib
import re

from urllib.parse import urlparse
from helpers import logger

log = logger.get_logger()


class Formula:
    def __init__(self, args) -> None:
        self.args = args
        self.host, self.domain, self.subdomains = self.parse_hostname()

    def parse_hostname(self):
        """Extract a domain and subdomains from the input"""
        url = urlparse(self.args.domain)
        host = url.hostname or url.geturl()
        _domain = re.search(r"[\w-]+[.](com|co.uk|ru|org|co|in|ai|sh|io)$", host)
        _subdomains = host[:_domain.start()] + host[_domain.end():]
        if not _subdomains:
            sys.stderr.write(f"No subdomains found for {host}")
            sys.stderr.flush()
            sys.exit(1)

        domain = _domain.group(0)
        subdomains = _subdomains.split('.')[:-1]
        log.debug(f"{host=}")
        log.debug(f"{domain=}")
        log.debug(f"{subdomains=}")
        
        return host, domain, subdomains

    def pnk(self):
        """Sequence of permutations wordlist on domain name"""
        log.debug("Permutation...")
        perms = itertools.permutations(self.subdomains, len(self.subdomains))
        for p in perms:
            print(p, flush=True)
            s = ".".join(p)
            print(s + "." + self.domain, flush=True)

        log.debug("Done!")

    def produce_wordlist(self):
        """Read the wordlist and returns lines generator"""
        wordlist = self.args.wordlist if self.args.wordlist else pathlib.Path(__file__).parent / 'wordlist.txt'
        with open(wordlist, 'r', encoding='UTF-8') as file:
            for line in file:
                yield line.strip()


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
