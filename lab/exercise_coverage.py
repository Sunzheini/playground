"""
Python Coverage Package Example
================================

The coverage package is used to measure code coverage of Python programs.
It monitors your program, noting which parts of the code have been executed,
then analyzes the source to identify code that could have been executed but was not.

Installation:
    pip install coverage

Usage Methods:
    1. Command line: coverage run script.py
    2. Programmatic API (shown in this example)
    3. pytest integration: pytest --cov=myproject tests/
"""

import coverage
import sys


# ============================================================================
# Example 1: Simple Functions to Test Coverage
# ============================================================================

def calculate_discount(price, discount_percent):
    """Calculate the final price after discount."""
    if price < 0:
        raise ValueError("Price cannot be negative")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price


def categorize_age(age):
    """Categorize a person by age."""
    if age < 0:
        return "Invalid"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# ============================================================================
# Example 2: Test Functions (Some code paths won't be covered)
# ============================================================================

def run_tests():
    """Run some tests - note that not all code paths will be covered."""
    print("Running tests...")

    # Test calculate_discount
    print(f"✓ Discount test: ${calculate_discount(100, 20)} (expected: 80.0)")

    # Test categorize_age - only testing some cases
    print(f"✓ Age test (child): {categorize_age(10)} (expected: Child)")
    print(f"✓ Age test (adult): {categorize_age(30)} (expected: Adult)")
    # Note: We're NOT testing Teenager, Senior, or Invalid cases

    # Test is_prime - limited coverage
    print(f"✓ Prime test (7): {is_prime(7)} (expected: True)")
    print(f"✓ Prime test (4): {is_prime(4)} (expected: False)")
    # Note: We're NOT testing edge cases like negative numbers or 2

    print("Tests completed!")


# ============================================================================
# Example 3: Using Coverage Programmatically
# ============================================================================

def example_programmatic_coverage():
    """Demonstrate using coverage package programmatically."""
    print("\n" + "="*70)
    print("EXAMPLE 3: Programmatic Coverage Measurement")
    print("="*70 + "\n")

    # Create a Coverage instance
    cov = coverage.Coverage()

    # Start measuring coverage
    cov.start()

    # Run the code to be measured
    run_tests()

    # Stop measuring
    cov.stop()

    # Save coverage data
    cov.save()

    # Print coverage report to console
    print("\n" + "-"*70)
    print("COVERAGE REPORT:")
    print("-"*70)
    cov.report()

    # Generate HTML coverage report
    print("\n" + "-"*70)
    print("Generating HTML coverage report...")
    print("-"*70)
    cov.html_report(directory='htmlcov')
    print("✓ HTML report generated in 'htmlcov' directory")
    print("  Open 'htmlcov/index.html' in a browser to view detailed coverage")


# ============================================================================
# Example 4: Coverage with Context Manager
# ============================================================================

def example_context_manager():
    """Demonstrate using coverage with context manager."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Coverage with Context Manager")
    print("="*70 + "\n")

    cov = coverage.Coverage()

    # Use context manager for automatic start/stop
    with cov.collect():
        # Test only specific functions
        result1 = calculate_discount(200, 15)
        result2 = is_prime(17)
        print(f"Discount result: {result1}")
        print(f"Is 17 prime? {result2}")

    print("\n" + "-"*70)
    print("COVERAGE REPORT (Context Manager):")
    print("-"*70)
    cov.report()


# ============================================================================
# Example 5: Coverage Analysis
# ============================================================================

def example_coverage_analysis():
    """Demonstrate coverage analysis and statistics."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Coverage Analysis")
    print("="*70 + "\n")

    cov = coverage.Coverage()
    cov.start()

    # Run tests with partial coverage
    run_tests()

    cov.stop()
    cov.save()

    # Get coverage data
    print("\n" + "-"*70)
    print("COVERAGE STATISTICS:")
    print("-"*70)

    # Get the total coverage percentage
    total = cov.report(file=sys.stdout)
    print(f"\nTotal Coverage: {total:.1f}%")

    # Analyze specific file
    print("\n" + "-"*70)
    print("DETAILED ANALYSIS:")
    print("-"*70)

    analysis = cov.analysis(__file__)
    executed_lines = analysis[1]
    missing_lines = analysis[2]

    print(f"File analyzed: {analysis[0]}")
    print(f"Executed lines: {len(executed_lines)}")
    print(f"Missing lines: {len(missing_lines)}")
    if missing_lines:
        print(f"Missing line numbers: {missing_lines[:10]}...")  # Show first 10


# ============================================================================
# Example 6: Command Line Usage Examples
# ============================================================================

def print_command_line_examples():
    """Print examples of how to use coverage from command line."""
    print("\n" + "="*70)
    print("COMMAND LINE USAGE EXAMPLES:")
    print("="*70 + "\n")

    examples = [
        ("Run coverage on a script", "coverage run exercise_coverage.py"),
        ("Show coverage report", "coverage report"),
        ("Show report with missing lines", "coverage report -m"),
        ("Generate HTML report", "coverage html"),
        ("Erase coverage data", "coverage erase"),
        ("Run and generate report", "coverage run exercise_coverage.py && coverage report"),
        ("Coverage with pytest", "pytest --cov=mymodule tests/"),
        ("Coverage with pytest (HTML)", "pytest --cov=mymodule --cov-report=html tests/"),
    ]

    for description, command in examples:
        print(f"• {description}:")
        print(f"  {command}\n")


# ============================================================================
# Example 7: Configuration (.coveragerc)
# ============================================================================

def print_configuration_example():
    """Print example of .coveragerc configuration file."""
    print("\n" + "="*70)
    print("CONFIGURATION FILE EXAMPLE (.coveragerc):")
    print("="*70 + "\n")

    config = """
[run]
# Specify which files to measure
source = .
omit = 
    */tests/*
    */venv/*
    */__pycache__/*

[report]
# Show missing lines in report
show_missing = True

# Exclude lines from coverage
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
    if TYPE_CHECKING:

[html]
# Directory for HTML report
directory = htmlcov
    """
    print(config)


# ============================================================================
# Main Execution
# ============================================================================

def main():
    """Main function to run all coverage examples."""
    print("="*70)
    print("PYTHON COVERAGE PACKAGE - COMPREHENSIVE EXAMPLES")
    print("="*70)

    # Show command line examples
    print_command_line_examples()

    # Show configuration example
    print_configuration_example()

    # Run programmatic examples
    try:
        # Example 3: Basic programmatic usage
        example_programmatic_coverage()

        # Example 4: Context manager
        example_context_manager()

        # Example 5: Coverage analysis
        example_coverage_analysis()

        print("\n" + "="*70)
        print("ALL EXAMPLES COMPLETED!")
        print("="*70)
        print("\nKey Takeaways:")
        print("1. Coverage helps identify untested code paths")
        print("2. Use 'coverage run' to measure coverage")
        print("3. Use 'coverage report' to see results")
        print("4. HTML reports provide detailed visual feedback")
        print("5. Aim for high coverage, but 100% isn't always necessary")
        print("6. Configure coverage with .coveragerc file")

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
