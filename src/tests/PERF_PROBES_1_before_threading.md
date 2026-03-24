
<details open>
  <summary>v3.0.0</summary>

```bash
/src/pnk/__main__.py ./src/tests/big_list.txt | wc -l
4133000

python3 -m cProfile -s cumulative ./src/pnk/__main__.py < ./src/tests/big_list.txt

34044492 function calls (34043930 primitive calls) in 13.163 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     19/1    0.000    0.000   13.191   13.191 {built-in method builtins.exec}
        1    0.000    0.000   13.191   13.191 __main__.py:1(<module>)
        1    0.000    0.000   13.179   13.179 __main__.py:70(main)
        1    2.895    2.895   13.172   13.172 core.py:199(run)
  4133000    5.068    0.000    5.068    0.000 {built-in method builtins.print}
   139798    0.505    0.000    2.492    0.000 core.py:20(parse_hostname)
  8266632    1.400    0.000    1.400    0.000 {method 'join' of 'str' objects}
  5251384    0.727    0.000    1.051    0.000 __init__.py:1517(debug)
   139798    0.166    0.000    0.869    0.000 parse.py:374(urlparse)
   139798    0.321    0.000    0.592    0.000 parse.py:452(urlsplit)
  4272798    0.406    0.000    0.435    0.000 core.py:51(pnk)
   139798    0.027    0.000    0.355    0.000 parse.py:338(geturl)
   139798    0.089    0.000    0.327    0.000 parse.py:509(urlunparse)
  5251384    0.324    0.000    0.324    0.000 __init__.py:1790(isEnabledFor)
   139798    0.050    0.000    0.266    0.000 __init__.py:174(search)
   559192    0.200    0.000    0.258    0.000 parse.py:119(_coerce_args)
   139798    0.029    0.000    0.159    0.000 parse.py:164(hostname)
   139800    0.155    0.000    0.155    0.000 {method 'search' of 're.Pattern' objects}
   139798    0.063    0.000    0.147    0.000 parse.py:520(urlunsplit)
   139798    0.079    0.000    0.130    0.000 parse.py:205(_hostinfo)
   838809    0.088    0.000    0.088    0.000 {method 'replace' of 'str' objects}
   979996    0.081    0.000    0.081    0.000 {built-in method builtins.isinstance}
   139798    0.074    0.000    0.074    0.000 __init__.py:466(__repr__)
   139822    0.038    0.000    0.062    0.000 __init__.py:280(_compile)
   419394    0.056    0.000    0.056    0.000 {method 'strip' of 'str' objects}
   139798    0.026    0.000    0.046    0.000 <string>:1(<lambda>)
   279633    0.042    0.000    0.042    0.000 {built-in method __new__ of type object at 0x105cfca50}
   559192    0.037    0.000    0.037    0.000 parse.py:108(_noop)
   279630    0.031    0.000    0.031    0.000 {method 'partition' of 'str' objects}
   139822    0.030    0.000    0.030    0.000 {method 'find' of 'str' objects}
   139922    0.028    0.000    0.028    0.000 {method 'split' of 'str' objects}
   139798    0.022    0.000    0.022    0.000 {method 'group' of 're.Match' objects}
   140001    0.020    0.000    0.020    0.000 {method 'rpartition' of 'str' objects}
   139806    0.020    0.000    0.020    0.000 {method 'lstrip' of 'str' objects}
   139798    0.018    0.000    0.018    0.000 {method 'start' of 're.Match' objects}
     31/4    0.000    0.000    0.018    0.004 <frozen importlib._bootstrap>:1349(_find_and_load)
     31/4    0.000    0.000    0.018    0.004 <frozen importlib._bootstrap>:1304(_find_and_load_unlocked)
     24/4    0.000    0.000    0.017    0.004 <frozen importlib._bootstrap>:911(_load_unlocked)
     17/4    0.000    0.000    0.017    0.004 <frozen importlib._bootstrap_external>:989(exec_module)
   139798    0.016    0.000    0.016    0.000 {method 'end' of 're.Match' objects}
     61/8    0.000    0.000    0.016    0.002 <frozen importlib._bootstrap>:480(_call_with_frames_removed)
   139798    0.011    0.000    0.011    0.000 parse.py:421(_checknetloc)
        1    0.000    0.000    0.010    0.010 core.py:1(<module>)
        1    0.000    0.000    0.007    0.007 __main__.py:13(setup_argparse)
        1    0.000    0.000    0.006    0.006 argparse.py:1764(__init__)
        9    0.000    0.000    0.006    0.001 argparse.py:1446(add_argument)
        7    0.000    0.000    0.006    0.001 argparse.py:2622(_get_formatter)
        7    0.000    0.000    0.006    0.001 argparse.py:164(__init__)
       17    0.000    0.000    0.006    0.000 <frozen importlib._bootstrap_external>:1062(get_code)
        1    0.000    0.000    0.005    0.005 shutil.py:1(<module>)
       24    0.000    0.000    0.005    0.000 <frozen importlib._bootstrap>:806(module_from_spec)
        1    0.000    0.000    0.005    0.005 pathlib.py:1(<module>)
        4    0.000    0.000    0.005    0.001 <frozen importlib._bootstrap_external>:1287(create_module)
        4    0.005    0.001    0.005    0.001 {built-in method _imp.create_dynamic}
        2    0.000    0.000    0.004    0.002 {built-in method builtins.__import__}
      4/3    0.000    0.000    0.004    0.001 <frozen importlib._bootstrap>:1390(_handle_fromlist)
        1    0.000    0.000    0.004    0.004 logger.py:1(<module>)
       17    0.000    0.000    0.004    0.000 <frozen importlib._bootstrap_external>:1183(get_data)
        1    0.000    0.000    0.003    0.003 parse.py:1(<module>)
       17    0.003    0.000    0.003    0.000 {method 'read' of '_io.BufferedReader' objects}
        4    0.000    0.000    0.003    0.001 __init__.py:1(<module>)
  107/105    0.001    0.000    0.003    0.000 {built-in method builtins.__build_class__}
       31    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:1240(_find_spec)
       10    0.000    0.000    0.002    0.000 _compiler.py:740(compile)
       17    0.001    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:751(_compile_bytecode)
       28    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:1520(find_spec)
       28    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:1491(_get_spec)
       23    0.000    0.000    0.002    0.000 __init__.py:226(compile)
        1    0.000    0.000    0.002    0.002 lzma.py:1(<module>)
        1    0.000    0.000    0.002    0.002 bz2.py:1(<module>)
       17    0.001    0.000    0.001    0.000 {built-in method marshal.loads}
      114    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1593(find_spec)
      289    0.001    0.000    0.001    0.000 <frozen codecs>:319(decode)
       10    0.000    0.000    0.001    0.000 _parser.py:969(parse)
    29/10    0.000    0.000    0.001    0.000 _parser.py:452(_parse_sub)
    70/11    0.000    0.000    0.001    0.000 _parser.py:512(_parse)
       10    0.000    0.000    0.001    0.000 _compiler.py:573(_code)
        1    0.000    0.000    0.001    0.001 ipaddress.py:1(<module>)
   113/10    0.000    0.000    0.001    0.000 _compiler.py:37(_compile)
      289    0.001    0.000    0.001    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.001    0.001 __init__.py:469(StrFormatStyle)
        1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:1171(exec_module)
        1    0.000    0.000    0.001    0.001 <frozen ntpath>:1(<module>)
        1    0.000    0.000    0.001    0.001 string.py:1(<module>)
      576    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:126(_path_join)
        1    0.000    0.000    0.000    0.000 string.py:69(__init_subclass__)
       17    0.000    0.000    0.000    0.000 {built-in method _io.open_code}
        5    0.000    0.000    0.000    0.000 __init__.py:355(namedtuple)
      174    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:140(_path_stat)
      190    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        1    0.000    0.000    0.000    0.000 __init__.py:436(PercentStyle)
        1    0.000    0.000    0.000    0.000 ipaddress.py:2317(_IPv6Constants)
       27    0.000    0.000    0.000    0.000 _compiler.py:243(_optimize_charset)
       34    0.000    0.000    0.000    0.000 ipaddress.py:2241(__init__)
      137    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1469(_path_importer_cache)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(__enter__)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1456(_path_hooks)
        1    0.000    0.000    0.000    0.000 argparse.py:1(<module>)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1685(path_hook_for_FileFinder)
        1    0.000    0.000    0.000    0.000 ipaddress.py:1569(_IPv4Constants)
       21    0.000    0.000    0.000    0.000 ipaddress.py:1502(__init__)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1567(__init__)
        4    0.000    0.000    0.000    0.000 gettext.py:616(gettext)
        4    0.000    0.000    0.000    0.000 gettext.py:578(dgettext)
        4    0.000    0.000    0.000    0.000 gettext.py:519(translation)
       26    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:185(_path_abspath)
        2    0.000    0.000    0.000    0.000 __init__.py:592(__init__)
        4    0.000    0.000    0.000    0.000 gettext.py:479(find)
        2    0.000    0.000    0.000    0.000 __init__.py:450(validate)
        2    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
       24    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:733(_init_module_attrs)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:304(acquire)
      676    0.000    0.000    0.000    0.000 _parser.py:168(__getitem__)
       34    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:482(cache_from_source)
       50    0.000    0.000    0.000    0.000 ipaddress.py:1920(__init__)
        5    0.000    0.000    0.000    0.000 {built-in method builtins.eval}
        4    0.000    0.000    0.000    0.000 argparse.py:1364(__init__)
1597/1481    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      565    0.000    0.000    0.000    0.000 _parser.py:261(get)
   129/26    0.000    0.000    0.000    0.000 _parser.py:178(getwidth)
        1    0.000    0.000    0.000    0.000 traceback.py:1(<module>)
       31    0.000    0.000    0.000    0.000 ipaddress.py:1286(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:1895(parse_args)
        1    0.000    0.000    0.000    0.000 argparse.py:1902(parse_known_args)
     1492    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       38    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:632(cached)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:611(_get_cached)
        1    0.000    0.000    0.000    0.000 argparse.py:1940(_parse_known_args)
       33    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:159(_path_isfile)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1644(_fill_cache)
     1187    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       38    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:150(_path_is_mode_type)
       22    0.000    0.000    0.000    0.000 ipaddress.py:1187(_ip_int_from_string)
       16    0.000    0.000    0.000    0.000 _parser.py:98(closegroup)
       34    0.000    0.000    0.000    0.000 ipaddress.py:1651(_ip_int_from_string)
       10    0.000    0.000    0.000    0.000 _compiler.py:511(_compile_info)
        1    0.000    0.000    0.000    0.000 argparse.py:2098(consume_positionals)
       73    0.000    0.000    0.000    0.000 {built-in method from_bytes}
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:162(__enter__)
       55    0.000    0.000    0.000    0.000 ipaddress.py:533(_split_addr_prefix)
        5    0.000    0.000    0.000    0.000 {built-in method posix.listdir}
        5    0.000    0.000    0.000    0.000 <frozen abc>:105(__new__)
        1    0.000    0.000    0.000    0.000 argparse.py:2251(_match_arguments_partial)
        1    0.000    0.000    0.000    0.000 __init__.py:164(match)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:420(__exit__)
        8    0.000    0.000    0.000    0.000 gettext.py:224(_expand_lang)
      690    0.000    0.000    0.000    0.000 _parser.py:240(__next)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:426(_get_module_lock)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1588(_get_spec)
       88    0.000    0.000    0.000    0.000 ipaddress.py:1213(_parse_octet)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:124(setdefault)
       20    0.000    0.000    0.000    0.000 enum.py:1562(__and__)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:372(release)
       31    0.000    0.000    0.000    0.000 __init__.py:102(find_spec)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1295(exec_module)
        1    0.000    0.000    0.000    0.000 argparse.py:1150(__init__)
       34    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:132(_path_split)
        4    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
       18    0.000    0.000    0.000    0.000 <frozen posixpath>:71(join)
      587    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:491(_verbose_message)
      189    0.000    0.000    0.000    0.000 _parser.py:176(append)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:802(spec_from_file_location)
       34    0.000    0.000    0.000    0.000 ipaddress.py:1631(_make_netmask)
        7    0.000    0.000    0.000    0.000 shutil.py:1422(get_terminal_size)
        8    0.000    0.000    0.000    0.000 locale.py:381(normalize)
       93    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       10    0.000    0.000    0.000    0.000 functools.py:518(decorating_function)
      283    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       31    0.000    0.000    0.000    0.000 <frozen os>:709(__getitem__)
       11    0.000    0.000    0.000    0.000 functools.py:35(update_wrapper)
      209    0.000    0.000    0.000    0.000 _parser.py:164(__len__)
       17    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1202(path_stats)
      275    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        3    0.000    0.000    0.000    0.000 argparse.py:1674(__init__)
        1    0.000    0.000    0.000    0.000 _compression.py:1(<module>)
       55    0.000    0.000    0.000    0.000 ipaddress.py:156(_split_optional_netmask)
      254    0.000    0.000    0.000    0.000 _parser.py:256(match)
       21    0.000    0.000    0.000    0.000 enum.py:726(__call__)
       17    0.000    0.000    0.000    0.000 <frozen _collections_abc>:804(get)
       35    0.000    0.000    0.000    0.000 _compiler.py:398(_simple)
      119    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1226(__exit__)
       29    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1128(find_spec)
        9    0.000    0.000    0.000    0.000 argparse.py:1875(_add_action)
       21    0.000    0.000    0.000    0.000 ipaddress.py:1161(_make_netmask)
       17    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:666(_classify_pyc)
       51    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_unpack_uint32)
       17    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:699(_validate_timestamp_pyc)
       46    0.000    0.000    0.000    0.000 ipaddress.py:1755(_parse_hextet)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 argparse.py:1497(add_argument_group)
       16    0.000    0.000    0.000    0.000 <frozen genericpath>:16(exists)
        4    0.000    0.000    0.000    0.000 locale.py:347(_replace_encoding)
      194    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:445(cb)
      119    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1222(__enter__)
        9    0.000    0.000    0.000    0.000 argparse.py:1696(_add_action)
       63    0.000    0.000    0.000    0.000 enum.py:1544(_get_value)
       17    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
       21    0.000    0.000    0.000    0.000 enum.py:1129(__new__)
       27    0.000    0.000    0.000    0.000 _compiler.py:216(_compile_charset)
        6    0.000    0.000    0.000    0.000 _compiler.py:386(_mk_bitmap)
        1    0.000    0.000    0.000    0.000 enum.py:1551(__or__)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:982(find_spec)
        8    0.000    0.000    0.000    0.000 argparse.py:1587(_get_optional_kwargs)
      101    0.000    0.000    0.000    0.000 _parser.py:293(tell)
       29    0.000    0.000    0.000    0.000 _parser.py:372(_escape)
        5    0.000    0.000    0.000    0.000 <frozen zipimport>:64(__init__)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:74(__new__)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:232(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:928(__init__)
      112    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        9    0.000    0.000    0.000    0.000 argparse.py:1507(_add_action)
       25    0.000    0.000    0.000    0.000 ipaddress.py:474(_prefix_from_prefix_string)
       31    0.000    0.000    0.000    0.000 <frozen os>:791(encode)
       16    0.000    0.000    0.000    0.000 _parser.py:86(opengroup)
      114    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:67(_relax_case)
       68    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:134(<genexpr>)
        4    0.000    0.000    0.000    0.000 __init__.py:43(normalize_encoding)
        1    0.000    0.000    0.000    0.000 <frozen posixpath>:408(abspath)
      181    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
       49    0.000    0.000    0.000    0.000 argparse.py:1417(register)
       36    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       86    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
      181    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:82(remove)
        1    0.000    0.000    0.000    0.000 argparse.py:1502(add_mutually_exclusive_group)
        7    0.000    0.000    0.000    0.000 argparse.py:605(_format_args)
        1    0.000    0.000    0.000    0.000 enum.py:1414(_missing_)
       75    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1293(__init__)
       85    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        1    0.000    0.000    0.000    0.000 ipaddress.py:1280(IPv4Address)
        1    0.000    0.000    0.000    0.000 argparse.py:1716(__init__)
       15    0.000    0.000    0.000    0.000 _parser.py:449(_uniq)
       34    0.000    0.000    0.000    0.000 ipaddress.py:1885(_split_scope_id)
        2    0.000    0.000    0.000    0.000 __init__.py:2149(getLogger)
      174    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
      129    0.000    0.000    0.000    0.000 {method 'isascii' of 'str' objects}
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:79(__init__)
       75    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       26    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:180(_path_isabs)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:173(__exit__)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:164(_path_isdir)
       11    0.000    0.000    0.000    0.000 functools.py:479(lru_cache)
        2    0.000    0.000    0.000    0.000 functools.py:188(total_ordering)
      9/8    0.000    0.000    0.000    0.000 _compiler.py:436(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 fnmatch.py:1(<module>)
       27    0.000    0.000    0.000    0.000 {built-in method builtins.locals}
      114    0.000    0.000    0.000    0.000 _parser.py:113(__init__)
      113    0.000    0.000    0.000    0.000 {method 'isdigit' of 'str' objects}
       17    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:643(_check_name_wrapper)
        1    0.000    0.000    0.000    0.000 argparse.py:157(HelpFormatter)
       52    0.000    0.000    0.000    0.000 _parser.py:83(groups)
       27    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        5    0.000    0.000    0.000    0.000 {built-in method _abc._abc_init}
       31    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        7    0.000    0.000    0.000    0.000 {built-in method posix.get_terminal_size}
       24    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:645(parent)
        2    0.000    0.000    0.000    0.000 __init__.py:1377(getLogger)
       62    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 ipaddress.py:1914(IPv6Address)
        1    0.000    0.000    0.000    0.000 argparse.py:1176(_SubParsersAction)
        9    0.000    0.000    0.000    0.000 argparse.py:1621(_pop_action_class)
       10    0.000    0.000    0.000    0.000 _parser.py:231(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:958(createLock)
        1    0.000    0.000    0.000    0.000 pathlib.py:292(PurePath)
        2    0.000    0.000    0.000    0.000 _compiler.py:391(_bytes_to_codes)
       51    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       18    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:48(_new_module)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:989(create_module)
      110    0.000    0.000    0.000    0.000 ipaddress.py:574(__int__)
        1    0.000    0.000    0.000    0.000 ipaddress.py:671(_BaseNetwork)
        2    0.000    0.000    0.000    0.000 argparse.py:1721(_add_action)
        3    0.000    0.000    0.000    0.000 enum.py:1404(_iter_member_by_def_)
        1    0.000    0.000    0.000    0.000 __init__.py:1126(__init__)
        9    0.000    0.000    0.000    0.000 argparse.py:845(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:662(spec_from_loader)
       78    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        4    0.000    0.000    0.000    0.000 argparse.py:1009(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:1987(take_action)
       37    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
       19    0.000    0.000    0.000    0.000 argparse.py:1421(_registry_get)
        4    0.000    0.000    0.000    0.000 _parser.py:274(getuntil)
       10    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
       46    0.000    0.000    0.000    0.000 {method 'issuperset' of 'frozenset' objects}
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:599(__init__)
       62    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
       29    0.000    0.000    0.000    0.000 {built-in method _imp.find_frozen}
       61    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
       21    0.000    0.000    0.000    0.000 <frozen posixpath>:41(_get_sep)
        1    0.000    0.000    0.000    0.000 ipaddress.py:1611(_BaseV6)
        2    0.000    0.000    0.000    0.000 __init__.py:892(_addHandlerRef)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 pathlib.py:824(Path)
       36    0.000    0.000    0.000    0.000 _parser.py:172(__setitem__)
       43    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.000    0.000 weakref.py:104(__init__)
       25    0.000    0.000    0.000    0.000 ipaddress.py:431(_ip_int_from_prefix)
        2    0.000    0.000    0.000    0.000 __init__.py:262(_register_at_fork_reinit_lock)
       17    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 functools.py:651(cache)
        2    0.000    0.000    0.000    0.000 {built-in method _imp.create_builtin}
       20    0.000    0.000    0.000    0.000 _compiler.py:570(isstring)
        1    0.000    0.000    0.000    0.000 <frozen abc>:110(register)
       35    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        9    0.000    0.000    0.000    0.000 __init__.py:234(_acquireLock)
        1    0.000    0.000    0.000    0.000 fnmatch.py:74(translate)
       15    0.000    0.000    0.000    0.000 {built-in method fromkeys}
       31    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
       31    0.000    0.000    0.000    0.000 {method 'encode' of 'str' objects}
        4    0.000    0.000    0.000    0.000 argparse.py:986(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:1510(setLevel)
       32    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:1497(__init__)
        1    0.000    0.000    0.000    0.000 pathlib.py:263(_PathParents)
        1    0.000    0.000    0.000    0.000 ipaddress.py:383(_IPAddressBase)
        1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_register}
        1    0.000    0.000    0.000    0.000 ipaddress.py:1487(IPv4Network)
       25    0.000    0.000    0.000    0.000 {built-in method sys.intern}
       29    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        9    0.000    0.000    0.000    0.000 __init__.py:243(_releaseLock)
        3    0.000    0.000    0.000    0.000 argparse.py:951(__init__)
       10    0.000    0.000    0.000    0.000 enum.py:202(__get__)
        1    0.000    0.000    0.000    0.000 {built-in method time.time}
       10    0.000    0.000    0.000    0.000 _parser.py:953(fix_flags)
        3    0.000    0.000    0.000    0.000 enum.py:1394(_iter_member_by_value_)
       25    0.000    0.000    0.000    0.000 ipaddress.py:415(_check_int_address)
       31    0.000    0.000    0.000    0.000 {built-in method _weakref._remove_dead_weakref}
        1    0.000    0.000    0.000    0.000 __init__.py:1878(LoggerAdapter)
        1    0.000    0.000    0.000    0.000 <frozen abc>:121(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 __init__.py:1482(Logger)
        4    0.000    0.000    0.000    0.000 argparse.py:1625(_get_handler)
        1    0.000    0.000    0.000    0.000 parse.py:152(_NetlocResultMixinBase)
        1    0.000    0.000    0.000    0.000 __init__.py:1465(_clear_cache)
       40    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1573(<genexpr>)
        1    0.000    0.000    0.000    0.000 logger.py:34(get_logger)
       25    0.000    0.000    0.000    0.000 __init__.py:429(<genexpr>)
        1    0.000    0.000    0.000    0.000 __init__.py:1867(__init__)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:412(__init__)
       20    0.000    0.000    0.000    0.000 _compiler.py:31(_combine_flags)
        3    0.000    0.000    0.000    0.000 _compiler.py:407(_generate_overlap_table)
       23    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       25    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:158(__init__)
        7    0.000    0.000    0.000    0.000 argparse.py:598(format)
        1    0.000    0.000    0.000    0.000 ipaddress.py:1139(_BaseV4)
        1    0.000    0.000    0.000    0.000 __init__.py:1117(StreamHandler)
        5    0.000    0.000    0.000    0.000 _compiler.py:467(_get_charset_prefix)
        2    0.000    0.000    0.000    0.000 {method 'tolist' of 'memoryview' objects}
        4    0.000    0.000    0.000    0.000 <frozen os>:795(decode)
       36    0.000    0.000    0.000    0.000 {built-in method _sre.unicode_iscased}
        2    0.000    0.000    0.000    0.000 _parser.py:893(_parse_flags)
        9    0.000    0.000    0.000    0.000 argparse.py:1634(_check_conflict)
        1    0.000    0.000    0.000    0.000 ipaddress.py:2150(IPv6Interface)
        1    0.000    0.000    0.000    0.000 argparse.py:1742(ArgumentParser)
        1    0.000    0.000    0.000    0.000 <frozen posixpath>:179(dirname)
        1    0.000    0.000    0.000    0.000 traceback.py:374(StackSummary)
        1    0.000    0.000    0.000    0.000 __init__.py:1353(Manager)
        2    0.000    0.000    0.000    0.000 __init__.py:255(escape)
       40    0.000    0.000    0.000    0.000 {built-in method _sre.unicode_tolower}
        1    0.000    0.000    0.000    0.000 bz2.py:26(BZ2File)
        1    0.000    0.000    0.000    0.000 argparse.py:2499(_get_values)
        1    0.000    0.000    0.000    0.000 argparse.py:1131(__init__)
        1    0.000    0.000    0.000    0.000 string.py:188(Formatter)
       20    0.000    0.000    0.000    0.000 {method 'isalnum' of 'str' objects}
       24    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:653(has_location)
       17    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:997(exec_module)
        7    0.000    0.000    0.000    0.000 {method 'fileno' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 ipaddress.py:1420(IPv4Interface)
        1    0.000    0.000    0.000    0.000 traceback.py:679(TracebackException)
        6    0.000    0.000    0.000    0.000 {method 'translate' of 'bytearray' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:919(Handler)
        1    0.000    0.000    0.000    0.000 lzma.py:38(LZMAFile)
       27    0.000    0.000    0.000    0.000 __init__.py:109(<lambda>)
       11    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
       10    0.000    0.000    0.000    0.000 _parser.py:77(__init__)
        1    0.000    0.000    0.000    0.000 weakref.py:289(update)
       21    0.000    0.000    0.000    0.000 {built-in method builtins.callable}
       14    0.000    0.000    0.000    0.000 _compiler.py:428(_get_iscased)
        2    0.000    0.000    0.000    0.000 parse.py:825(__getattr__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1103(_resolve_filename)
        6    0.000    0.000    0.000    0.000 __init__.py:208(_checkLevel)
       17    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1153(__init__)
       12    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 _parser.py:304(checkgroupname)
        1    0.000    0.000    0.000    0.000 <frozen posixpath>:169(basename)
        7    0.000    0.000    0.000    0.000 argparse.py:589(_metavar_formatter)
        1    0.000    0.000    0.000    0.000 traceback.py:248(FrameSummary)
        1    0.000    0.000    0.000    0.000 <frozen os>:1116(__subclasshook__)
        1    0.000    0.000    0.000    0.000 parse.py:361(_fix_result_transcoding)
        1    0.000    0.000    0.000    0.000 __init__.py:1358(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:501(_requires_builtin_wrapper)
        9    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        2    0.000    0.000    0.000    0.000 _weakrefset.py:85(add)
        1    0.000    0.000    0.000    0.000 __init__.py:546(Formatter)
        1    0.000    0.000    0.000    0.000 argparse.py:1362(_ActionsContainer)
        1    0.000    0.000    0.000    0.000 __init__.py:1702(addHandler)
       17    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1178(get_filename)
        1    0.000    0.000    0.000    0.000 _compression.py:33(DecompressReader)
        1    0.000    0.000    0.000    0.000 argparse.py:1571(_get_positional_kwargs)
        7    0.000    0.000    0.000    0.000 argparse.py:206(__init__)
        9    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        3    0.000    0.000    0.000    0.000 enum.py:117(_iter_bits_lsb)
        3    0.000    0.000    0.000    0.000 _parser.py:295(seek)
        1    0.000    0.000    0.000    0.000 string.py:57(Template)
        3    0.000    0.000    0.000    0.000 threading.py:124(RLock)
        1    0.000    0.000    0.000    0.000 _weakrefset.py:37(__init__)
        1    0.000    0.000    0.000    0.000 core.py:14(Formula)
        4    0.000    0.000    0.000    0.000 functools.py:965(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:2557(_get_value)
       10    0.000    0.000    0.000    0.000 enum.py:1292(value)
       17    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:986(create_module)
        2    0.000    0.000    0.000    0.000 {method 'translate' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 ipaddress.py:563(_BaseAddress)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1158(create_module)
        4    0.000    0.000    0.000    0.000 __init__.py:811(__init__)
        1    0.000    0.000    0.000    0.000 <frozen posixpath>:60(isabs)
        8    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
        4    0.000    0.000    0.000    0.000 {method 'index' of 'str' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1428(_fixupParents)
        1    0.000    0.000    0.000    0.000 {built-in method posix._path_normpath}
        1    0.000    0.000    0.000    0.000 _parser.py:312(_class_escape)
        1    0.000    0.000    0.000    0.000 argparse.py:1887(_get_positional_actions)
        2    0.000    0.000    0.000    0.000 __init__.py:443(__init__)
        5    0.000    0.000    0.000    0.000 {built-in method sys._getframemodulename}
        1    0.000    0.000    0.000    0.000 <frozen _collections_abc>:104(_check_methods)
        1    0.000    0.000    0.000    0.000 argparse.py:892(BooleanOptionalAction)
        1    0.000    0.000    0.000    0.000 __init__.py:503(StringTemplateStyle)
        1    0.000    0.000    0.000    0.000 __init__.py:1373(disable)
        1    0.000    0.000    0.000    0.000 __init__.py:2285(NullHandler)
        1    0.000    0.000    0.000    0.000 ipaddress.py:2225(IPv6Network)
        4    0.000    0.000    0.000    0.000 functools.py:970(__set_name__)
        1    0.000    0.000    0.000    0.000 parse.py:834(_Quoter)
        2    0.000    0.000    0.000    0.000 argparse.py:1304(__init__)
        1    0.000    0.000    0.000    0.000 pathlib.py:1413(PosixPath)
        1    0.000    0.000    0.000    0.000 __init__.py:1287(_StderrHandler)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'memoryview' objects}
        4    0.000    0.000    0.000    0.000 _parser.py:166(__delitem__)
        1    0.000    0.000    0.000    0.000 argparse.py:109(_AttributeHolder)
        2    0.000    0.000    0.000    0.000 {built-in method maketrans}
        1    0.000    0.000    0.000    0.000 argparse.py:980(__call__)
        1    0.000    0.000    0.000    0.000 __init__.py:286(LogRecord)
        1    0.000    0.000    0.000    0.000 __init__.py:727(BufferingFormatter)
        1    0.000    0.000    0.000    0.000 _compression.py:9(BaseStream)
        2    0.000    0.000    0.000    0.000 {method 'setter' of 'property' objects}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.any}
        1    0.000    0.000    0.000    0.000 __init__.py:1202(FileHandler)
        1    0.000    0.000    0.000    0.000 parse.py:190(_NetlocResultMixinStr)
        1    0.000    0.000    0.000    0.000 argparse.py:794(Action)
        1    0.000    0.000    0.000    0.000 argparse.py:1672(_ArgumentGroup)
        1    0.000    0.000    0.000    0.000 argparse.py:2366(_get_nargs_pattern)
        1    0.000    0.000    0.000    0.000 __init__.py:806(Filterer)
        1    0.000    0.000    0.000    0.000 {built-in method posix.register_at_fork}
        1    0.000    0.000    0.000    0.000 parse.py:220(_NetlocResultMixinBytes)
        1    0.000    0.000    0.000    0.000 argparse.py:1714(_MutuallyExclusiveGroup)
        1    0.000    0.000    0.000    0.000 pathlib.py:801(PurePosixPath)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.get_frozen_object}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1276(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method _imp.exec_builtin}
        1    0.000    0.000    0.000    0.000 core.py:15(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:1287(FileType)
        1    0.000    0.000    0.000    0.000 argparse.py:949(_StoreAction)
        1    0.000    0.000    0.000    0.000 pathlib.py:151(_Selector)
        1    0.000    0.000    0.000    0.000 traceback.py:90(_Sentinel)
        4    0.000    0.000    0.000    0.000 {built-in method _sre.ascii_tolower}
        1    0.000    0.000    0.000    0.000 argparse.py:1148(_VersionAction)
        1    0.000    0.000    0.000    0.000 argparse.py:1342(Namespace)
        1    0.000    0.000    0.000    0.000 parse.py:136(_ResultMixinStr)
        4    0.000    0.000    0.000    0.000 {built-in method _sre.ascii_iscased}
        1    0.000    0.000    0.000    0.000 argparse.py:1129(_HelpAction)
        1    0.000    0.000    0.000    0.000 pathlib.py:1425(WindowsPath)
        1    0.000    0.000    0.000    0.000 {method 'groups' of 're.Match' objects}
        1    0.000    0.000    0.000    0.000 <frozen posixpath>:52(normcase)
        1    0.000    0.000    0.000    0.000 argparse.py:204(_Section)
        1    0.000    0.000    0.000    0.000 argparse.py:731(MetavarTypeHelpFormatter)
        1    0.000    0.000    0.000    0.000 pathlib.py:180(_ParentSelector)
        1    0.000    0.000    0.000    0.000 pathlib.py:223(_RecursiveWildcardSelector)
        1    0.000    0.000    0.000    0.000 pathlib.py:811(PureWindowsPath)
        1    0.000    0.000    0.000    0.000 ipaddress.py:20(AddressValueError)
        1    0.000    0.000    0.000    0.000 pathlib.py:241(_DoubleRecursiveWildcardSelector)
        1    0.000    0.000    0.000    0.000 argparse.py:1041(_AppendAction)
        1    0.000    0.000    0.000    0.000 traceback.py:656(_ExceptionPrintContext)
        1    0.000    0.000    0.000    0.000 __init__.py:1861(RootLogger)
        1    0.000    0.000    0.000    0.000 argparse.py:1178(_ChoicesPseudoAction)
        1    0.000    0.000    0.000    0.000 parse.py:323(DefragResult)
        1    0.000    0.000    0.000    0.000 __init__.py:769(Filter)
        1    0.000    0.000    0.000    0.000 __init__.py:1311(PlaceHolder)
        1    0.000    0.000    0.000    0.000 argparse.py:1106(_CountAction)
        1    0.000    0.000    0.000    0.000 shutil.py:67(Error)
        1    0.000    0.000    0.000    0.000 argparse.py:1007(_StoreTrueAction)
        1    0.000    0.000    0.000    0.000 argparse.py:984(_StoreConstAction)
        1    0.000    0.000    0.000    0.000 argparse.py:1079(_AppendConstAction)
        1    0.000    0.000    0.000    0.000 argparse.py:680(RawDescriptionHelpFormatter)
        1    0.000    0.000    0.000    0.000 pathlib.py:191(_WildcardSelector)
        1    0.000    0.000    0.000    0.000 parse.py:144(_ResultMixinBytes)
        1    0.000    0.000    0.000    0.000 parse.py:350(SplitResultBytes)
        1    0.000    0.000    0.000    0.000 ipaddress.py:24(NetmaskValueError)
        1    0.000    0.000    0.000    0.000 ipaddress.py:1131(_BaseConstants)
        2    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method atexit.register}
        2    0.000    0.000    0.000    0.000 enum.py:1411(<lambda>)
        1    0.000    0.000    0.000    0.000 argparse.py:1349(__init__)
        1    0.000    0.000    0.000    0.000 argparse.py:691(RawTextHelpFormatter)
        1    0.000    0.000    0.000    0.000 argparse.py:765(ArgumentError)
        1    0.000    0.000    0.000    0.000 parse.py:331(SplitResult)
        1    0.000    0.000    0.000    0.000 argparse.py:702(ArgumentDefaultsHelpFormatter)
        1    0.000    0.000    0.000    0.000 argparse.py:1276(_ExtendAction)
        1    0.000    0.000    0.000    0.000 pathlib.py:174(_TerminatingSelector)
        1    0.000    0.000    0.000    0.000 parse.py:336(ParseResult)
        1    0.000    0.000    0.000    0.000 parse.py:342(DefragResultBytes)
        1    0.000    0.000    0.000    0.000 shutil.py:70(SameFileError)
        1    0.000    0.000    0.000    0.000 __init__.py:1776(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 argparse.py:1024(_StoreFalseAction)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 parse.py:355(ParseResultBytes)
        1    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'removeprefix' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1014(is_package)
        1    0.000    0.000    0.000    0.000 argparse.py:785(ArgumentTypeError)
        1    0.000    0.000    0.000    0.000 argparse.py:2582(_check_value)
        1    0.000    0.000    0.000    0.000 __init__.py:1033(setFormatter)
        1    0.000    0.000    0.000    0.000 shutil.py:80(ReadError)
        1    0.000    0.000    0.000    0.000 shutil.py:83(RegistryError)
        1    0.000    0.000    0.000    0.000 shutil.py:87(_GiveupOnFastCopy)
        1    0.000    0.000    0.000    0.000 {method '__init_subclass__' of 'object' objects}
        1    0.000    0.000    0.000    0.000 shutil.py:77(ExecError)
        1    0.000    0.000    0.000    0.000 __init__.py:1369(disable)
        1    0.000    0.000    0.000    0.000 shutil.py:73(SpecialFileError)
```
</details>
