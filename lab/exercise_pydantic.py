"""
Pydantic is a data validation and settings management library that:
    Enforces type hints at runtime
    Provides detailed error messages when data is invalid
    Supports complex data structures (nested models, JSON Schema)
    Integrates with FastAPI (for web APIs) and other frameworks
"""
from pydantic import (
    BaseModel, ValidationError, Field, field_validator,
    model_validator, computed_field
)
from pydantic_settings import BaseSettings
from typing import Optional


# ============================================================================
# 1. BASIC BaseModel USAGE
# ============================================================================
class User(BaseModel):
    name: str
    age: int
    email: str | None = None  # Optional field

# Validates data automatically
try:
    user = User(name="Alice", age="30")  # Input gets coerced to correct types
    print(f"1. Basic User: {user.name}, age={user.age}")
except ValidationError as e:
    print(e)


# ============================================================================
# 2. DUMP METHODS (Serialization)
# ============================================================================
class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True

product = Product(name="Laptop", price=999.99)

# model_dump() - returns Python dict
print(f"\n2a. model_dump(): {product.model_dump()}")

# model_dump_json() - returns JSON string
print(f"2b. model_dump_json(): {product.model_dump_json()}")

# Exclude fields
print(f"2c. Exclude fields: {product.model_dump(exclude={'price'})}")

# Include only specific fields
print(f"2d. Include only: {product.model_dump(include={'name', 'price'})}")


# ============================================================================
# 3. FIELD USAGE (Field constraints and metadata)
# ============================================================================
class Employee(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Employee name")
    employee_id: int = Field(..., gt=0, description="Must be positive")
    salary: float = Field(default=50000.0, ge=0, description="Annual salary")
    department: str = Field(default="General", alias="dept")  # Alias for input

emp = Employee(name="Bob", employee_id=123, dept="IT")  # Using alias
print(f"\n3. Employee with Field: {emp.name}, ID={emp.employee_id}, Dept={emp.department}")


# ============================================================================
# 4. FIELD_VALIDATOR (Validate individual fields)
# ============================================================================
class UserAccount(BaseModel):
    username: str
    email: str
    age: int

    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v.lower()  # Normalize to lowercase

    @field_validator('age')
    @classmethod
    def age_must_be_adult(cls, v: int) -> int:
        if v < 18:
            raise ValueError('Must be 18 or older')
        return v

try:
    account = UserAccount(username="Alice123", email="alice@example.com", age=25)
    print(f"\n4. Field validator passed: {account.username}")
except ValidationError as e:
    print(f"Validation error: {e}")


# ============================================================================
# 5. MODEL_VALIDATOR (Validate entire model)
# ============================================================================
class DateRange(BaseModel):
    start_date: int
    end_date: int

    @model_validator(mode='after')
    def check_dates(self) -> 'DateRange':
        if self.end_date < self.start_date:
            raise ValueError('end_date must be after start_date')
        return self

try:
    date_range = DateRange(start_date=20250101, end_date=20250201)
    print(f"\n5. Model validator passed: {date_range.start_date} to {date_range.end_date}")
except ValidationError as e:
    print(f"Model validation error: {e}")


# ============================================================================
# 6. COMPUTED_FIELD (Derived properties)
# ============================================================================
class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height

rect = Rectangle(width=10, height=5)
print(f"\n6. Computed field: Rectangle area = {rect.area}")
print(f"   Serialized: {rect.model_dump()}")  # Includes computed field


# ============================================================================
# 7. STRICT MODE (No type coercion)
# ============================================================================
class StrictUser(BaseModel):
    model_config = {'strict': True}  # Enable strict mode

    name: str
    age: int

try:
    # This will fail because "30" is a string, not an int
    strict_user = StrictUser(name="Charlie", age="30")
except ValidationError as e:
    print(f"\n7. Strict mode error (expected): age must be int, not str")

# This works
strict_user_ok = StrictUser(name="Charlie", age=30)
print(f"   Strict mode success: {strict_user_ok.name}, {strict_user_ok.age}")


# ============================================================================
# 8. BaseSettings (Environment variables and settings management)
# ============================================================================
class AppSettings(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False
    max_connections: int = Field(default=100, ge=1)
    api_key: Optional[str] = None

    model_config = {
        'env_prefix': 'APP_',  # Environment variables like APP_DEBUG
        'env_file': '.env',     # Load from .env file if exists
        'extra': 'ignore'       # Ignore extra fields
    }

settings = AppSettings()
print(f"\n8. BaseSettings: app={settings.app_name}, debug={settings.debug}, max_conn={settings.max_connections}")


# ============================================================================
# 9. NESTED MODELS
# ============================================================================
class Address(BaseModel):
    street: str
    city: str
    country: str = "USA"

class Company(BaseModel):
    name: str
    address: Address
    employees: list[str]

company = Company(
    name="TechCorp",
    address={"street": "123 Main St", "city": "Boston"},
    employees=["Alice", "Bob"]
)
print(f"\n9. Nested models: {company.name} in {company.address.city}")


# ============================================================================
# 10. MODEL CONFIGURATION
# ============================================================================
class ConfigExample(BaseModel):
    model_config = {
        'str_strip_whitespace': True,   # Strip whitespace from strings
        'validate_assignment': True,     # Validate on attribute assignment
        'frozen': False,                 # Allow mutation (True = immutable)
        'populate_by_name': True,        # Allow population by field name or alias
    }

    name: str = Field(alias="userName")
    value: int

config_ex = ConfigExample(userName="  Test  ", value=42)
print(f"\n10. Config (stripped): '{config_ex.name}', value={config_ex.value}")


print("\n" + "="*70)
print("All Pydantic examples completed successfully!")
print("="*70)
