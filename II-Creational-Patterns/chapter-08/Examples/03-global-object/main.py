"""
Demonstrates the global object pattern

Treats the `global_object` module as a singleton class
"""

import global_object

global_object.print_greeting("Alice")

global_object.greeting = "Howdy"

global_object.print_greeting("Bob")
