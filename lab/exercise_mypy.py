# ===== No ERRORS =====
from typing import List, Dict


def greet(name: str) -> str:
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    return a + b

# ===== TYPE ERRORS =====

# 1. Function call with wrong argument types
result1 = add_numbers(5, "hello")  # Error: string instead of int
result2 = add_numbers(3.14, 2)     # Error: float instead of int

# 2. Variable type mismatches
name = 123  # Error: assigning int to str variable
age = "thirty"  # Error: assigning str to int variable

# 3. List type violations
numbers: List[int] = [1, 2, 3, "four"]  # Error: string in int list

# 4. Dictionary type violations
counts: Dict[str, int] = {"apples": 5, "oranges": "three"}  # Error: string value

# 5. Return type mismatch
def get_age() -> int:
    return "25"  # Error: returning string instead of int

# 6. Missing required arguments
greet()  # Error: missing argument 'name'


# run with `mypy .\lab\exercise_mypy.py`