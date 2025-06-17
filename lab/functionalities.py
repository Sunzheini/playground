# ---------------------------------------------------------
# switch case
# ---------------------------------------------------------
term = int(input())


match term:
    case 1:
        print(term + 1)
    case 2:
        print(term + 2)
    case 3:
        print(term + 3)
    case _:             # default
        print(term + 4)


# ---------------------------------------------------------
# eval
# ---------------------------------------------------------
x = 'print(55)'
eval(x)


# Perimeter of Square
def calculatePerimeter(l):
    return 4*l


# Area of Square
def calculateArea(l):
    return l*l


expression = input("Type a function: ")


for el in range(1, 5):
    if expression == 'calculatePerimeter(l)':
        print("If length is ", el, ", Perimeter = ", eval(expression))
    elif expression == 'calculateArea(l)':
        print("If length is ", el, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break


# ---------------------------------------------------------
# help
# ---------------------------------------------------------
help(print)     # Displays the documentation for the print function


def my_function():
    """
    This is a sample function.
    It does nothing.
    """
    pass


help(my_function)  # Displays the documentation for my_function


# ---------------------------------------------------------
# map
# ---------------------------------------------------------
def square(x):
    """Returns the square of x."""
    return x * x


def main():
    numbers = [1, 2, 3, 4, 5]
    # Using map to apply the square function to each element in numbers
    squared_numbers = list(map(square, numbers))
    print("Squared numbers:", squared_numbers)


# # ---------------------------------------------------------
# filter
# -----------------------------------------------------------
def is_even(x):
    """Returns True if x is even, False otherwise."""
    return x % 2 == 0


def main2():
    numbers = [1, 2, 3, 4, 5, 6]
    # Using filter to get only even numbers from the list
    even_numbers = list(filter(is_even, numbers))
    print("Even numbers:", even_numbers)


# ---------------------------------------------------------
# sorted
# -----------------------------------------------------------
def main3():
    numbers = [5, 2, 9, 1, 5, 6]
    # Using sorted to sort the list in ascending order
    sorted_numbers = sorted(numbers, reverse=False, key=None)
    print("Sorted numbers:", sorted_numbers)


# ---------------------------------------------------------
# zip
# -----------------------------------------------------------
def main4():
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    # Using zip to combine names and ages into a list of tuples
    combined = list(zip(names, ages))
    print("Combined names and ages:", combined)


# ---------------------------------------------------------
# reduce
# -----------------------------------------------------------
from functools import reduce


def add(x, y):
    """Returns the sum of x and y."""
    return x + y


def main5():
    numbers = [1, 2, 3, 4, 5]
    # Using reduce to sum all elements in the list
    total = reduce(add, numbers)
    print("Total sum:", total)


# -----------------------------------------------------------
# enumerate
# -----------------------------------------------------------
def main6():
    fruits = ["apple", "banana", "cherry"]
    # Using enumerate to get index and value pairs
    for index, fruit in enumerate(fruits):
        print(f"Index: {index}, Fruit: {fruit}")


# -----------------------------------------------------------
# pprint
# -----------------------------------------------------------
from pprint import pprint


def main7():
    data = {
        'name': 'Alice',
        'age': 30,
        'hobbies': ['reading', 'hiking', 'coding'],
        'address': {
            'city': 'Wonderland',
            'zip': '12345'
        }
    }
    # Using pprint to print the data structure in a readable format
    pprint(data)


# -----------------------------------------------------------
# defaultdict
# -----------------------------------------------------------
from collections import defaultdict


def main8():
    # Using defaultdict to create a dictionary with default value of list
    d = defaultdict(list)
    d['fruits'].append('apple')
    d['fruits'].append('banana')
    d['vegetables'].append('carrot')

    # Printing the defaultdict
    print("Defaultdict contents:")
    for key, value in d.items():
        print(f"{key}: {value}")


# -----------------------------------------------------------
# any
# -----------------------------------------------------------
def main9():
    numbers = [0, 1, 2, 3]
    # Using any to check if any number in the list is greater than 2
    has_greater_than_two = any(num > 2 for num in numbers)
    print("Any number greater than 2:", has_greater_than_two)


# -----------------------------------------------------------
# all
# -----------------------------------------------------------
def main10():
    numbers = [1, 2, 3, 4]
    # Using all to check if all numbers in the list are greater than 0
    all_positive = all(num > 0 for num in numbers)
    print("All numbers are positive:", all_positive)


# -----------------------------------------------------------
# counter
# -----------------------------------------------------------
from collections import Counter


def main11():
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    # Using Counter to count occurrences of each word
    word_count = Counter(words)
    print("Word count:", word_count)


# -----------------------------------------------------------
# dataclass
# -----------------------------------------------------------
from dataclasses import dataclass


@dataclass
class Person:
    """
    A simple dataclass to represent a person.
    Automatically generates init, repr, and other methods.
    """
    name: str
    age: int
    is_student: bool

    def greet(self) -> str:
        """Returns a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."


def main12():
    # Creating an instance of the Person dataclass
    person = Person(name="Alice", age=30, is_student=False)
    print(person.greet())
    print(person)  # Automatically generated __repr__ method


# -----------------------------------------------------------
# functools.cache
# -----------------------------------------------------------
from functools import cache


@cache
def fibonacci(n: int) -> int:
    """Returns the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main13():
    # Calculating Fibonacci numbers using the cached function
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")


# -----------------------------------------------------------
# slicing
# -----------------------------------------------------------
def main14():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Slicing the list to get the first five elements
    first_five = numbers[:5]
    print("First five numbers:", first_five)

    # Slicing the list to get every second element
    every_second = numbers[::2]
    print("Every second number:", every_second)

    # Slicing the list to reverse it
    reversed_numbers = numbers[::-1]
    print("Reversed numbers:", reversed_numbers)


# -----------------------------------------------------------
# if __name__ == "__main__":
# -----------------------------------------------------------
if __name__ == "__main__":
    main()


# place it inside a .py file to avoid running on import, so
# that it only runs when the script is executed directly.

"""
__name__ is a special Python variable that holds:
    "__main__" when the script is run directly
    The module name when the script is imported
"""

"""
The convention exists so you can:
    Have code that runs when you execute the script directly
    Have the same code available for import without automatically executing anything
    Prevent certain code from running during imports
"""


# -----------------------------------------------------------
# for else (prevents using a flag variable)
# -----------------------------------------------------------
def main15():
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        if number == 3:
            print("Found 3, breaking the loop.")
            break
    else:
        print("This will not be printed because the loop was broken.")

    print("Loop completed, either found 3 or finished iterating.")


# -----------------------------------------------------------
# while else
# -----------------------------------------------------------
def main16():
    count = 0
    while count < 5:
        print(f"Count is {count}.")
        count += 1
    else:
        print("Count reached 5, exiting the loop.")


# -----------------------------------------------------------
# with statement (context manager)
# -----------------------------------------------------------
def main17():
    with open("example.txt", "w") as file:
        file.write("Hello, World!")

    # The file is automatically closed after the with block
    print("File written and closed automatically.")


# -----------------------------------------------------------






