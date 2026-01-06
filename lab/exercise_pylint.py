"""
Pylint is a static code analysis tool for Python that checks for:
    Coding standards compliance (PEP 8)
    Code quality issues
    Potential bugs
    Code smells
    Design problems

# Key Features
    Error Detection: Finds syntax errors, undefined variables, etc.
    Code Style: Enforces PEP 8 conventions
    Code Quality: Identifies refactoring opportunities
    Customizable: Configurable rules and thresholds
    Rating System: Gives your code a score out of 10

# Analyze a single file
pylint exercise_pylint.py
pylint --reports=no --score=yes exercise_pylint.py

# Analyze a module/package
pylint my_package/

# Analyze entire project
pylint . (inside project root) # but this will include venv and other folders
pylint --ignore-paths=".*venv.*|.*\.idea.*|.*migrations.*|.*test.*|.*__pycache__.*" .          # ignore common folders

pylint --persistent=no .    # disable caching of results
""""" 
import os,sys
myVar=10
CONSTANT=50

def badFunction(x,y):
    result=x+y
    unused=5
    if result>10:
        return True
    else:
        return False

class my_class:
    def method1(self):
        pass

print("hello world")
