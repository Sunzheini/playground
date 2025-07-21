import json
"""
The json module provides methods to serialize Python objects to JSON 
(for storage/APIs) and deserialize JSON back to Python objects.
"""

# json.dumps(obj): Convert a Python object to a JSON-formatted string.
# json.dump(obj, file): Write JSON directly to a file-like object.

"""
Supported Types:

Python	        JSON Equivalent
dict	        Object
list, tuple	    Array
str	            String
int, float	    Number
True/False	    true/false
None	        null
"""

data = {
    "name": "Alice",
    "age": 30,
    "is_active": True,
    "pets": ["Dog", "Cat"],
    "address": None
}

# Convert to JSON string
json_string = json.dumps(data, indent=2)  # `indent` for pretty-printing
print(json_string)


# json.loads(json_string): Parse a JSON string to a Python object.
# json.load(file): Read JSON from a file-like object.

# From JSON string
json_str = '{"name": "Bob", "score": 95}'
python_dict = json.loads(json_str)
print(python_dict["name"])  # Output: Bob
