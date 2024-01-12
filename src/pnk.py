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

    def incrmt(self, subdomain):
        """Increment a digit found in subdomain"""
        log.debug("Increment digits...")
        pattern = re.compile('(?<!\d)\d{1,2}(?!\d)')
        match = pattern.search(subdomain)
        log.debug(match)
        if match:
            for i in range(10 if int(match.group()) < 10 else 100):
                _s = subdomain.replace(
                    subdomain[match.start(): match.end()],
                    str(i).zfill(len(subdomain[match.start(): match.end()])),
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
                        _s = s.copy()
                        for index, j in enumerate(s):
                            for i in self.incrmt(j):
                                _s[index] = i
                                print(".".join(_s) + "." + d)
                            _s[index] = j
                    for p in self.pnk(s):
                        print(".".join(p) + "." + d)

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
    parser.add_argument('-i', '--increment', action='store_true', help='additionally increment any one or two digits on subdomains')
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
