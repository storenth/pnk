# Profiling
1. cProfile: use this built-in tool to understand which functions in your code take the longest to run.
The `-s` cumulative flag tells cProfile to sort by cumulative time spent inside each function; this gives us a view into the slowest parts of a section of code.
```python
python3 -m cProfile -s cumulative ./src/pnk/__main__.py  -i < src/tests/one.txt

18798 function calls (18223 primitive calls) in 0.016 seconds
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    0.001    0.001    core.py:81(run)
...
```
2. A timing decorator: use these techniques to understand the behavior of statements and functions.
```python
@timefn
def run():
    pass

@timefn: run took 0.0010941028594970703 seconds
```