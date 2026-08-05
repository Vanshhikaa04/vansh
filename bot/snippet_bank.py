"""
Bank of small, genuine Python snippets the commit bot draws from.

Each entry is real, self-contained, useful code (a function, decorator, or
tiny class) — not filler. The bot picks one unused entry per commit, writes
it to snippets/<category>/<id>.py, and commits it.

Feel free to add more entries over time; once the bank (plus the
test-generation fallback in commit_bot.py) is exhausted, the bot logs a
skip instead of inventing meaningless content.
"""

from __future__ import annotations

import textwrap

SNIPPETS: list[dict] = []


def _add(id_: str, category: str, title: str, code: str, message: str | None = None) -> None:
    SNIPPETS.append(
        {
            "id": id_,
            "category": category,
            "title": title,
            "code": textwrap.dedent(code).strip() + "\n",
            "commit_message": message or f"Add {title} to {category} snippets",
        }
    )


# ---------------------------------------------------------------- math ----

_add(
    "is_prime",
    "math",
    "is_prime",
    '''
    """Check whether a positive integer is prime."""


    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    ''',
)

_add(
    "gcd_lcm",
    "math",
    "gcd_lcm",
    '''
    """Greatest common divisor and least common multiple."""


    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return abs(a)


    def lcm(a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // gcd(a, b)
    ''',
)

_add(
    "factorial",
    "math",
    "factorial",
    '''
    """Iterative and recursive factorial implementations."""


    def factorial_iterative(n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


    def factorial_recursive(n: int) -> int:
        return 1 if n <= 1 else n * factorial_recursive(n - 1)
    ''',
)

_add(
    "fibonacci",
    "math",
    "fibonacci",
    '''
    """Fibonacci sequence generators."""
    from functools import lru_cache


    def fibonacci_iterative(n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


    @lru_cache(maxsize=None)
    def fibonacci_recursive(n: int) -> int:
        return n if n < 2 else fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    ''',
)

_add(
    "sum_of_digits",
    "math",
    "sum_of_digits",
    '''
    """Sum and digital root of an integer's digits."""


    def sum_of_digits(n: int) -> int:
        return sum(int(d) for d in str(abs(n)))


    def digital_root(n: int) -> int:
        n = abs(n)
        while n >= 10:
            n = sum_of_digits(n)
        return n
    ''',
)

_add(
    "is_armstrong_number",
    "math",
    "is_armstrong_number",
    '''
    """Check whether a number equals the sum of its digits raised to the
    power of the digit count (e.g. 153 = 1**3 + 5**3 + 3**3)."""


    def is_armstrong_number(n: int) -> bool:
        digits = str(n)
        power = len(digits)
        return n == sum(int(d) ** power for d in digits)
    ''',
)

_add(
    "collatz_sequence",
    "math",
    "collatz_sequence",
    '''
    """Generate the Collatz sequence starting at n until it reaches 1."""


    def collatz_sequence(n: int) -> list[int]:
        if n < 1:
            raise ValueError("n must be a positive integer")
        sequence = [n]
        while n != 1:
            n = n // 2 if n % 2 == 0 else 3 * n + 1
            sequence.append(n)
        return sequence
    ''',
)

_add(
    "sieve_of_eratosthenes",
    "math",
    "sieve_of_eratosthenes",
    '''
    """List all primes up to n using the Sieve of Eratosthenes."""


    def sieve_of_eratosthenes(n: int) -> list[int]:
        if n < 2:
            return []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False
        return [i for i, prime in enumerate(is_prime) if prime]
    ''',
)

_add(
    "power_iterative",
    "math",
    "power_iterative",
    '''
    """Compute base ** exponent using fast exponentiation (O(log n))."""


    def power(base: float, exponent: int) -> float:
        if exponent < 0:
            return 1 / power(base, -exponent)
        result = 1.0
        while exponent:
            if exponent & 1:
                result *= base
            base *= base
            exponent >>= 1
        return result
    ''',
)

_add(
    "is_perfect_number",
    "math",
    "is_perfect_number",
    '''
    """A perfect number equals the sum of its proper divisors (e.g. 28)."""


    def is_perfect_number(n: int) -> bool:
        if n < 2:
            return False
        divisor_sum = sum(i for i in range(1, n) if n % i == 0)
        return divisor_sum == n
    ''',
)

# ------------------------------------------------------------- strings ----

_add(
    "is_palindrome",
    "strings",
    "is_palindrome",
    '''
    """Check whether a string reads the same forwards and backwards,
    ignoring case, spaces, and punctuation."""
    import re


    def is_palindrome(text: str) -> bool:
        cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
        return cleaned == cleaned[::-1]
    ''',
)

_add(
    "is_anagram",
    "strings",
    "is_anagram",
    '''
    """Check whether two strings are anagrams of each other."""
    from collections import Counter


    def is_anagram(a: str, b: str) -> bool:
        normalize = lambda s: Counter(s.lower().replace(" ", ""))
        return normalize(a) == normalize(b)
    ''',
)

_add(
    "reverse_words",
    "strings",
    "reverse_words",
    '''
    """Reverse the order of words in a sentence."""


    def reverse_words(sentence: str) -> str:
        return " ".join(sentence.split()[::-1])
    ''',
)

_add(
    "caesar_cipher",
    "strings",
    "caesar_cipher",
    '''
    """A classic Caesar cipher encoder/decoder."""
    import string


    def caesar_encode(text: str, shift: int) -> str:
        alphabet = string.ascii_lowercase
        shifted = alphabet[shift % 26:] + alphabet[:shift % 26]
        table = str.maketrans(alphabet + alphabet.upper(), shifted + shifted.upper())
        return text.translate(table)


    def caesar_decode(text: str, shift: int) -> str:
        return caesar_encode(text, -shift)
    ''',
)

_add(
    "run_length_encoding",
    "strings",
    "run_length_encoding",
    '''
    """Run-length encode/decode a string, e.g. "aaab" <-> "3a1b"."""
    from itertools import groupby


    def run_length_encode(text: str) -> str:
        return "".join(f"{len(list(group))}{char}" for char, group in groupby(text))


    def run_length_decode(encoded: str) -> str:
        result = []
        count = ""
        for char in encoded:
            if char.isdigit():
                count += char
            else:
                result.append(char * int(count))
                count = ""
        return "".join(result)
    ''',
)

_add(
    "longest_common_prefix",
    "strings",
    "longest_common_prefix",
    '''
    """Find the longest common prefix shared by a list of strings."""


    def longest_common_prefix(words: list[str]) -> str:
        if not words:
            return ""
        prefix = words[0]
        for word in words[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    ''',
)

_add(
    "count_vowels",
    "strings",
    "count_vowels",
    '''
    """Count vowels in a string."""


    def count_vowels(text: str) -> int:
        return sum(1 for char in text.lower() if char in "aeiou")
    ''',
)

_add(
    "is_pangram",
    "strings",
    "is_pangram",
    '''
    """Check whether a sentence uses every letter of the alphabet at least once."""
    import string


    def is_pangram(sentence: str) -> bool:
        return set(string.ascii_lowercase) <= set(sentence.lower())
    ''',
)

_add(
    "title_case",
    "strings",
    "title_case",
    '''
    """Title-case a sentence while keeping small connector words lowercase."""

    _SMALL_WORDS = {"a", "an", "the", "and", "but", "or", "of", "in", "on", "to"}


    def title_case(sentence: str) -> str:
        words = sentence.split()
        result = []
        for i, word in enumerate(words):
            lowered = word.lower()
            if i != 0 and lowered in _SMALL_WORDS:
                result.append(lowered)
            else:
                result.append(lowered.capitalize())
        return " ".join(result)
    ''',
)

_add(
    "dedupe_preserve_order",
    "strings",
    "dedupe_preserve_order",
    '''
    """Remove duplicate characters/words while preserving first-seen order."""


    def dedupe_preserve_order(items: list) -> list:
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    ''',
)

_add(
    "word_frequency",
    "strings",
    "word_frequency",
    '''
    """Count word frequency in a block of text."""
    import re
    from collections import Counter


    def word_frequency(text: str) -> Counter:
        words = re.findall(r"[a-z']+", text.lower())
        return Counter(words)
    ''',
)

# --------------------------------------------------------------- lists ----

_add(
    "chunk_list",
    "lists",
    "chunk_list",
    '''
    """Split a list into fixed-size chunks."""


    def chunk_list(items: list, size: int) -> list[list]:
        if size <= 0:
            raise ValueError("size must be positive")
        return [items[i:i + size] for i in range(0, len(items), size)]
    ''',
)

_add(
    "flatten_list",
    "lists",
    "flatten_list",
    '''
    """Recursively flatten an arbitrarily nested list."""
    from collections.abc import Iterable


    def flatten_list(items: Iterable) -> list:
        result = []
        for item in items:
            if isinstance(item, list):
                result.extend(flatten_list(item))
            else:
                result.append(item)
        return result
    ''',
)

_add(
    "rotate_list",
    "lists",
    "rotate_list",
    '''
    """Rotate a list left or right by k positions."""


    def rotate_list(items: list, k: int) -> list:
        if not items:
            return items
        k %= len(items)
        return items[k:] + items[:k]
    ''',
)

_add(
    "find_duplicates",
    "lists",
    "find_duplicates",
    '''
    """Return elements that appear more than once, preserving first-seen order."""
    from collections import Counter


    def find_duplicates(items: list) -> list:
        counts = Counter(items)
        seen = set()
        result = []
        for item in items:
            if counts[item] > 1 and item not in seen:
                seen.add(item)
                result.append(item)
        return result
    ''',
)

_add(
    "moving_average",
    "lists",
    "moving_average",
    '''
    """Compute the simple moving average over a sliding window."""


    def moving_average(values: list[float], window: int) -> list[float]:
        if window <= 0:
            raise ValueError("window must be positive")
        return [
            sum(values[i:i + window]) / window
            for i in range(len(values) - window + 1)
        ]
    ''',
)

_add(
    "transpose_matrix",
    "lists",
    "transpose_matrix",
    '''
    """Transpose a 2D matrix represented as a list of lists."""


    def transpose_matrix(matrix: list[list]) -> list[list]:
        return [list(row) for row in zip(*matrix)]
    ''',
)

_add(
    "binary_search",
    "lists",
    "binary_search",
    '''
    """Binary search over a sorted list; returns the index or -1."""


    def binary_search(sorted_items: list, target) -> int:
        low, high = 0, len(sorted_items) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_items[mid] == target:
                return mid
            if sorted_items[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    ''',
)

_add(
    "bubble_sort",
    "lists",
    "bubble_sort",
    '''
    """Bubble sort: simple O(n^2) in-place sort, returns a new sorted list."""


    def bubble_sort(items: list) -> list:
        result = list(items)
        n = len(result)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
            if not swapped:
                break
        return result
    ''',
)

_add(
    "insertion_sort",
    "lists",
    "insertion_sort",
    '''
    """Insertion sort: O(n^2) sort that performs well on nearly-sorted data."""


    def insertion_sort(items: list) -> list:
        result = list(items)
        for i in range(1, len(result)):
            key = result[i]
            j = i - 1
            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = key
        return result
    ''',
)

_add(
    "merge_sort",
    "lists",
    "merge_sort",
    '''
    """Merge sort: O(n log n) stable divide-and-conquer sort."""


    def merge_sort(items: list) -> list:
        if len(items) <= 1:
            return list(items)
        mid = len(items) // 2
        left, right = merge_sort(items[:mid]), merge_sort(items[mid:])
        merged, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    ''',
)

_add(
    "quick_sort",
    "lists",
    "quick_sort",
    '''
    """Quick sort using the Lomuto partition scheme (not in-place, for clarity)."""


    def quick_sort(items: list) -> list:
        if len(items) <= 1:
            return list(items)
        pivot = items[len(items) // 2]
        lesser = [x for x in items if x < pivot]
        equal = [x for x in items if x == pivot]
        greater = [x for x in items if x > pivot]
        return quick_sort(lesser) + equal + quick_sort(greater)
    ''',
)

# ------------------------------------------------------- data structures --

_add(
    "stack",
    "data_structures",
    "Stack",
    '''
    """A minimal LIFO stack backed by a Python list."""


    class Stack:
        def __init__(self) -> None:
            self._items: list = []

        def push(self, item) -> None:
            self._items.append(item)

        def pop(self):
            if not self._items:
                raise IndexError("pop from empty stack")
            return self._items.pop()

        def peek(self):
            if not self._items:
                raise IndexError("peek from empty stack")
            return self._items[-1]

        def is_empty(self) -> bool:
            return not self._items

        def __len__(self) -> int:
            return len(self._items)
    ''',
)

_add(
    "queue",
    "data_structures",
    "Queue",
    '''
    """A minimal FIFO queue backed by collections.deque."""
    from collections import deque


    class Queue:
        def __init__(self) -> None:
            self._items: deque = deque()

        def enqueue(self, item) -> None:
            self._items.append(item)

        def dequeue(self):
            if not self._items:
                raise IndexError("dequeue from empty queue")
            return self._items.popleft()

        def is_empty(self) -> bool:
            return not self._items

        def __len__(self) -> int:
            return len(self._items)
    ''',
)

_add(
    "linked_list",
    "data_structures",
    "LinkedList",
    '''
    """A minimal singly linked list with append and to_list."""
    from __future__ import annotations


    class _Node:
        def __init__(self, value) -> None:
            self.value = value
            self.next: "_Node | None" = None


    class LinkedList:
        def __init__(self) -> None:
            self._head: "_Node | None" = None

        def append(self, value) -> None:
            node = _Node(value)
            if self._head is None:
                self._head = node
                return
            current = self._head
            while current.next:
                current = current.next
            current.next = node

        def to_list(self) -> list:
            result = []
            current = self._head
            while current:
                result.append(current.value)
                current = current.next
            return result
    ''',
)

_add(
    "binary_tree",
    "data_structures",
    "BinaryTree",
    '''
    """A minimal binary search tree with insert and in-order traversal."""
    from __future__ import annotations


    class TreeNode:
        def __init__(self, value) -> None:
            self.value = value
            self.left: "TreeNode | None" = None
            self.right: "TreeNode | None" = None

        def insert(self, value) -> None:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)

        def inorder(self) -> list:
            left = self.left.inorder() if self.left else []
            right = self.right.inorder() if self.right else []
            return left + [self.value] + right
    ''',
)

_add(
    "min_stack",
    "data_structures",
    "MinStack",
    '''
    """A stack that supports retrieving the minimum element in O(1)."""


    class MinStack:
        def __init__(self) -> None:
            self._items: list = []
            self._minimums: list = []

        def push(self, item) -> None:
            self._items.append(item)
            current_min = min(item, self._minimums[-1]) if self._minimums else item
            self._minimums.append(current_min)

        def pop(self):
            self._minimums.pop()
            return self._items.pop()

        def get_min(self):
            if not self._minimums:
                raise IndexError("get_min from empty stack")
            return self._minimums[-1]
    ''',
)

# -------------------------------------------------------------- misc/dec --

_add(
    "memoize_decorator",
    "misc",
    "memoize",
    '''
    """A simple memoization decorator for pure functions."""
    from functools import wraps


    def memoize(func):
        cache = {}

        @wraps(func)
        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]

        return wrapper
    ''',
)

_add(
    "timer_decorator",
    "misc",
    "timer",
    '''
    """A decorator that prints how long a function took to run."""
    import time
    from functools import wraps


    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"{func.__name__} took {elapsed:.6f}s")
            return result

        return wrapper
    ''',
)

_add(
    "retry_decorator",
    "misc",
    "retry",
    '''
    """A decorator that retries a function a fixed number of times on
    exception, with optional delay between attempts."""
    import time
    from functools import wraps


    def retry(times: int = 3, delay: float = 0.0, exceptions=(Exception,)):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                last_exc = None
                for attempt in range(1, times + 1):
                    try:
                        return func(*args, **kwargs)
                    except exceptions as exc:
                        last_exc = exc
                        if attempt < times and delay:
                            time.sleep(delay)
                raise last_exc

            return wrapper

        return decorator
    ''',
)

_add(
    "flatten_dict",
    "misc",
    "flatten_dict",
    '''
    """Flatten a nested dictionary into dotted-key form,
    e.g. {"a": {"b": 1}} -> {"a.b": 1}."""


    def flatten_dict(nested: dict, parent_key: str = "", sep: str = ".") -> dict:
        items: dict = {}
        for key, value in nested.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                items.update(flatten_dict(value, new_key, sep=sep))
            else:
                items[new_key] = value
        return items
    ''',
)

_add(
    "chunked_reader",
    "misc",
    "read_in_chunks",
    '''
    """Read a file lazily in fixed-size chunks, useful for large files."""
    from collections.abc import Iterator


    def read_in_chunks(file_path: str, chunk_size: int = 8192) -> Iterator[str]:
        with open(file_path, "r", encoding="utf-8") as handle:
            while True:
                chunk = handle.read(chunk_size)
                if not chunk:
                    break
                yield chunk
    ''',
)

_add(
    "singleton_decorator",
    "misc",
    "singleton",
    '''
    """A class decorator that turns a class into a singleton."""
    from functools import wraps


    def singleton(cls):
        instances = {}

        @wraps(cls)
        def get_instance(*args, **kwargs):
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]

        return get_instance
    ''',
)
