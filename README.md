# Python Module 00 — Growing Code

*Python fundamentals through community garden data.*

## Description

**Growing Code** is the first module of the 42 Python curriculum. It introduces Python's core building blocks through small, garden-themed exercises: each one asks for a single function that reads, computes, or displays information about a community garden.

Concepts covered:

- Defining and calling functions
- Reading input with `input()` and displaying output with `print()`
- Variables, type conversion (`int()`), and arithmetic expressions
- Conditionals (`if` / `elif` / `else`)
- Loops and recursion
- Type annotations (type hints)
- Code style compliance with `flake8` and static type checking with `mypy`

Every exercise is a standalone `.py` file that defines one function. Files are not meant to run on their own: a separate test script imports and calls the function.

## Exercises

| Exercise | Directory | File | Concept |
|----------|-----------|------|---------|
| 0 | `ex0/` | `ft_hello_garden.py` | Defining a function, `print()` |
| 1 | `ex1/` | `ft_plot_area.py` | `input()`, `int()`, arithmetic (area of a rectangular plot) |
| 2 | `ex2/` | `ft_harvest_total.py` | Variables, addition |
| 3 | `ex3/` | `ft_plant_age.py` | `if` / `else` conditionals |
| 4 | `ex4/` | `ft_water_reminder.py` | Conditional logic |
| 5 | `ex5/` | `ft_count_harvest.py` | Counting up to the harvest day (loops / recursion) |
| 6 | `ex6/` | `ft_garden_summary.py` | Combining input, formatting, and calculations |
| 7 | `ex7/` | `ft_seed_inventory.py` | Type annotations |

> **Note:** exercise names, file names, and the authorized functions can differ slightly between subject versions. Check the PDF of your subject and adjust this table if needed.

### Example

```python
>>> from ex0.ft_hello_garden import ft_hello_garden
>>> ft_hello_garden()
Hello, Garden Community!
```

```python
>>> from ex1.ft_plot_area import ft_plot_area
>>> ft_plot_area()
Enter length: 5
Enter width: 3
Plot area: 15
```

## Instructions

### Requirements

- Python 3.10 or later
- `flake8` (style checker, the equivalent of `norminette` for Python)
- `mypy` (type checker, needed for the type annotation exercise)

No external libraries are required by the exercises themselves.

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flake8 mypy
```

### Project structure

```
python00/
├── ex0/
│   └── ft_hello_garden.py
├── ex1/
│   └── ft_plot_area.py
├── ex2/
│   └── ft_harvest_total.py
├── ex3/
│   └── ft_plant_age.py
├── ex4/
│   └── ft_water_reminder.py
├── ex5/
│   └── ft_count_harvest.py
├── ex6/
│   └── ft_garden_summary.py
├── ex7/
│   └── ft_seed_inventory.py
└── README.md
```

### Running and testing

Each function is called from a small test script (provided with the subject, or one you write yourself). For a quick check from the interpreter:

```bash
python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"
```

### Checking code quality

```bash
# Style (no output means no errors)
flake8 ex0/ft_hello_garden.py
flake8 .

# Type hints (exercise 7)
mypy ex7/ft_seed_inventory.py
```

### Rules to keep in mind

- Only use the functions authorized in each exercise (for example `print()`, `input()`, `int()`).
- Every file must define the requested function with the exact name given in the subject.
- Any code that does not respect `flake8` rules is considered incorrect.
- Be ready to explain every line of your code during the peer evaluation.

### Use of AI

> Replace this section with an honest description of how AI was (or was not) used, for example:
> AI was used to better understand concepts such as type hints and recursion, and to review the README structure. All code was written, tested, and understood by the author.

