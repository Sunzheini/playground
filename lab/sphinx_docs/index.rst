Welcome to Exercise Sphinx Documentation!
==========================================

This documentation demonstrates how to use Sphinx to auto-generate
beautiful documentation from Python docstrings.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Overview
========

This project contains examples of:

* **Google-style docstrings** - Clean and readable format
* **NumPy-style docstrings** - Detailed scientific documentation
* **Type hints** - Modern Python type annotations
* **Comprehensive examples** - Real-world usage demonstrations

Quick Start
===========

To run the example code::

    python exercise_sphinx.py

To build this documentation::

    cd sphinx_docs
    sphinx-build -b html . _build/html

Then open ``_build/html/index.html`` in your browser.

Modules
=======

.. automodule:: exercise_sphinx
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__, __repr__

Classes
=======

Calculator
----------

.. autoclass:: exercise_sphinx.Calculator
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

ScientificCalculator
--------------------

.. autoclass:: exercise_sphinx.ScientificCalculator
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

User
----

.. autoclass:: exercise_sphinx.User
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__, __repr__

Functions
=========

Mathematical Functions
----------------------

.. autofunction:: exercise_sphinx.factorial

.. autofunction:: exercise_sphinx.fibonacci

.. autofunction:: exercise_sphinx.is_prime

Utility Functions
-----------------

.. autofunction:: exercise_sphinx.format_currency

Demonstration Functions
-----------------------

.. autofunction:: exercise_sphinx.demonstrate_sphinx_features

.. autofunction:: exercise_sphinx.print_sphinx_setup_guide

.. autofunction:: exercise_sphinx.main

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

