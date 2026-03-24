
<details open>
  <summary>v1.0.1</summary>

```bash
python3 -m cProfile -s cumulative ./src/pnk/__main__.py -c < ./src/tests/list.txt
3205288 function calls (2946470 primitive calls) in 0.816 seconds

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     19/1    0.000    0.000    0.816    0.816 {built-in method builtins.exec}
        1    0.000    0.000    0.816    0.816 __main__.py:1(<module>)
        1    0.000    0.000    0.806    0.806 __main__.py:38(main)
        1    0.071    0.071    0.802    0.802 core.py:95(run)
395584/137343    0.294    0.000    0.539    0.000 core.py:87(join_product_tuples)
   928811    0.154    0.000    0.245    0.000 __init__.py:1467(debug)
   138221    0.152    0.000    0.152    0.000 {built-in method builtins.print}
   928811    0.092    0.000    0.092    0.000 __init__.py:1734(isEnabledFor)
   397220    0.022    0.000    0.022    0.000 {method 'join' of 'str' objects}
396815/396692    0.016    0.000    0.016    0.000 {built-in method builtins.len}
     29/4    0.000    0.000    0.012    0.003 <frozen importlib._bootstrap>:1167(_find_and_load)
     29/4    0.000    0.000    0.012    0.003 <frozen importlib._bootstrap>:1122(_find_and_load_unlocked)
     23/4    0.000    0.000    0.012    0.003 <frozen importlib._bootstrap>:666(_load_unlocked)
     17/4    0.000    0.000    0.012    0.003 <frozen importlib._bootstrap_external>:934(exec_module)
     57/8    0.000    0.000    0.011    0.001 <frozen importlib._bootstrap>:233(_call_with_frames_removed)
        1    0.000    0.000    0.008    0.008 core.py:1(<module>)
        2    0.000    0.000    0.004    0.002 {built-in method builtins.__import__}
      5/4    0.000    0.000    0.004    0.001 <frozen importlib._bootstrap>:1209(_handle_fromlist)
        1    0.000    0.000    0.004    0.004 logger.py:1(<module>)
        4    0.000    0.000    0.004    0.001 __init__.py:1(<module>)
       29    0.000    0.000    0.003    0.000 <frozen importlib._bootstrap>:1056(_find_spec)
       60    0.000    0.000    0.003    0.000 __init__.py:272(_compile)
        1    0.000    0.000    0.003    0.003 __main__.py:13(setup_argparse)
        1    0.000    0.000    0.003    0.003 pathlib.py:1(<module>)
       12    0.000    0.000    0.003    0.000 _compiler.py:738(compile)
  104/102    0.001    0.000    0.003    0.000 {built-in method builtins.__build_class__}
       26    0.000    0.000    0.003    0.000 <frozen importlib._bootstrap_external>:1496(find_spec)
       26    0.000    0.000    0.003    0.000 <frozen importlib._bootstrap_external>:1464(_get_spec)
        1    0.000    0.000    0.003    0.003 argparse.py:1730(__init__)
        5    0.000    0.000    0.003    0.001 argparse.py:1412(add_argument)
      139    0.001    0.000    0.003    0.000 <frozen importlib._bootstrap_external>:1604(find_spec)
       36    0.000    0.000    0.003    0.000 __init__.py:225(compile)
        3    0.000    0.000    0.003    0.001 argparse.py:2580(_get_formatter)
        3    0.000    0.000    0.003    0.001 argparse.py:164(__init__)
```
</details>
