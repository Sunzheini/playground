"""
A module containing helper functions for concurrency and parallelism projects.
"""
def counter(number: int, q=None) -> None:
    """
    A simple counting function that counts up to a specified number.
    Optionally puts the result into a queue for inter-process communication.
    :param number: The number to count up to.
    :param q: An optional Queue to put the result into.
    :return: None
    """
    count = 0
    for _ in range(number):
        count += 1

    if q is not None:
        q.put(count)  # put the result into the queue
