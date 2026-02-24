"""
This file demonstrates how to use pytest for testing a simple Calculator class. It includes
examples of fixtures, parametrized tests, exception testing, and more.

pytest vs unittest:
- pytest is more concise and has powerful features like fixtures and parametrization.
- pytest has better support for test discovery and more informative failure reports.
- pytest allows for more flexible test organization and supports a wider range of testing styles.
- pytest has a rich ecosystem of plugins for additional functionality (e.g., coverage, parallel
testing).
- pytest is generally more popular in the Python community for new projects, while unittest is often
used in legacy codebases or when a more traditional testing style is preferred.
- pytest uses simple assert statements for test assertions, while unittest requires specific
assertion methods (e.g., self.assertEqual).
- pytest allows for more dynamic test generation and parametrization, while unittest typically
requires more boilerplate code for similar functionality.
- pytest has a more flexible fixture system that can be used for setup and teardown, while unittest
relies on setUp and tearDown methods within test classes.
- unittest is part of the standard library and follows a more traditional xUnit style.
"""

"""
At its heart, pytest is built on a plugin system powered by a library called pluggy . This means 
that almost every feature of pytest—from test discovery to reporting—is implemented as a plugin. 
This architecture allows you to intercept and modify pytest's behavior at specific points in the 
test lifecycle using "hook functions"

For most projects, you'll begin by creating a conftest.py file in your tests directory. This
file is automatically discovered by pytest and acts as a built-in, project-specific plugin. It's
the perfect place to define custom fixtures, hooks, and configuration that you want to be available
across all your test files. By using conftest.py, you can keep your test code clean and organized
while still having access to powerful setup and teardown functionality provided by fixtures.
"""
import pytest


class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        return self.history.copy()

    def clear_history(self):
        self.history.clear()


# ============= FIXTURES =============
"""
Automatic execution (autouse=True):
    - The fixture runs without being explicitly requested in test functions
    - You don't need to add it as a parameter to test functions

Session scope (scope="session"):
    - Runs once at the beginning of the test session
    - Shared across all tests in the session
    - Fixture is not torn down until all tests complete
    - When you don't specify a scope, pytest uses scope="function" as the default
"""
@pytest.fixture
def example_fixture():
    """An example fixture that runs before each test"""
    print("\nSetting up example fixture before test")
    yield   # Test runs happen here and after yield is teardown
    print("\nTearing down example fixture after test")


@pytest.fixture(scope="session", autouse=True)
def example_fixture2():
    """Session-scoped fixture example"""
    print("\nSetting up session-scoped fixture before any tests")
    yield   # All tests run here
    print("\nTearing down session-scoped fixture after all tests")


@pytest.fixture
def calc():
    """Fixture that provides a fresh Calculator instance for each test"""
    return Calculator()


@pytest.fixture
def calc_with_history():
    """Fixture that provides a Calculator with some pre-existing history"""
    calc = Calculator()
    calc.add(5, 3)
    calc.multiply(2, 4)
    return calc


@pytest.fixture(scope="session")
def test_data():
    """Session-scoped fixture - created once for entire test session"""
    return {
        'positive_numbers': [1, 2, 3, 10, 100],
        'negative_numbers': [-1, -5, -10],
        'zero_values': [0, 0.0],
        'large_numbers': [1000000, 999999999]
    }


# ============= BASIC TESTS =============
def test_addition(calc):
    """Test basic addition functionality"""
    result = calc.add(2, 3)
    assert result == 5


def test_subtraction(calc):
    """Test basic subtraction functionality"""
    result = calc.subtract(5, 3)
    assert result == 2


def test_multiplication(calc):
    """Test basic multiplication functionality"""
    result = calc.multiply(4, 3)
    assert result == 12


def test_division(calc):
    """Test basic division functionality"""
    result = calc.divide(10, 2)
    assert result == 5.0


# ============= EXCEPTION TESTING =============
def test_division_by_zero_raises_error(calc):
    """Test that division by zero raises ValueError"""
    with pytest.raises(ValueError) as excinfo:
        calc.divide(5, 0)

    assert str(excinfo.value) == "Cannot divide by zero"


def test_division_by_zero_with_message_check(calc):
    """Alternative way to test exceptions with specific message"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)


# ============= PARAMETRIZED TESTS =============
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, -50, 50),
    (1.5, 2.5, 4.0),
])
def test_addition_parametrized(calc, a, b, expected):
    """Test addition with multiple parameter combinations"""
    result = calc.add(a, b)
    assert result == expected


@pytest.mark.parametrize("operation, a, b, expected", [
    ("add", 2, 3, 5),
    ("subtract", 10, 4, 6),
    ("multiply", 3, 4, 12),
    ("divide", 15, 3, 5.0),
])
def test_operations_parametrized(calc, operation, a, b, expected):
    """Test multiple operations with parametrization"""
    method = getattr(calc, operation)
    result = method(a, b)
    assert result == expected


# ============= HISTORY FUNCTIONALITY TESTS =============
def test_history_tracking(calc):
    """Test that operations are properly recorded in history"""
    calc.add(5, 3)
    calc.multiply(2, 4)

    history = calc.get_history()
    assert len(history) == 2
    assert "5 + 3 = 8" in history
    assert "2 * 4 = 8" in history


def test_history_is_copied(calc):
    """Test that get_history returns a copy, not the original list"""
    calc.add(1, 1)
    history1 = calc.get_history()
    history2 = calc.get_history()

    # Modifying one shouldn't affect the other
    history1.append("fake entry")
    assert len(history2) == 1


def test_clear_history(calc_with_history):
    """Test clearing calculator history"""
    assert len(calc_with_history.get_history()) > 0  # Pre-condition

    calc_with_history.clear_history()
    assert len(calc_with_history.get_history()) == 0


# ============= PROPERTY-BASED TESTING =============
def test_addition_is_commutative(calc, test_data):
    """Test that addition is commutative (a + b = b + a)"""
    for a in test_data['positive_numbers']:
        for b in test_data['positive_numbers']:
            result1 = Calculator().add(a, b)  # Fresh calc to avoid history mixing
            result2 = Calculator().add(b, a)
            assert result1 == result2, f"Addition not commutative for {a} and {b}"


def test_multiplication_by_zero(calc, test_data):
    """Test that anything multiplied by zero equals zero"""
    all_numbers = (test_data['positive_numbers'] +
                   test_data['negative_numbers'] +
                   test_data['large_numbers'])

    for num in all_numbers:
        assert calc.multiply(num, 0) == 0
        # Create fresh calc for each test to avoid history interference
        calc = Calculator()


# ============= FIXTURES WITH CLEANUP =============
@pytest.fixture
def temp_file():
    """Fixture that creates and cleans up a temporary file"""
    import tempfile
    import os

    # Setup
    fd, path = tempfile.mkstemp()
    os.close(fd)

    yield path  # This is what gets passed to the test

    # Cleanup
    if os.path.exists(path):
        os.remove(path)


def test_calculator_can_save_history_to_file(calc, temp_file):
    """Example test using a fixture with cleanup"""
    calc.add(1, 2)
    calc.multiply(3, 4)

    # Save history to file
    with open(temp_file, 'w') as f:
        for entry in calc.get_history():
            f.write(entry + '\n')

    # Read it back and verify
    with open(temp_file, 'r') as f:
        lines = f.read().strip().split('\n')

    assert len(lines) == 2
    assert "1 + 2 = 3" in lines
    assert "3 * 4 = 12" in lines


# ============= MARKS AND CONDITIONAL TESTING =============
@pytest.mark.slow
def test_large_calculations(calc):
    """Test marked as slow - can be skipped with -m "not slow" """
    result = calc.multiply(999999, 999999)
    assert result == 999998000001


@pytest.mark.skipif(True, reason="Skipping this test for demo purposes")
def test_skipped_example(calc):
    """This test will be skipped"""
    assert calc.add(1, 1) == 2


@pytest.mark.xfail(reason="Known bug - fix pending")
def test_expected_failure(calc):
    """This test is expected to fail"""
    # This would fail, but pytest knows it should fail
    assert calc.divide(1, 0) == float('inf')


# ============= TESTING WITH MOCK DATA =============
def test_calculator_with_complex_workflow(calc):
    """Test a complex workflow with multiple operations"""
    # Perform a series of calculations
    calc.add(10, 5)  # 15
    result1 = calc.subtract(20, 8)  # 12
    result2 = calc.multiply(result1, 2)  # 24
    final_result = calc.divide(result2, 3)  # 8.0

    assert final_result == 8.0
    assert len(calc.get_history()) == 4

    # Check that all operations are in history
    history = calc.get_history()
    assert any("10 + 5 = 15" in entry for entry in history)
    assert any("20 - 8 = 12" in entry for entry in history)
    assert any("12 * 2 = 24" in entry for entry in history)
    assert any("24 / 3 = 8.0" in entry for entry in history)


# ============= CONFIGURATION AND SETUP =============
# Create a pytest.ini file in your project root:
"""
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    unit: marks tests as unit tests
"""


# to debug right click on the test and select "Debug ..."
# pytest - k "llm_query" to execute a test by keyword


# ============= RUNNING THE TESTS =============
"""
Basic commands:

# Run all tests
pytest

# Run all tests and see print statements
pytest -s

# Run with verbose output
pytest -v

# Run specific test file
pytest test_calculator.py

# Run specific test
pytest test_calculator.py::test_addition

# Run tests matching pattern
pytest -k "addition"

# Skip slow tests
pytest -m "not slow"

# Run only slow tests
pytest -m "slow"

# Generate coverage report
pytest --cov=calculator

# Run with detailed output on failures
pytest -vvv --tb=long

# Run in parallel (requires pytest-xdist)
pytest -n auto
"""
