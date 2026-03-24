#!/usr/bin/python3
import functools
import itertools
import multiprocessing
import os
import pathlib
import re
import sys
from urllib.parse import urlparse
from typing import Iterator, List, Tuple, Optional, Dict, Any, Generator

from pnk.helpers import logger

log = logger.get_logger()
# Ensure immediate output flushing
print = functools.partial(print, flush=True)


class WorkerFormula:
    """Optimized worker class for multiprocessing - following High Performance Python best practices"""
    # Pre-compile ALL regex patterns at class level (immutable, shared across processes)
    DOMAIN_PATTERN = re.compile(
        r"[\w-]+[.](рф|com|co.uk|ru|org|co|in|ai|sh|io|jp|com.cn|cn|cz|de|net|fr|it|au|ca|ir|br|com.br|co.kr|gov|uk|kz|tech|shop|moscow|store|me)$"
    )
    DASH_UNDERSCORE_PATTERN = re.compile(r"[-_]")
    DIGIT_PATTERN = re.compile(r"(?<!\d)\d{1,2}(?!\d)")
    CARTESIAN_PATTERN = re.compile(r"((?<!\d)\d{1,2}(?!\d))")
    
    def __init__(self, args_dict: Dict[str, Any]):
        # Keep as dict to avoid expensive namespace creation
        self.args_dict = args_dict
        self._separators = ["-", "_", "."]
        self._domain_pattern_cache = {}
    
    @property
    def args(self):
        """Lazy namespace creation only when needed"""
        if not hasattr(self, '_args_obj'):
            self._args_obj = type('Args', (), self.args_dict)()
        return self._args_obj
    
    def parse_hostname(self, hostname: str, target: Optional[str] = None) -> Tuple[str, str, List[str]]:
        """Extract a domain and subdomains from the input - OPTIMIZED"""
        url = urlparse(hostname)
        host = url.hostname or url.geturl()
        
        if not host:
            raise TypeError(f"No host found for {host}")
        
        # Use cached pattern or compile new one
        if target:
            pattern = self._domain_pattern_cache.get(target)
            if pattern is None:
                pattern = re.compile(rf"{re.escape(target)}$")
                self._domain_pattern_cache[target] = pattern
        else:
            pattern = self.DOMAIN_PATTERN
            
        _domain = pattern.search(host)
        
        if not _domain:
            raise TypeError(f"No domain found for {host}")
            
        _subdomains = host[:_domain.start()] + host[_domain.end():]
        if not _subdomains:
            raise TypeError(f"No subdomains found for {host}")
            
        domain = _domain.group(0)
        
        # More efficient subdomain splitting
        subdomains = _subdomains.rstrip('.').split('.')
        
        return host, domain, subdomains
    
    def pnk(self, subdomains: List[str]) -> Iterator[Tuple[str, ...]]:
        """Sequence of permutations on subdomains - OPTIMIZED"""
        return itertools.permutations(subdomains)
    
    def replacer(self, subdomains: List[str]) -> Iterator[Tuple[Tuple[str, ...], ...]]:
        """Replace `-` and `_` found in subdomain with dots and vice versa - OPTIMIZED"""
        result_arrays = []
        has_replacements = False
        
        for s in subdomains:
            parts = self.DASH_UNDERSCORE_PATTERN.split(s)
            if len(parts) == 1:
                result_arrays.append([(s,)])
            else:
                has_replacements = True
                # Build combinations iteratively for better performance
                combinations = []
                for i, part in enumerate(parts):
                    combinations.append([part])
                    if i < len(parts) - 1:
                        combinations.append(self._separators)
                result_arrays.append(itertools.product(*combinations))
        
        if has_replacements:
            return itertools.product(*result_arrays)
        return iter(())
    
    def incrmt(self, subdomain: str) -> Iterator[str]:
        """Increment a digit found in subdomain - OPTIMIZED"""
        # Find all matches first to avoid repeated iteration
        matches = list(self.DIGIT_PATTERN.finditer(subdomain))
        if not matches:
            return
            
        for match in matches:
            m_start, m_end = match.start(), match.end()
            match_group = match.group()
            range_count = 10 if len(match_group) < 2 else 100
            width = len(match_group)
            
            # Pre-compute parts outside the loop
            prefix = subdomain[:m_start]
            suffix = subdomain[m_end:]
            
            # Pre-generate all replacements
            replacements = [str(i).zfill(width) for i in range(range_count)]
            
            # Yield all variations
            for replacement in replacements:
                yield prefix + replacement + suffix
            
            # Check for duplicated digits
            if (match_group in prefix and match_group not in suffix):
                for replacement in replacements:
                    yield subdomain.replace(match_group, replacement)
    
    def crtsn(self, subdomains: List[str]) -> Iterator[Tuple[Tuple[str, ...], ...]]:
        """Cartesian product with digit replacement - OPTIMIZED"""
        subs_list = []
        is_process = False
        
        for _s in subdomains:
            _list = self.CARTESIAN_PATTERN.split(_s)
            _deque = []
            
            if len(_list) == 1:
                _deque.append(_list)
            else:
                is_process = True
                
                for x in _list:
                    if not x:  # Skip empty strings early
                        continue
                    try:
                        _integer = int(x)
                        # Check if it's a valid 1-2 digit number
                        if 0 <= _integer <= 99 or x in ("0", "00"):
                            x_length = len(x)
                            if x_length <= 2:
                                # Pre-generate all number variations
                                num_range = range(10 if x_length == 1 else 100)
                                _deque.append([str(i).zfill(x_length) for i in num_range])
                            else:
                                _deque.append([x])
                    except ValueError:
                        _deque.append([x])
            
            subs_list.append(itertools.product(*_deque))
        
        if is_process:
            return itertools.product(*subs_list)
        return iter(())
    
    def join_product_tuples(self, tuples: Tuple[Tuple[str, ...], ...], delimeter: Optional[str] = None) -> str:
        """Convert a list of tuples into a string - OPTIMIZED"""
        dlmtr = delimeter if delimeter else "."
        
        # Replace recursion with iterative join for better performance
        parts = []
        for t in tuples:
            parts.append("".join(t))
        return dlmtr.join(parts)
    
    def produce_wordlist(self, subdomains: List[str]) -> Iterator[Iterator[Tuple[str, ...]]]:
        """Read wordlist and yield permutations - OPTIMIZED"""
        wordlist_path = (
            self.args_dict.get('wordlist')
            or pathlib.Path(__file__).parent / "wordlist.txt"
        )
        
        # Read wordlist once and cache if possible
        try:
            with open(wordlist_path, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f if line.strip()]
        except (IOError, OSError):
            return  # Silently handle errors in worker
            
        for word in words:
            yield self.pnk([word, *subdomains])
    
    def _process_line_operations(self, s: List[str], d: str) -> List[str]:
        """Process all operations for a single line - OPTIMIZED to reduce function calls"""
        results = []
        args = self.args_dict  # Use dict directly for performance
        
        if args.get('increment'):
            s_copy = s.copy()  # Copy once per operation
            for index, j in enumerate(s):
                for i in self.incrmt(j):
                    s_copy[index] = i
                    results.append(".".join(filter(None, [".".join(s_copy), d])))
                s_copy[index] = j  # Reset

        if args.get('cartesian'):
            for c in self.crtsn(s):
                results.append(".".join(filter(None, [self.join_product_tuples(c), d])))

        if args.get('replace'):
            for x in self.replacer(s):
                results.append(".".join(filter(None, [self.join_product_tuples(x), d])))

        if args.get('wordlist'):
            for word_subs_permutations in self.produce_wordlist(s):
                for p in word_subs_permutations:
                    result1 = ".".join(filter(None, [self.join_product_tuples(p), d]))
                    result2 = ".".join(filter(None, [self.join_product_tuples(p, "-"), d]))
                    results.append(result1)
                    results.append(result2)

        # Default permutations
        for p in self.pnk(s):
            results.append(".".join(filter(None, [".".join(p), d])))
        
        return results
    
    def process_chunk(self, chunk: List[str]) -> List[str]:
        """Process a chunk of lines efficiently"""
        all_results = []
        
        for line in chunk:
            line = line.strip()
            if not line:
                continue
                
            try:
                if self.args_dict.get('data'):
                    h, d, s = (None, None, line.split("."))
                else:
                    target = self.args_dict.get('target')
                    parse_func = (self.parse_hostname if not target
                                else lambda x: self.parse_hostname(x, target))
                    h, d, s = parse_func(line)
            except TypeError:
                continue  # Skip invalid lines silently in worker
            
            # Process all operations for this line and collect results
            results = self._process_line_operations(s, d)
            all_results.extend(results)
        
        return all_results


def worker_process_chunk(chunk_data: Tuple[List[str], Dict[str, Any]]) -> List[str]:
    """
    Worker function for multiprocessing - optimized following High Performance Python
    - Minimal function call overhead
    - Stateless design
    - Efficient memory usage
    """
    chunk, args_dict = chunk_data
    worker = WorkerFormula(args_dict)
    return worker.process_chunk(chunk)


class Formula:
    """Main Formula class with optimized multiprocessing and memory management"""
    
    # Pre-compile ALL regex patterns at class level
    DOMAIN_PATTERN = re.compile(
        r"[\w-]+[.](рф|com|co.uk|ru|org|co|in|ai|sh|io|jp|com.cn|cn|cz|de|net|fr|it|au|ca|ir|br|com.br|co.kr|gov|uk|kz|tech|shop|moscow|store|me)$"
    )
    DASH_UNDERSCORE_PATTERN = re.compile(r"[-_]")
    DIGIT_PATTERN = re.compile(r"(?<!\d)\d{1,2}(?!\d)")
    CARTESIAN_PATTERN = re.compile(r"((?<!\d)\d{1,2}(?!\d))")
    
    # Cache for domain patterns with targets
    _domain_pattern_cache = {}
    
    def __init__(self, args, file, wordlist=None) -> None:
        self.args = args
        self.file = file
        self.wordlist = wordlist
        # Pre-compute frequently used values
        self._separators = ["-", "_", "."]

    def parse_hostname(self, hostname: str, target: Optional[str] = None) -> Tuple[str, str, List[str]]:
        """Extract a domain and subdomains from the input - OPTIMIZED"""
        log.debug(f"{target=}")
        url = urlparse(hostname)
        log.debug(f"{url=}")
        host = url.hostname or url.geturl()
        log.debug(f"{host=}")
        
        if not host:
            raise TypeError(f"No host found for {host}")
        
        # Use cached pattern or compile new one
        if target:
            pattern = self._domain_pattern_cache.get(target)
            if pattern is None:
                pattern = re.compile(rf"{re.escape(target)}$")
                self._domain_pattern_cache[target] = pattern
        else:
            pattern = self.DOMAIN_PATTERN
            
        _domain = pattern.search(host)
        log.debug(f"{_domain=}")
        
        if not _domain:
            raise TypeError(f"No domain found for {host}")
            
        _subdomains = host[:_domain.start()] + host[_domain.end():]
        if not _subdomains:
            raise TypeError(f"No subdomains found for {host}")
            
        domain = _domain.group(0)
        log.debug(f"{domain=}")
        
        # More efficient subdomain splitting
        subdomains = _subdomains.rstrip('.').split('.')
        log.debug(f"{subdomains=}")
        
        return host, domain, subdomains

    def pnk(self, subdomains: List[str]) -> Iterator[Tuple[str, ...]]:
        """Sequence of permutations on subdomains - OPTIMIZED"""
        log.debug("Permutation...")
        return itertools.permutations(subdomains)

    def replacer(self, subdomains: List[str]) -> Iterator[Tuple[Tuple[str, ...], ...]]:
        """Replace `-` and `_` found in subdomain with dots and vice versa - OPTIMIZED"""
        log.debug("Replace dashes and underscores with dots")
        
        result_arrays = []
        has_replacements = False
        
        for s in subdomains:
            parts = self.DASH_UNDERSCORE_PATTERN.split(s)
            if len(parts) == 1:
                result_arrays.append([(s,)])
            else:
                has_replacements = True
                # Build combinations iteratively for better performance
                combinations = []
                for i, part in enumerate(parts):
                    combinations.append([part])
                    if i < len(parts) - 1:
                        combinations.append(self._separators)
                result_arrays.append(itertools.product(*combinations))
        
        if has_replacements:
            return itertools.product(*result_arrays)
        return iter(())

    def incrmt(self, subdomain: str) -> Iterator[str]:
        """Increment a digit found in subdomain - OPTIMIZED"""
        log.debug(f"Increment digits on {subdomain=}")
        
        # Find all matches first to avoid repeated iteration
        matches = list(self.DIGIT_PATTERN.finditer(subdomain))
        if not matches:
            log.debug("No digits found!")
            return
            
        for match in matches:
            m_start, m_end = match.start(), match.end()
            match_group = match.group()
            range_count = 10 if len(match_group) < 2 else 100
            width = len(match_group)
            
            # Pre-compute parts outside the loop
            prefix = subdomain[:m_start]
            suffix = subdomain[m_end:]
            
            # Pre-generate all replacements
            replacements = [str(i).zfill(width) for i in range(range_count)]
            
            # Yield all variations
            for replacement in replacements:
                yield prefix + replacement + suffix
            
            # Check for duplicated digits
            if (match_group in prefix and match_group not in suffix):
                log.debug("duplicated digits")
                for replacement in replacements:
                    yield subdomain.replace(match_group, replacement)

    def crtsn(self, subdomains: List[str]) -> Iterator[Tuple[Tuple[str, ...], ...]]:
        """Cartesian product with digit replacement - OPTIMIZED"""
        log.debug("Cartesian...")
        
        subs_list = []
        is_process = False
        
        for _s in subdomains:
            log.debug(_s)
            _list = self.CARTESIAN_PATTERN.split(_s)
            _deque = []
            
            if len(_list) == 1:
                _deque.append(_list)
            else:
                is_process = True
                log.debug(_list)
                
                for x in _list:
                    if not x:  # Skip empty strings early
                        continue
                    try:
                        _integer = int(x)
                        # Check if it's a valid 1-2 digit number
                        if 0 <= _integer <= 99 or x in ("0", "00"):
                            log.debug(f"{x=}")
                            x_length = len(x)
                            if x_length <= 2:
                                # Pre-generate all number variations
                                num_range = range(10 if x_length == 1 else 100)
                                _deque.append([str(i).zfill(x_length) for i in num_range])
                            else:
                                _deque.append([x])
                    except ValueError:
                        _deque.append([x])
            
            subs_list.append(itertools.product(*_deque))
        
        if is_process:
            return itertools.product(*subs_list)
        return iter(())

    def join_product_tuples(self, tuples: Tuple[Tuple[str, ...], ...], delimeter: Optional[str] = None) -> str:
        """Convert a list of tuples into a string - OPTIMIZED"""
        dlmtr = delimeter if delimeter else "."
        log.debug(tuples)
        
        # Replace recursion with iterative join for better performance
        parts = []
        for t in tuples:
            parts.append("".join(t))
        return dlmtr.join(parts)

    def produce_wordlist(self, subdomains: List[str]) -> Iterator[Iterator[Tuple[str, ...]]]:
        """Read wordlist and yield permutations - OPTIMIZED"""
        wordlist_path = (
            self.args.wordlist
            if self.args.wordlist
            else pathlib.Path(__file__).parent / "wordlist.txt"
        )
        
        # Read wordlist once and cache if possible
        try:
            with open(wordlist_path, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f if line.strip()]
        except (IOError, OSError) as e:
            log.error(f"Error reading wordlist: {e}")
            return
            
        for word in words:
            log.debug(f"{word=}")
            yield self.pnk([word, *subdomains])

    def _process_single_line(self, line: str) -> None:
        """Process a single line in single-process mode"""
        log.debug(line)
        try:
            if self.args.data:
                h, d, s = (None, None, line.split("."))
            else:
                parse_func = (self.parse_hostname if not self.args.target
                            else lambda x: self.parse_hostname(x, self.args.target))
                h, d, s = parse_func(line)
        except TypeError as err:
            log.debug(f"{err=}")
            return
        
        # Process all operations for this line
        self._process_line_operations(s, d)

    def _process_line_operations(self, s: List[str], d: str) -> None:
        """Process all operations for a single line - OPTIMIZED to reduce function calls"""
        # Use local variables for frequently accessed attributes
        args = self.args
        
        if args.increment:
            s_copy = s.copy()  # Copy once per operation
            for index, j in enumerate(s):
                for i in self.incrmt(j):
                    s_copy[index] = i
                    print(".".join(filter(None, [".".join(s_copy), d])))
                s_copy[index] = j  # Reset

        if args.cartesian:
            for c in self.crtsn(s):
                log.debug(c)
                print(".".join(filter(None, [self.join_product_tuples(c), d])))

        if args.replace:
            for x in self.replacer(s):
                log.debug(x)
                print(".".join(filter(None, [self.join_product_tuples(x), d])))

        if args.wordlist:
            for word_subs_permutations in self.produce_wordlist(s):
                for p in word_subs_permutations:
                    log.debug(p)
                    result1 = ".".join(filter(None, [self.join_product_tuples(p), d]))
                    result2 = ".".join(filter(None, [self.join_product_tuples(p, "-"), d]))
                    print(result1)
                    print(result2)

        # Default permutations
        for p in self.pnk(s):
            log.debug(p)
            print(".".join(filter(None, [".".join(p), d])))

    def _get_args_dict(self) -> Dict[str, Any]:
        """Convert args to dictionary for multiprocessing"""
        return {
            'increment': getattr(self.args, 'increment', False),
            'cartesian': getattr(self.args, 'cartesian', False),
            'data': getattr(self.args, 'data', False),
            'replace': getattr(self.args, 'replace', False),
            'target': getattr(self.args, 'target', None),
            'wordlist': getattr(self.args, 'wordlist', None),
        }

    def _calculate_chunk_size(self, num_jobs: int, estimated_lines: int = None) -> int:
        """Calculate optimal chunk size based on High Performance Python best practices
        Follow High Performance Python guidance:
            - Chunks should take 100ms-1s to process
            - Avoid too many small chunks
            - Consider L1/L2 cache sizes
        """
        cpu_count = multiprocessing.cpu_count()
        
        if estimated_lines:
            if estimated_lines < 100:
                """Performance: Multiprocessing overhead may hurt performance"""
                # Very small files - single process recommended
                return estimated_lines
            elif estimated_lines < 1000:
                # Small files: smaller chunks for better load balancing
                return min(50, estimated_lines // 2)
            elif estimated_lines < 10000:
                # Medium files: balanced chunking
                return 200
            elif estimated_lines < 100000:
                # Large files: larger chunks for efficiency
                return 500
            elif estimated_lines < 1000000:
                # Large files: larger chunks for efficiency
                return 1000
            else:
                # Very large files: optimize for throughput
                return 2000
        else:
            # Default based on CPU count and jobs
            return 200 * min(cpu_count, num_jobs)

    def _generate_chunks_from_stream(self, file_objects, chunk_size: int, args_dict: Dict[str, Any]) -> Generator[Tuple[List[str], Dict[str, Any]], None, None]:
        """Stream chunks without loading entire file into memory - CRITICAL FIX"""
        current_chunk = []
        
        for file_obj in file_objects:
            for line in file_obj:
                line = line.strip()
                if line:
                    current_chunk.append(line)
                    if len(current_chunk) >= chunk_size:
                        yield (current_chunk.copy(), args_dict)
                        current_chunk.clear()
        
        # Yield any remaining lines
        if current_chunk:
            yield (current_chunk, args_dict)

    def _output_results_buffered(self, results: List[str], buffer_size: int = 5000) -> None:
        """Efficient buffered output with optimized I/O"""
        if not results:
            return
            
        # Use larger buffers for better I/O performance
        if len(results) >= buffer_size:
            # Large result set - write in optimized batches
            for i in range(0, len(results), buffer_size):
                batch = results[i:i + buffer_size]
                sys.stdout.write("\n".join(batch) + "\n")
                sys.stdout.flush()
        else:
            # Small result set - write all at once
            sys.stdout.write("\n".join(results) + "\n")
            sys.stdout.flush()

    def _estimate_line_count(self) -> int:
        """Quickly estimate line count for chunk size optimization"""
        try:
            line_count = 0
            for file_obj in self.file:
                # Reset file pointer if possible
                if hasattr(file_obj, 'seek'):
                    current_pos = file_obj.tell()
                    file_obj.seek(0)
                    line_count += sum(1 for _ in file_obj)
                    file_obj.seek(current_pos)
                else:
                    # Can't reset, use default estimation
                    return 10000  # Conservative default
            return line_count
        except (IOError, OSError):
            return 10000  # Fallback to conservative estimate

    def run(self) -> None:
        """Optimized runner with proper memory management and multiprocessing"""
        num_jobs = getattr(self.args, 'jobs', 1)
        
        # Estimate line count for optimal chunk sizing
        estimated_lines = self._estimate_line_count()
        
        # For very small files, use single process to avoid multiprocessing overhead
        if estimated_lines < 100 or num_jobs == 1:
            log.debug("Using single-process mode")
            for lines in self.file:
                for line in lines:
                    self._process_single_line(line.strip())
            return
        
        # Multiprocessing mode with streaming chunks
        args_dict = self._get_args_dict()
        chunk_size = self._calculate_chunk_size(num_jobs, estimated_lines)
        
        log.info(f"Starting multiprocessing with {num_jobs} jobs, chunk size {chunk_size}")
        
        # Generate chunks from stream (memory efficient)
        chunk_generator = self._generate_chunks_from_stream(self.file, chunk_size, args_dict)
        
        # Use appropriate multiprocessing context
        if hasattr(os, 'fork'):
            ctx = multiprocessing.get_context('fork')  # Better performance on Unix
        else:
            ctx = multiprocessing.get_context('spawn')
        
        with ctx.Pool(processes=num_jobs) as pool:
            # Process chunks as they become available
            results_iterator = pool.imap_unordered(
                worker_process_chunk,
                chunk_generator,
                chunksize=1  # Each chunk is one work unit
            )
            
            # Process results with efficient buffering
            total_results = 0
            for result_list in results_iterator:
                if result_list:
                    self._output_results_buffered(result_list)
                    total_results += len(result_list)
            
            log.debug(f"Processing complete, generated {total_results} results")