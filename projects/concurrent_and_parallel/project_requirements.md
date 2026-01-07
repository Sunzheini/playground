# Project: Concurrent and Parallel Programming in Python

## Implements asynchrony and non-blocking environment concepts
1. Description
Without asynchronous language capability, every call of methods, functions, or action execution 
would result in a blocking environment and use only one thread. The blocking environment means 
that in case of heavy computations and executions of the asynchronous operation(i.e., call to API), 
everything in the application would be queued and waiting for the current execution to finish, 
causing a significant decline in the end-user experience. Python provides approaches and methods 
that enable the execution of heavy CPU and asynchronous operations in a non-blocking way.

2. Skills
Uses of asynchronous functions: definition and execution
Uses of asynchronous event loops
Uses of asynchronous objects: tasks and futures
Uses of asynchronous communication techniques: transports and protocols

3. Knowledge
Difference between Concurrency and Parallelism
Definition and difference between IO-bound and CPU-bound operations
Definition of Process, Thread, and Coroutine
What is the purpose of await and async keywords?
Describe how to run a code asynchronously
What's the difference between the coroutines and generators?

## Implements concurrency concepts by using language capabilities
1. Description
In simple words, concurrency is a process in which multiple operations are executed simultaneously 
in parallel, and programming languages support concurrency differently. Multiple threads language 
concurrences are usually supported natively with the built-in approaches in the language itself. 
There are numerous implementations for single threads on executing operations in parallel.

2. Skills
Uses multiple processes and multiprocessing library along with ProcessPoolExecutor API
Uses multiple threads and threading library along with ThreadPoolExecutor API

3. Knowledge
Differences between process and thread
Describe the GIL's primary purpose and limitations
What is a thread-/process-pool? What are the benefits of using pool API?
Is it possible to start already finished Thread object once again?
How to start thread/process in Python?
Do threads have states in Python?
Is it possible to run another program in a separate process from Python code?
