# pnk
Produce a combination of subdomains without repetitions - generates permutations P(n,k)

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
  -i, --increment       additionally increment digits on subdomains
  -w WORDLIST, --wordlist WORDLIST
                        wordlist file to mixed with subdomains
```
```bash
$ cat subs1.txt subs2.txt | ./pnk.py
```

# Make it fast
WIP: but, to turn this single process script into multiprocess use [interlace](https://github.com/codingo/Interlace)


## Examples
Permutations:
```bash
echo "aws3.s11.env2.tesla.com" | ./src/pnk.py
aws3.s11.env2.tesla.com
aws3.env2.s11.tesla.com
s11.aws3.env2.tesla.com
s11.env2.aws3.tesla.com
env2.aws3.s11.tesla.com
env2.s11.aws3.tesla.com
```
With incrementation option
```bash
echo "aws3.s11.env2.tesla.com" | ./src/pnk.py -i
aws0.s11.env2.tesla.com
aws1.s11.env2.tesla.com
aws2.s11.env2.tesla.com
aws3.s11.env2.tesla.com
aws4.s11.env2.tesla.com
aws5.s11.env2.tesla.com
aws6.s11.env2.tesla.com
aws7.s11.env2.tesla.com
aws8.s11.env2.tesla.com
aws9.s11.env2.tesla.com
aws3.s00.env2.tesla.com
aws3.s01.env2.tesla.com
aws3.s02.env2.tesla.com
aws3.s03.env2.tesla.com
...
```

## Limitations
Unexpectedly works with incremet option in the following cases:
```bash
v5-5.test.io -> v0-0.test.io .. v9-9.test.io
5io5.33.ya.ru -> 0io0.33.ya.ru .. 5io5.09.ya.ru
777v.host.ai -> 777v.host.ai
```