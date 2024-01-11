# pnk
Комбинация доменов и слов на основе размещений без повторений P(n,k)

# Make it work
- [ ] replace each subs with each word: test.domain.com -> demo.domain.com
- [x] swap subs itself: web.test.domain.com -> test.web.domain.com
- [ ] insert word by creating new subs: test.domain.com -> demo.test.domain.com, test.demo.domain.com
- [x] increase/decrease subs with numbers: test1.domain.com -> test2.domain.com

# Make it right
1. `stdin`: reads standard input. This is useful for capturing a pipeline’s contents at an intermediate stage of processing.
2. `stdout`: supports standard output.
3. Works with the next arguments:
```
usage: pnk.py [-h] [-i] [-w WORDLIST] [FILE ...]

Set CLI args pnk works with

positional arguments:
  FILE                  list of subdomains/hosts to process

optional arguments:
  -h, --help            show this help message and exit
  -i, --increment       additionally increment any \d{2} digits on subdomains
  -w WORDLIST, --wordlist WORDLIST
                        wordlist file to mixed with subdomains
```
```bash
$ cat subs1.txt subs2.txt | ./pnk.py
```

# Make it fast
WIP. But, to turn this single process script into multiprocessing use [interlace](https://github.com/codingo/Interlace)


## Limitations
Works unexpectedly:
```bash
v5-5.test.io -> v0-0.test.io .. v9-9.test.io
5io5.33.ya.ru -> 0io0.33.ya.ru .. 5io5.09.ya.ru
777v.host.ai -> 777v.host.ai
```