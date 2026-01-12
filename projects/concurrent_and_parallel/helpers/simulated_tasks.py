"""
This module provides simulated CPU-intensive, IO-intensive, and mixed tasks
for demonstrating concurrency and parallelism concepts.
"""
import time


def cpu_intensive_task(n: int) -> int:
    """Heavy CPU task."""
    result = 0
    for i in range(n):
        result += i * i
        result = (result * 997) % (n + 1)  # Extra computation
        result ^= i  # Bitwise operation
        result = result // 7 if result % 7 == 0 else result * 3

    # Add another heavy loop
    for i in range(n // 10):
        for j in range(10):
            result += (i * j) ** 0.5
            result = result % 1000007

    return result


def io_intensive_task(n: int) -> int:
    """IO-intensive task: simulate API/database calls and file operations."""
    # Simulate network delay with varying sleep times
    delay = (n % 100) * 0.0002
    time.sleep(delay)

    # Simulate file I/O by creating and reading from memory (not actual disk)
    data = b"x" * 1000  # Simulate reading 1KB of data
    processed = len(data) * n

    # Another sleep to simulate network response time
    time.sleep(delay * 0.5)
    return processed


def mixed_task(n: int) -> int:
    """Properly scaled mixed task."""
    result = 0

    cpu_work = n // 10  # 400k iterations for n=4M
    for i in range(cpu_work):
        result += i * i * i

    # IO: Meaningful sleep
    sleep_time = min(0.5, n / 10000000)  # Up to 0.5s for large n
    time.sleep(sleep_time)

    # More CPU
    for i in range(cpu_work // 2):
        result = (result * 13 + i) % 1000000

    return result
