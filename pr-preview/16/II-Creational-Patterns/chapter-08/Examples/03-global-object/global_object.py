"""
Demonstrates the more Pythonic global object pattern

Variables and Constants
-----------------------

* `greeting` : `str` -- Configurable greeting the module uses

Functions
---------

* `print_greeting` -- print out a greeting to a person
"""

greeting: str = "Hello"


def print_greeting(name: str) -> None:
    """
    Greets a person

    Configure the module-level `greeting` parameter to
    modify the greeting

    Parameters
    ----------
    name : str
        the name of the person to greet

    See Also
    --------
    `greeting`

    """
    print(f"{greeting} {name}")
