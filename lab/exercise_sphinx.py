"""
Sphinx Documentation Generator Example
======================================

Sphinx is a powerful documentation generator that converts reStructuredText (reST)
files into HTML, PDF, and other formats. It's widely used for Python projects.

Installation:
    pip install sphinx sphinx-rtd-theme

Quick Start:
    1. sphinx-quickstart docs/
    2. Edit docs/conf.py and docs/index.rst
    3. sphinx-build -b html docs/ docs/_build/html
    4. Open docs/_build/html/index.html in browser

Features:
    - Automatic API documentation from docstrings
    - Multiple output formats (HTML, PDF, LaTeX, ePub)
    - Cross-referencing and indexing
    - Syntax highlighting
    - Extensions for various features
    - Beautiful themes (ReadTheDocs, Alabaster, etc.)
"""

import math
from typing import List, Optional, Union
from datetime import datetime


# ============================================================================
# Example 1: Google Style Docstrings (Popular with Sphinx)
# ============================================================================

class Calculator:
    """
    A simple calculator class demonstrating Google-style docstrings.

    This class provides basic arithmetic operations and serves as an example
    of how to write documentation that Sphinx can process.

    Args:
        name (str): The name of this calculator instance.
        precision (int, optional): Number of decimal places for results. Defaults to 2.

    Attributes:
        name (str): The calculator's name.
        precision (int): Decimal precision for calculations.
        history (List[str]): History of calculations performed.

    Example:
        >>> calc = Calculator("MyCalc")
        >>> result = calc.add(5, 3)
        >>> print(result)
        8.0

    Note:
        This class is for demonstration purposes only.

    See Also:
        :class:`ScientificCalculator`: For advanced calculations.
    """

    def __init__(self, name: str, precision: int = 2):
        """Initialize the calculator with a name and precision."""
        self.name = name
        self.precision = precision
        self.history: List[str] = []

    def add(self, a: float, b: float) -> float:
        """
        Add two numbers together.

        Args:
            a (float): First number to add.
            b (float): Second number to add.

        Returns:
            float: Sum of a and b, rounded to the specified precision.

        Raises:
            TypeError: If inputs are not numeric.

        Example:
            >>> calc = Calculator("Test")
            >>> calc.add(10.5, 20.3)
            30.8
        """
        result = round(a + b, self.precision)
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """
        Subtract b from a.

        Args:
            a (float): Number to subtract from.
            b (float): Number to subtract.

        Returns:
            float: Difference of a and b.
        """
        result = round(a - b, self.precision)
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.

        Args:
            a (float): First multiplicand.
            b (float): Second multiplicand.

        Returns:
            float: Product of a and b.
        """
        result = round(a * b, self.precision)
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """
        Divide a by b.

        Args:
            a (float): Dividend (number to be divided).
            b (float): Divisor (number to divide by).

        Returns:
            float: Quotient of a divided by b.

        Raises:
            ZeroDivisionError: If b is zero.

        Warning:
            Division by zero will raise an exception.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = round(a / b, self.precision)
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self) -> List[str]:
        """
        Get the calculation history.

        Returns:
            List[str]: List of all calculations performed.
        """
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear()


# ============================================================================
# Example 2: NumPy Style Docstrings (Alternative format)
# ============================================================================

class ScientificCalculator(Calculator):
    """
    Advanced calculator with scientific functions.

    Extends the basic Calculator with trigonometric and logarithmic functions.
    This class demonstrates NumPy-style docstrings.

    Parameters
    ----------
    name : str
        The name of this calculator instance.
    precision : int, optional
        Number of decimal places for results (default is 4).
    angle_mode : str, optional
        'radians' or 'degrees' for trigonometric functions (default is 'radians').

    Attributes
    ----------
    angle_mode : str
        Current angle mode for trigonometric operations.

    Examples
    --------
    >>> sci_calc = ScientificCalculator("SciCalc", angle_mode='degrees')
    >>> sci_calc.sin(90)
    1.0

    >>> sci_calc.power(2, 3)
    8.0
    """

    def __init__(self, name: str, precision: int = 4, angle_mode: str = "radians"):
        """Initialize scientific calculator."""
        super().__init__(name, precision)
        self.angle_mode = angle_mode

    def power(self, base: float, exponent: float) -> float:
        """
        Raise base to the power of exponent.

        Parameters
        ----------
        base : float
            The base number.
        exponent : float
            The exponent to raise the base to.

        Returns
        -------
        float
            base raised to the power of exponent.

        Examples
        --------
        >>> calc = ScientificCalculator("Test")
        >>> calc.power(2, 3)
        8.0
        >>> calc.power(5, 0.5)
        2.236
        """
        result = round(base ** exponent, self.precision)
        self.history.append(f"{base}^{exponent} = {result}")
        return result

    def sqrt(self, x: float) -> float:
        """
        Calculate square root of x.

        Parameters
        ----------
        x : float
            Number to find square root of (must be non-negative).

        Returns
        -------
        float
            Square root of x.

        Raises
        ------
        ValueError
            If x is negative.
        """
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = round(math.sqrt(x), self.precision)
        self.history.append(f"√{x} = {result}")
        return result

    def sin(self, angle: float) -> float:
        """
        Calculate sine of angle.

        Parameters
        ----------
        angle : float
            Angle in radians or degrees (depending on angle_mode).

        Returns
        -------
        float
            Sine of the angle.
        """
        rad = math.radians(angle) if self.angle_mode == "degrees" else angle
        result = round(math.sin(rad), self.precision)
        self.history.append(f"sin({angle}) = {result}")
        return result

    def cos(self, angle: float) -> float:
        """
        Calculate cosine of angle.

        Parameters
        ----------
        angle : float
            Angle in radians or degrees (depending on angle_mode).

        Returns
        -------
        float
            Cosine of the angle.
        """
        rad = math.radians(angle) if self.angle_mode == "degrees" else angle
        result = round(math.cos(rad), self.precision)
        self.history.append(f"cos({angle}) = {result}")
        return result

    def log(self, x: float, base: float = math.e) -> float:
        """
        Calculate logarithm of x to the given base.

        Parameters
        ----------
        x : float
            The number (must be positive).
        base : float, optional
            The logarithm base (default is e for natural log).

        Returns
        -------
        float
            Logarithm of x to the given base.

        Raises
        ------
        ValueError
            If x is not positive or base is not valid.
        """
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Invalid logarithm base")
        result = round(math.log(x, base), self.precision)
        self.history.append(f"log_{base}({x}) = {result}")
        return result


# ============================================================================
# Example 3: Module-level Functions with Various Docstring Features
# ============================================================================

def factorial(n: int) -> int:
    """
    Calculate factorial of n (n!).

    The factorial of a non-negative integer n is the product of all positive
    integers less than or equal to n.

    Args:
        n (int): Non-negative integer to calculate factorial of.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.

    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1

    Note:
        - 0! is defined as 1
        - This implementation uses iteration, not recursion
        - Large values of n may cause integer overflow

    See Also:
        - :func:`fibonacci`: Calculate Fibonacci numbers
        - :func:`is_prime`: Check if number is prime

    .. versionadded:: 1.0
    .. versionchanged:: 1.1
       Added type hints and improved error handling.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int, use_cache: bool = True) -> int:
    """
    Calculate the nth Fibonacci number.

    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): Index of Fibonacci number to calculate (0-based).
        use_cache (bool, optional): Whether to use memoization. Defaults to True.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.

    Example:
        >>> fibonacci(10)
        55
        >>> [fibonacci(i) for i in range(7)]
        [0, 1, 1, 2, 3, 5, 8]

    Tip:
        Enable ``use_cache=True`` for better performance with large n.

    .. warning::
       Very large values of n may be slow without caching.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n <= 1:
        return n

    if use_cache:
        # Iterative approach with O(n) time, O(1) space
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    else:
        # Simple recursive (slow for large n)
        return fibonacci(n - 1, False) + fibonacci(n - 2, False)


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.

    Example:
        >>> is_prime(17)
        True
        >>> is_prime(18)
        False
        >>> [x for x in range(20) if is_prime(x)]
        [2, 3, 5, 7, 11, 13, 17, 19]

    Note:
        This uses trial division up to sqrt(n).
        For very large numbers, consider using probabilistic tests.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def format_currency(amount: float, currency: str = "USD") -> str:
    """
    Format a number as currency.

    Args:
        amount (float): The monetary amount to format.
        currency (str, optional): Currency code (USD, EUR, GBP, etc.). Defaults to "USD".

    Returns:
        str: Formatted currency string.

    Example:
        >>> format_currency(1234.56)
        '$1,234.56 USD'
        >>> format_currency(999.99, 'EUR')
        '€999.99 EUR'

    Todo:
        * Add support for more currencies
        * Implement locale-specific formatting
        * Add cryptocurrency support
    """
    symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
    }
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f} {currency}"


# ============================================================================
# Example 4: Data Classes and Type Hints
# ============================================================================

class User:
    """
    Represents a user in the system.

    Attributes:
        username (str): The user's unique username.
        email (str): The user's email address.
        created_at (datetime): When the user account was created.
        is_active (bool): Whether the user account is active.
        role (str): User's role (e.g., 'admin', 'user', 'guest').
    """

    def __init__(
        self,
        username: str,
        email: str,
        role: str = "user",
        is_active: bool = True
    ):
        """
        Create a new user.

        Args:
            username (str): Unique username (3-20 characters).
            email (str): Valid email address.
            role (str, optional): User role. Defaults to "user".
            is_active (bool, optional): Active status. Defaults to True.

        Raises:
            ValueError: If username or email is invalid.
        """
        if not 3 <= len(username) <= 20:
            raise ValueError("Username must be 3-20 characters")
        if "@" not in email:
            raise ValueError("Invalid email address")

        self.username = username
        self.email = email
        self.role = role
        self.is_active = is_active
        self.created_at = datetime.now()

    def activate(self) -> None:
        """Activate the user account."""
        self.is_active = True

    def deactivate(self) -> None:
        """Deactivate the user account."""
        self.is_active = False

    def change_role(self, new_role: str) -> None:
        """
        Change the user's role.

        Args:
            new_role (str): New role to assign.

        Example:
            >>> user = User("john", "john@example.com")
            >>> user.change_role("admin")
        """
        self.role = new_role

    def __repr__(self) -> str:
        """Return string representation of the user."""
        return f"User(username='{self.username}', email='{self.email}', role='{self.role}')"


# ============================================================================
# Example 5: Demonstration and Usage
# ============================================================================

def demonstrate_sphinx_features():
    """
    Demonstrate various features documented for Sphinx.

    This function exercises all the documented classes and functions,
    showing how they work together.

    Returns:
        dict: Summary of demonstration results.
    """
    print("=" * 70)
    print("SPHINX DOCUMENTATION EXAMPLE - FEATURE DEMONSTRATION")
    print("=" * 70)

    results = {}

    # Test Calculator
    print("\n1. Basic Calculator (Google-style docstrings):")
    print("-" * 70)
    calc = Calculator("BasicCalc", precision=2)
    print(f"Calculator: {calc.name}")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")
    print(f"History: {calc.get_history()}")
    results['basic_calc'] = True

    # Test ScientificCalculator
    print("\n2. Scientific Calculator (NumPy-style docstrings):")
    print("-" * 70)
    sci_calc = ScientificCalculator("SciCalc", precision=4, angle_mode="degrees")
    print(f"Calculator: {sci_calc.name}")
    print(f"2^8 = {sci_calc.power(2, 8)}")
    print(f"√16 = {sci_calc.sqrt(16)}")
    print(f"sin(90°) = {sci_calc.sin(90)}")
    print(f"cos(0°) = {sci_calc.cos(0)}")
    print(f"log(100, base=10) = {sci_calc.log(100, 10)}")
    results['scientific_calc'] = True

    # Test module functions
    print("\n3. Mathematical Functions:")
    print("-" * 70)
    print(f"5! = {factorial(5)}")
    print(f"Fibonacci(10) = {fibonacci(10)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 18 prime? {is_prime(18)}")
    print(f"Currency: {format_currency(1234.56)}")
    results['math_functions'] = True

    # Test User class
    print("\n4. User Management:")
    print("-" * 70)
    user = User("alice", "alice@example.com", role="user")
    print(f"Created user: {user}")
    print(f"User is active: {user.is_active}")
    user.change_role("admin")
    print(f"Changed role to: {user.role}")
    results['user_class'] = True

    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 70)

    return results


def print_sphinx_setup_guide():
    """Print a guide for setting up Sphinx documentation."""
    print("\n" + "=" * 70)
    print("SPHINX SETUP GUIDE")
    print("=" * 70 + "\n")

    print("STEP 1: Install Sphinx and theme")
    print("-" * 70)
    print("pip install sphinx sphinx-rtd-theme sphinx-autodoc-typehints\n")

    print("STEP 2: Initialize Sphinx in your project")
    print("-" * 70)
    print("cd your_project")
    print("mkdir docs")
    print("cd docs")
    print("sphinx-quickstart\n")
    print("Follow the prompts (accept defaults for most questions)\n")

    print("STEP 3: Configure docs/conf.py")
    print("-" * 70)
    conf_py = """
# Add to conf.py:
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',        # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',       # Support for Google/NumPy style docstrings
    'sphinx.ext.viewcode',       # Add links to source code
    'sphinx.ext.todo',           # Support for TODO items
    'sphinx_autodoc_typehints',  # Better type hint support
]

html_theme = 'sphinx_rtd_theme'  # ReadTheDocs theme
"""
    print(conf_py)

    print("\nSTEP 4: Create docs/index.rst")
    print("-" * 70)
    index_rst = """
Welcome to My Project's Documentation
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   examples
   api

API Reference
=============

.. automodule:: exercise_sphinx
   :members:
   :undoc-members:
   :show-inheritance:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    print(index_rst)

    print("\nSTEP 5: Generate API documentation")
    print("-" * 70)
    print("sphinx-apidoc -o docs/ . --force")
    print("This auto-generates .rst files from your Python modules\n")

    print("STEP 6: Build HTML documentation")
    print("-" * 70)
    print("sphinx-build -b html docs/ docs/_build/html")
    print("# Or use the Makefile:")
    print("cd docs")
    print("make html\n")

    print("STEP 7: View documentation")
    print("-" * 70)
    print("Open docs/_build/html/index.html in your web browser\n")

    print("COMMON SPHINX DIRECTIVES:")
    print("-" * 70)
    directives = """
.. note:: This is a note
.. warning:: This is a warning
.. code-block:: python
   
   def example():
       return "code example"

.. autoclass:: ClassName
   :members:

.. autofunction:: function_name

:param param_name: Description
:type param_name: type
:returns: Description
:rtype: return_type
:raises ExceptionType: When this happens
"""
    print(directives)

    print("\nUSEFUL EXTENSIONS:")
    print("-" * 70)
    print("- sphinx.ext.autodoc: Auto-generate from docstrings")
    print("- sphinx.ext.napoleon: Google/NumPy style docstrings")
    print("- sphinx.ext.intersphinx: Link to other project docs")
    print("- sphinx.ext.todo: TODO support")
    print("- sphinx.ext.coverage: Coverage statistics")
    print("- sphinx.ext.mathjax: Math equations")
    print("- sphinx_rtd_theme: ReadTheDocs theme")
    print("\n" + "=" * 70)


# ============================================================================
# Main Execution
# ============================================================================

def main():
    """Main function to demonstrate Sphinx documentation features."""
    try:
        # Demonstrate documented features
        demonstrate_sphinx_features()

        # Print setup guide
        print_sphinx_setup_guide()

        print("\n" + "=" * 70)
        print("KEY POINTS:")
        print("=" * 70)
        print("✓ Use clear, detailed docstrings for all public APIs")
        print("✓ Support Google or NumPy style for parameters/returns")
        print("✓ Include examples in docstrings using doctests")
        print("✓ Use type hints for better documentation")
        print("✓ Add notes, warnings, and cross-references")
        print("✓ Generate HTML docs with: sphinx-build -b html docs/ docs/_build/html")
        print("✓ Host on ReadTheDocs.org for free public hosting")
        print("\n" + "=" * 70)

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

