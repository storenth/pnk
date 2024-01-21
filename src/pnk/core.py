#!/usr/bin/python3
import functools
import itertools
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
        log.debug(f"{url=}")
        host = url.hostname or url.geturl()
        log.debug(f"{host=}")
        if host:
            _domain = re.search(
                r"[\w-]+[.](com|co.uk|ru|org|co|in|ai|sh|io|jp|com.cn|cn|cz|de|net|fr|it|au|ca|ir|br|com.br|co.kr|gov|uk|kz|tech|shop|moscow|store|me)$",
                host,
            )
            log.debug(f"{_domain=}")
            if not _domain:
                raise TypeError(f"No domain found for {host}")
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
        log.debug(f"Increment digits on {subdomain=}")
        pattern = re.compile('(?<!\d)\d{1,2}(?!\d)')
        counter = 0
        for match in pattern.finditer(subdomain):
            counter = counter + 1
            log.debug(match)
            if match:
                m_start = match.start()
                m_end = match.end()
                range_count = 10 if len(match.group()) < 2 else 100
                for i in range(range_count):
                    _s = (
                        subdomain[:m_start]
                        + str(i).zfill(len(subdomain[m_start: m_end]))
                        + subdomain[m_end:]
                    )
                    log.debug(_s)
                    yield _s
                # check for duplicated digits to increment it both
                if match.group() in subdomain[:m_start] and match.group() not in subdomain[m_end:]:
                    log.debug("duplicated digits")
                    log.debug(match)
                    for i in range(range_count):
                        _sd = subdomain.replace(
                            subdomain[m_start: m_end],
                            str(i).zfill(len(subdomain[m_start: m_end])),
                        )
                        log.debug(_sd)
                        yield _sd
        if counter == 0:
            log.debug("No digits found!")
            yield subdomain

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
                    if self.args.cartesian:
                        for p in itertools.product(*map(self.incrmt, s)):
                            print(".".join(p) + "." + d)
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
