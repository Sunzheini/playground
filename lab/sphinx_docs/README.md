# Sphinx Documentation Example - Complete Guide

## 📚 What This Example Demonstrates

This is a **comprehensive example** of using Sphinx to generate professional documentation from Python docstrings. The example includes:

### ✨ Features Demonstrated

1. **Google-Style Docstrings** - Clean, readable format popular in Python projects
2. **NumPy-Style Docstrings** - Detailed format preferred for scientific code
3. **Type Hints** - Modern Python type annotations for better documentation
4. **Auto-Generated HTML Docs** - Beautiful, searchable documentation website
5. **Real Working Code** - All examples are functional and tested

### 📁 Files Created

```
lab/
├── exercise_sphinx.py          # Main example file with documented code
└── sphinx_docs/                # Sphinx documentation directory
    ├── conf.py                 # Sphinx configuration
    ├── index.rst               # Main documentation page
    ├── modules.rst             # Modules listing
    ├── _static/                # Static files (CSS, images)
    ├── _templates/             # HTML templates
    └── _build/
        └── html/               # Generated HTML documentation
            └── index.html      # Open this in browser!
```

## 🚀 Quick Start

### 1. Run the Example Code

```bash
cd D:\Study\Projects\PycharmProjects\playground\lab
python exercise_sphinx.py
```

This will:
- Demonstrate all the documented features
- Show Google and NumPy style docstrings in action
- Print a complete setup guide
- Run test calculations

### 2. View the Generated Documentation

Open this file in your browser:
```
D:\Study\Projects\PycharmProjects\playground\lab\sphinx_docs\_build\html\index.html
```

Or run:
```bash
cd sphinx_docs\_build\html
start index.html
```

### 3. Rebuild Documentation (After Changes)

```bash
cd sphinx_docs
sphinx-build -b html . _build/html
```

## 📖 What's Included in exercise_sphinx.py

### Classes

1. **Calculator** - Basic calculator demonstrating Google-style docstrings
   - `add()`, `subtract()`, `multiply()`, `divide()`
   - `get_history()`, `clear_history()`

2. **ScientificCalculator** - Advanced calculator with NumPy-style docstrings
   - `power()`, `sqrt()`, `sin()`, `cos()`, `log()`
   - Inherits from Calculator

3. **User** - User management class
   - `activate()`, `deactivate()`, `change_role()`

### Functions

1. **factorial(n)** - Calculate factorial with comprehensive docs
2. **fibonacci(n)** - Calculate Fibonacci numbers
3. **is_prime(n)** - Check if number is prime
4. **format_currency()** - Format numbers as currency

### Demo Functions

- **demonstrate_sphinx_features()** - Runs all examples
- **print_sphinx_setup_guide()** - Prints setup instructions
- **main()** - Main entry point

## 📝 Docstring Styles

### Google Style (Used for Calculator)

```python
def add(self, a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a (float): First number to add.
        b (float): Second number to add.
    
    Returns:
        float: Sum of a and b.
    
    Example:
        >>> calc.add(10.5, 20.3)
        30.8
    """
```

### NumPy Style (Used for ScientificCalculator)

```python
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
    """
```

## 🔧 Sphinx Configuration

The `conf.py` file includes:

### Extensions Used

- **sphinx.ext.autodoc** - Auto-generate docs from docstrings
- **sphinx.ext.napoleon** - Support Google/NumPy docstrings
- **sphinx.ext.viewcode** - Add source code links
- **sphinx.ext.todo** - TODO support
- **sphinx.ext.intersphinx** - Link to other docs (like Python docs)
- **sphinx.ext.coverage** - Documentation coverage stats

### Theme

- **alabaster** - Default clean theme (can switch to sphinx_rtd_theme)

## 📊 Example Output

### Running exercise_sphinx.py

```
======================================================================
SPHINX DOCUMENTATION EXAMPLE - FEATURE DEMONSTRATION
======================================================================

1. Basic Calculator (Google-style docstrings):
----------------------------------------------------------------------
Calculator: BasicCalc
5 + 3 = 8
10 - 4 = 6
6 * 7 = 42
20 / 4 = 5.0
History: ['5 + 3 = 8', '10 - 4 = 6', '6 * 7 = 42', '20 / 4 = 5.0']

2. Scientific Calculator (NumPy-style docstrings):
----------------------------------------------------------------------
Calculator: SciCalc
2^8 = 256
√16 = 4.0
sin(90°) = 1.0
cos(0°) = 1.0
log(100, base=10) = 2.0

3. Mathematical Functions:
----------------------------------------------------------------------
5! = 120
Fibonacci(10) = 55
Is 17 prime? True
Is 18 prime? False
Currency: $1,234.56 USD

4. User Management:
----------------------------------------------------------------------
Created user: User(username='alice', email='alice@example.com', role='user')
User is active: True
Changed role to: admin
```

## 🎯 Key Takeaways

1. ✅ **Use detailed docstrings** - They become your documentation
2. ✅ **Choose a style** - Google or NumPy, be consistent
3. ✅ **Include examples** - Doctest examples are super helpful
4. ✅ **Use type hints** - Makes docs clearer and enables type checking
5. ✅ **Add cross-references** - Link related functions/classes
6. ✅ **Build regularly** - Keep docs in sync with code
7. ✅ **Host online** - ReadTheDocs.org offers free hosting

## 🌐 Advanced Usage

### Generate Different Formats

```bash
# HTML (default)
sphinx-build -b html docs/ docs/_build/html

# PDF (requires LaTeX)
sphinx-build -b latex docs/ docs/_build/latex
cd docs/_build/latex
make

# ePub (for e-readers)
sphinx-build -b epub docs/ docs/_build/epub

# Man pages
sphinx-build -b man docs/ docs/_build/man
```

### Watch for Changes (Auto-rebuild)

```bash
pip install sphinx-autobuild
sphinx-autobuild docs/ docs/_build/html
# Opens browser and auto-reloads on changes!
```

### Check Documentation Coverage

```bash
sphinx-build -b coverage docs/ docs/_build/coverage
cat docs/_build/coverage/python.txt
```

## 🔗 Resources

- **Sphinx Official Docs**: https://www.sphinx-doc.org/
- **ReadTheDocs Theme**: https://sphinx-rtd-theme.readthedocs.io/
- **Napoleon Extension**: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
- **Google Style Guide**: https://google.github.io/styleguide/pyguide.html
- **NumPy Style Guide**: https://numpydoc.readthedocs.io/

## 💡 Tips

1. **Start with good docstrings** - Sphinx just formats what you write
2. **Use consistent formatting** - Pick Google or NumPy style
3. **Include examples** - They're the most helpful part of docs
4. **Link related items** - Use `:class:`, `:func:`, `:meth:` roles
5. **Add diagrams** - Sphinx supports Graphviz, PlantUML, etc.
6. **Version your docs** - Tag releases and build docs for each version
7. **Automate builds** - CI/CD can build and deploy docs automatically

## 🎨 Customization

### Change Theme

Install ReadTheDocs theme:
```bash
pip install sphinx-rtd-theme
```

Update `conf.py`:
```python
html_theme = 'sphinx_rtd_theme'
```

### Add Custom CSS

Create `_static/custom.css`:
```css
.wy-nav-content {
    max-width: 1200px !important;
}
```

Update `conf.py`:
```python
html_css_files = ['custom.css']
```

### Add Logo

```python
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'
```

## ✅ Success!

You now have:
- ✅ A complete working example of Sphinx documentation
- ✅ Generated HTML documentation you can browse
- ✅ Knowledge of both Google and NumPy docstring styles
- ✅ A template for your own projects

**Next Steps:**
1. Browse the generated HTML docs
2. Try modifying docstrings and rebuilding
3. Apply this to your own projects
4. Host your docs on ReadTheDocs.org

---

**Created:** February 10, 2026  
**File Location:** `D:\Study\Projects\PycharmProjects\playground\lab\exercise_sphinx.py`  
**Documentation:** `D:\Study\Projects\PycharmProjects\playground\lab\sphinx_docs\_build\html\index.html`

