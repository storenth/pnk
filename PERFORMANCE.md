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
3. Cartesian product
```
python3 -m cProfile -s calls ./src/pnk/__main__.py  -c < src/tests/one.txt
@timefn: run took 0.0016446113586425781 seconds
         17880 function calls (17305 primitive calls) in 0.017 seconds
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1437    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
1180/1059    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1099    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
     1069    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
      888    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
      708    0.000    0.000    0.000    0.000 _parser.py:231(__next)
      690    0.000    0.000    0.000    0.000 _parser.py:162(__getitem__)
      575    0.000    0.000    0.000    0.000 _parser.py:252(get)
      540    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:244(_verbose_message)
      531    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:126(_path_join)
      531    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:128(<listcomp>)
      303    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      296    0.000    0.000    0.000    0.000 {built-in method builtins.min}
      268    0.000    0.000    0.000    0.000 _parser.py:247(match)
      217    0.000    0.000    0.000    0.000 _parser.py:158(__len__)
```
