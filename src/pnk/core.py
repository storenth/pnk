#!/usr/bin/python3
import itertools
import functools
import pathlib
import re

from urllib.parse import urlparse
from pnk.helpers import logger

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
            log.debug(f"No domain found for {host}")
            if not _domain:
                raise TypeError(f"No subdomains found for {host}")
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
        """Sequence of permutations on subdomains"""
        log.debug("Permutation...")
        for p in itertools.permutations(subdomains):
            yield p

    def incrmt(self, subdomain):
        """Increment a digit found in subdomain"""
        log.debug("Increment digits...")
        pattern = re.compile('(?<!\d)\d{1,2}(?!\d)')
        matches = pattern.finditer(subdomain)
        for match in matches:
            log.debug(match)
            if match:
                for i in range(10 if len(match.group()) < 2 else 100):
                    _s = (
                        subdomain[:match.start()]
                        + str(i).zfill(len(subdomain[match.start(): match.end()]))
                        + subdomain[match.end():]
                    )
                    log.debug(_s)
                    yield _s
                # check for duplicated digits to increment it both
                if match.group() in subdomain[:match.start()]:
                    log.debug("duplicated digits")
                    log.debug(match)
                    for i in range(10 if len(match.group()) < 2 else 100):
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
        """TODO: see https://github.com/storenth/pnk/issues/1
        Read the wordlist and returns lines generator
        """
        wordlist = self.args.wordlist if self.args.wordlist else pathlib.Path(__file__).parent / 'wordlist.txt'
        with open(wordlist, 'r', encoding='UTF-8') as file:
            for line in file:
                yield line.strip()
