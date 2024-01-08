#!/usr/bin/python3
import sys
import argparse
import itertools
import functools
import pathlib
import re

from urllib.parse import urlparse
from helpers import logger

log = logger.get_logger()
functools.partial(print, flush=True)


class Formula:
    def __init__(self, args, file, wordlist=None) -> None:
        self.args = args  # optional arguments stored here
        self.file = file
        self.wordlist = wordlist

    def parse_hostname(self, hostname):
        """Extract a domain and subdomains from the input"""
        url = urlparse(hostname)
        host = url.hostname or url.geturl()
        log.debug(f"{host=}")
        if host:
            _domain = re.search(r"[\w-]+[.](com|co.uk|ru|org|co|in|ai|sh|io)$", host)
            log.debug(f"{_domain=}")
            _subdomains = host[:_domain.start()] + host[_domain.end():]
            if not _subdomains:
                raise TypeError(f"No subdomains found for {host}")
            domain = _domain.group(0)
            log.debug(f"{domain=}")
            subdomains = _subdomains.split('.')[:-1]
            log.debug(f"{subdomains=}")
            return host, domain, subdomains
        else:
            raise TypeError(f"No host found for {host}")

    def pnk(self, subdomains):
        """Sequence of permutations wordlist on domain name"""
        log.debug("Permutation...")
        for p in itertools.permutations(subdomains):
            yield p

    def incrmt(self, subdomains):
        """Increment a digit found in subdomains.

        Yes:
            v1.subs1.subdomain -> v2.subs1.subdomain
            v1.subs1.subdomain -> v1.subs2.subdomain
        No:
            v1.subs01.subdomain -> v2.subs02.subdomain
            aws77.subs009.subdomain -> aws1.subs1.subdomain
            v001.subdomain01 -> v002.subdomain01
        """
        log.debug("Increment digits...")
        subdomains_string = ".".join(subdomains)
        is_matched = re.search('(?<!\d)\d(?!\d)', subdomains_string)  # TODO: v001.subdomain01 -> v002.subdomain01 ...
        if is_matched:
            for i in range(10):
                _s = subdomains_string.replace(
                    subdomains_string[is_matched.start(): is_matched.end()], str(i)
                )
                log.debug(_s)
                yield _s

    def run(self):
        """Compose functions on files with hostname lines"""
        for lines in self.file:
            for line in lines:
                log.debug(line.strip())
                try:
                    h, d, s = self.parse_hostname(line.strip())
                except TypeError:
                    pass  # ignore not hostname and lack of subdomains cases
                else:
                    if self.args.increment:
                        for i in self.incrmt(s):
                            print(i)
                            print(i + "." + d)
                    for p in self.pnk(s):
                        print(p)
                        s = ".".join(p)
                        print(s + "." + d)

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
    # optional argument
    parser.add_argument('-i', '--increment', action='store_true', help='additionally increment any \d{2} digits on subdomains')
    parser.add_argument('-w', '--wordlist', help='wordlist file to mixed with subdomains')  # TODO: implement then use with multiprocessing only
    # positional argument
    parser.add_argument(
        'file',
        nargs='*',
        type=argparse.FileType('r', encoding='UTF-8'),
        default=[sys.stdin],
        metavar='FILE',
        help='list of subdomains/hosts to process',
    )
    args = parser.parse_args()
    if not args.file:
        parser.print_help(sys.stderr)
        parser.exit(1)
    return args


def main(args):
    """Entry point for the programm"""
    if args.wordlist:
        log.debug(f"{args.wordlist}")

    frml = Formula(args, args.file, args.wordlist)
    frml.run()

if __name__ == '__main__':
    args = setup_argparse()
    main(args)
