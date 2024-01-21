# pnk
Produce a new combination of subdomains - generates permutations P(n,k).

## Make it work
- [x] swap subs themselves: web.test.domain.com -> test.web.domain.com
- [x] increase/decrease digits on subs with numbers: test1.domain.com -> test2.domain.com

## Make it right
1. `stdin`: reads standard input. This is useful for capturing a pipeline’s contents at an intermediate stage of processing.
2. `stdout`: supports standard output.
3. Works with the next arguments:
```
usage: pnk.py [-h] [-i | -c] [-v] [FILE ...]

Generates a new subdomains on provided input

positional arguments:
  FILE             list of subdomains/hosts to process

optional arguments:
  -h, --help       show this help message and exit
  -i, --increment  increment any one or two digits on subdomains
  -c, --cartesian  increment digits on subdomains creating Cartesian product
  -v, --version    show program's version number and exit
```
```bash
$ cat subs1.txt subs2.txt | pnk
```

## Make it fast
WIP: but for now, to turn this single process script into multiprocess use [interlace](https://github.com/codingo/Interlace)


# Features
Permutations:
```bash
echo "aws3-3.s11.env2.tesla.com" | pnk
aws3-3.s11.env2.tesla.com
aws3-3.env2.s11.tesla.com
s11.aws3-3.env2.tesla.com
s11.env2.aws3-3.tesla.com
env2.aws3-3.s11.tesla.com
env2.s11.aws3-3.tesla.com
```
With incrementation option:
```bash
echo "aws3-3.s11.env2.tesla.com" | pnk -i
aws0-3.s11.env2.tesla.com
aws1-3.s11.env2.tesla.com
aws2-3.s11.env2.tesla.com
...
aws8-8.s11.env2.tesla.com
aws9-9.s11.env2.tesla.com
...
```

## Install & Usage
PyPi:
```bash
pip3 install --no-deps pnk
```
From the source code:
```bash
$ cat subs1.txt subs2.txt | ./src/pnk/__main__.py
```

# Constraints
### Feature request
See the open [issue](https://github.com/storenth/pnk/issues/1#issue-2080221058) for the following feature requests:
- [ ] replace each subs with word in wordlist: v2.test.domain.com -> demo.test.domain.com
- [ ] prepend/append word by creating new subs: test.domain.com -> demo.test.domain.com, test.demo.domain.com
### Limitations
1. Does't handle incremet option in the following cases: more then two digits:
```
v123.tesla.com -> v123.tesla.com
aws.1002030v.amazon.com -> aws.1002030v.amazon.com
```
2. Does not ships with DNS resolver, use [massdns](https://github.com/blechschmidt/massdns)
```bash
$ pnk < list.txt | massdns -
```
3. Possible out of memory issues when redirecting `stdout` to a file, please read the [Wiki](https://github.com/storenth/pnk/wiki)
## TODO
1. Combinations of incrementations (cartesian product of all digits found in each sub): 
```
5io5.33.ya.ru -> 0io0.00.ya.ru .. 9io9.99.ya.ru
```
How it works now:
```
5io5.33.ya.ru -> 0io5.00.ya.ru .. 9io5.99.ya.ru .. 5io0.00.ya.ru .. 5io9.99.ya.ru
```