from typing import List, Dict, Tuple, Set, Optional

"""
The typing module provides runtime support for type hints (introduced in Python 3.5+),
enabling better code documentation, IDE support, and static type checking with tools
like mypy.
"""

# Variable annotations
name: str = "Alice"
age: int = 30
scores: List[float] = [89.5, 92.0, 95.5]
flags: Dict[str, bool] = {"logged_in": True, "is_admin": False}

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Optional types (None or Type)
def get_user(id: int) -> Optional[Dict[str, str]]:
    return {"name": "Alice"} if id == 1 else None
