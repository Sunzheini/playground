import yaml

"""
PyYAML provides simple functions to convert between Python objects and YAML

YAML is a superset of JSON (valid JSON is valid YAML)

Use consistent indentation (2 or 4 spaces, never tabs)!
"""

"""
yaml syntax:

1. Key-Value Pairs:
    name: John Doe
    age: 30
    is_student: false
2. Lists:
    fruits:
      - apple
      - banana
      - orange
3. Nested Mixed Structures:
config:
  debug: true
  max_connections: 100
  features:
    - authentication
    - logging
    - caching
"""

"""
yaml recognizes the following data types:

# Strings
title: "Hello World"
description: Plain text without quotes
multiline: |
  This is a multiline
  string that preserves
  line breaks

# Numbers
integer: 42
float: 3.14159
scientific: 1.2e-3

# Booleans
enabled: true
disabled: false

# Null
empty_value: null
also_null: ~

# Dates
date: 2023-12-25
datetime: 2023-12-25T10:30:00Z
"""
