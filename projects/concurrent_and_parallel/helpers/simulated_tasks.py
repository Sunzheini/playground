"""
This module provides simulated CPU-intensive, IO-intensive, and mixed tasks
for demonstrating concurrency and parallelism concepts.
"""
import time


def cpu_intensive_task(n: int) -> int:
    """CPU-intensive task: calculate sum of squares (computationally heavy)."""
    result = 0
    for i in range(n):
        result += i * i
    for i in range(n // 100):
        result = (result * i) % (n + 1)
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
    """Mixed CPU + IO task: demonstrates both types of operations."""
    # CPU phase: some computation
    cpu_result = 0
    for i in range(n // 10):
        cpu_result += i ** 1.5

    # IO phase: simulate waiting
    time.sleep(max(0.001, (n % 50) * 0.0001))

    # Again CPU work
    for i in range(n // 20):
        cpu_result = (cpu_result + i) % 1000

    return cpu_result
