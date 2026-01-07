"""
A module containing helper functions for concurrency and parallelism projects.
"""
def counter(n: int, queue = None, process_id = None):
    """
    Counter function that puts result in queue
    :param n: The number to count up to.
    :param queue: The multiprocessing queue to put results into.
    :param process_id: The ID of the process.
    """
    count = 0
    for i in range(n):
        count += 1

    if queue:
        queue.put({
            'process_id': process_id,
            'count': count,
            'completed': True
        })

    return count
