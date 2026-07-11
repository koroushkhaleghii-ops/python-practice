"""
Goal: Write a program that takes a range (e.g., 10 to 50) and:
1. Lists all prime numbers within that range.
2. Counts the composite (non-prime) numbers.
3. If a number is less than 2, print "Invalid number".
"""

import math

def is_prime(n):
    if n < 2:
        return False
    # Loop only up to the square root - practicing Big-O optimization
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:
            return False
    return True

start = 10
end = 50
prime_list = []
composite_count = 0

for num in range(start, end + 1):
    if is_prime(num):
        prime_list.append(num)
    elif num > 1:  # Count composites
        composite_count += 1

print(f"Prime numbers between {start} and {end}: {prime_list}")
print(f"Total composite numbers: {composite_count}")