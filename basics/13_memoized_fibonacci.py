"""
Goal: Write a function to calculate the nth Fibonacci number.
1. Write a recursive version (which is extremely slow for large n).
2. Optimize it using the `@lru_cache` decorator.
3. Take user input for n and compare execution times.
"""

from functools import lru_cache
import time

@lru_cache(maxsize=None)  # maxsize=None means unlimited caching
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Try n = 35. Without cache it takes ~5 seconds. With cache, less than a millisecond!
n = 35
start = time.time()
result = fib(n)
end = time.time()
print(f"{n}th Fibonacci number: {result}")
print(f"Execution time: {(end - start)*1000:.2f} milliseconds")