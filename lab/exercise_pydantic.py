from pydantic import BaseModel, ValidationError
"""
Pydantic is a data validation and settings management library that:
    Enforces type hints at runtime
    Provides detailed error messages when data is invalid
    Supports complex data structures (nested models, JSON Schema)
    Integrates with FastAPI (for web APIs) and other frameworks
"""


class User(BaseModel):
    name: str
    age: int
    email: str | None = None  # Optional field

# Validates data automatically
try:
    user = User(name="Alice", age="30")  # Input gets coerced to correct types
    print(user.age)  # 30 (int, not str)
except ValidationError as e:
    print(e)  # Detailed error if validation fails
