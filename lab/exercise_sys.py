import sys
"""
The sys module provides access to variables and functions that interact with the
Python interpreter and the system environment
"""

print("script name:", sys.argv[0])  # Name of the script being executed
print("arguments:", sys.argv[1:])  # List of command-line arguments passed to the script

sys.exit()  # Exit the script with a status code (0 for success, non-zero for error)
# sys.path.    # commands related to the Python path



