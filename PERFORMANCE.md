# Profiling
1. cProfile: use this built-in tool to understand which functions in your code take the longest to run.
```python
python3 -m cProfile -s cumulative ./src/pnk/__main__.py  -i < tests/list.txt

30588 function calls (30013 primitive calls) in 0.019 seconds
...
```
2. A timing decorator: use these techniques to understand the behavior of statements and functions.
```python
@timefn
def run():
    pass

@timefn: run took 0.00506901741027832 seconds
```
