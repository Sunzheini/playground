# Python program to measure elapsed time using perf_counter()
from time import perf_counter, sleep

def measure_elapsed_time():
    # Start the timer
    start_time = perf_counter()

    # Simulate work (10 iterations with 0.1s delay each)
    for _ in range(20):
        sleep(0.1)  # Simulating task processing

    # Stop the timer
    end_time = perf_counter()

    # Calculate and display results
    elapsed_time = end_time - start_time
    print(f"Start Time: {start_time:.6f} seconds")
    print(f"End Time: {end_time:.6f} seconds")
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")

measure_elapsed_time()