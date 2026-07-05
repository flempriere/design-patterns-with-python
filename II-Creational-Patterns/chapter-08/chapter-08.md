# Chapter 8: The Singleton Pattern

- [Notes](#notes)
  - [The Traditional Singleton](#the-traditional-singleton)
    - [Static Classes](#static-classes)
  - [The Python Global Object
    Pattern](#the-python-global-object-pattern)
  - [Identifying Singletons](#identifying-singletons)
  - [Consequences of the Singleton
    Pattern](#consequences-of-the-singleton-pattern)
- [Summary](#summary)

## Notes

- Sometimes in an application it is useful to have exactly *one*
  instance of a given class
  - For example,

    1. One Window Manager
    2. One database access point
- The *Singleton Pattern* is a design pattern for enforcing a single
  instance of a class
  - Usually implemented with a single global point of access

``` mermaid
---
title: "The Singleton Pattern (Python Flavoured)"
---
classDiagram

class Singleton {
    - instance : Singleton
    + instance() Singleton
}

class SingletonException

Singleton --> SingletonException : throws
```

### The Traditional Singleton

- The traditional singleton is implemented in other languages via the
  following,

  1. Making all constructors private
      - Prevents a client instantiating it themselves
  2. Providing a *static* or *class* method that returns a *reference*
      to the instance
      - In some cases *lazy instantiation* is used
      - The first call to this function also creates the first instance

- In Python we cannot make constructors private, so we have to use some
  workarounds

  - We *can* however, define an `Exception`

    ``` python
    class SingletonException(Exception):
        """
        Raised when trying to create multiple instances
        of a singleton
        """

        pass
    ```

  - We throw this whenever the client attempts to directly invoke the
    `__init__` method if there is already an instance

- The actual instance itself is stored as a *class variable*,
  `_instance`

  - The leading underscore `_` indicates the variable is private and
    should not be directly accessed
  - Instead, we then define a *class method* as an access point to this
    instance

  ``` python
    class Singleton:
        """
        Represents a singleton object for which
        only one instance can be created

        The global instance should be accessed via
        the `instance` method

        Attributes
        ----------
        name : str
            instance name
        """

        _instance = None

        @classmethod
        def instance(cls) -> Singleton:
            """
            Access the global instance of this singleton

            Creates the instance if it has not yet
            been invoked

            Returns
            -------
            Singleton
                The single global instance
            """
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance

        def __init__(self) -> None:
            """
            Create a new instance of the Singleton

            Raises
            ------
            SingletonException
                Raised if attempting to create multiple instances
            """
            if Singleton._instance is not None:
                raise SingletonException("Cannot create multiple instances of Singleton")
            else:
                Singleton._instance = self
  ```

> [!NOTE]
>
> **An Alternative implementation**
>
> If we didn’t want the implicit lazy instantiation we could remove the
> class method and leave only the class variable. The client can then
> call `__init__` to invoke the instance, and if the instance is yet to
> be created will receive `None`

- We can now run some basic tests,
  - Here we show that the first instance we create is subsequently
    returned by a call to `instance` and that we get an exception when
    trying to call the `__init__` a second time

``` python
first = Singleton()
second = Singleton.instance()

# assert accessing singleton instance returns same global instance
assert first == second, "multiple singleton instances detected"
print("Received the same global object")

# trying to directly call `__init__ a second time throws an exception
Singleton()
```

    Received the same global object

    SingletonException: Cannot create multiple instances of Singleton
    ---------------------------------------------------------------------------
    SingletonException                        Traceback (most recent call last)
    Cell In[3], line 9
          5 assert first == second, "multiple singleton instances detected"
          6 print("Received the same global object")
          7
          8 # trying to directly call `__init__ a second time throws an exception
    ----> 9 Singleton()

    Cell In[2], line 44, in Singleton.__init__(self)
         40         SingletonException
         41             Raised if attempting to create multiple instances
         42         """
         43         if Singleton._instance is not None:
    ---> 44             raise SingletonException("Cannot create multiple instances of Singleton")
         45         else:
         46             Singleton._instance = self

    SingletonException: Cannot create multiple instances of Singleton

- The above approach could also be extended to enable a fixed number of
  singleton instances to be created an accessed
- The code above is provided in
  [singleton.py](Examples/01-singleton/singleton.py)

#### Static Classes

- Another method of implementing a singleton-like class is to implement
  a class that purely consists of static or class methods

  - And class attributes if required
  - `@classmethod` is tied to the class instance so can be modified by
    subclasses
  - `@staticmethod` are not modified by inheritance

- For example, here we implement a mock of a `Spooler`

  ``` python
    """
    Demonstrate a Singleton implemented as a static class

    Classes
    -------

    * Spooler -- Mocks a print spooler to demonstrate a class implementing static methods
    """


    class Spooler:
        @staticmethod
        def print_text(text: str) -> None:
            print(text)
  ```

- Methods are invoked via the class name

  ``` python
    name = "Fred"
    Spooler.print_text(name)
  ```

      Fred

- Note, in Python static methods are largely not distinct from free
  functions aside from being namespaced to the class

- In general the preferred implementation pattern is as free functions
  in a module

  - In general only use the above if you need to create a small local
    namespace within a module or these are methods strongly coupled to a
    class but not any specific implementation
    - If you need something at the class-level consider `@classmethod`
      instead

- The code above is implemented in
  [spooler.py](Examples/02-spooler/spooler.py)

### The Python Global Object Pattern

- The above discussion on static objects highlights some of the ways
  that the singleton pattern is viewed as an anti-pattern in python
- The *global object pattern* is the preferred pythonic way of
  implementing singleton-like classes where a single instance is shared
  - Since modules contents are only imported *once* we can treat the
    module itself as the *singleton class* with the mapping,
    - Attributes are global variables and constants defined in the
      module
    - Methods are free functions defined in the module
  - If we need to provide *object instances* then
    - We create a global object instance of the desired class and assign
      it a name in a module
    - Any code that imports the module then gains access to this object
- For example, here we define a simple module for greeting someone
  - The user can configure the `greeting` global variable to control the
    greeting
  - Can then invoke the `print_greeting` method
    - By importing this module, only *one* such greeting can exist at a
      time

``` python
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
```

- The calling code then looks like,

  ``` python
    """
    Demonstrates the global object pattern

    Treats the `global_object` module as a singleton class
    """

    import global_object

    global_object.print_greeting("Alice")

    global_object.greeting = "Howdy"

    global_object.print_greeting("Bob")
  ```

- The proper implementation is provided in
  [main.py](Examples/03-global-object/main.py) and
  [global_object.py](Examples/03-global-object/global_object.py)

> [!NOTE]
>
> The above example is obviously quite contrived but the goal here is to
> show the *concept*

### Identifying Singletons

- An issue with singleton’s can be identifying which classes are
  singletons
  - And which singleton instances have been created
- One solution is to invoke all singleton’s up front at the start of the
  program
  - Generally poor practice
  - Much better to follow the principle of creating things closest to
    where they are needed
- Another solution is to define a *Registry*
  - All singleton’s register themselves with the registry when they are
    first invoked
  - They can then be accessed via the registry
    - Typically implemented as a dictionary
  - An issue with the registry approach is that it can weaken type
    checking
    - The registry is best implemented using something like the global
      object pattern discussed above

### Consequences of the Singleton Pattern

- The singleton pattern is sometimes regarded as an anti-pattern

- As discussed above in Python one should also prefer the [Global Object
  Pattern](#the-python-global-object-pattern)

- Other critiques include

  1. It can be difficult to subclass a singleton because one cannot
      create instantiate the different subclasses
  2. Singleton’s can be extended to allow a fixed number of entities
      other than zero
  3. They effectively introduce a global state dependency into a
      program
      - This can make it harder to test components
  4. Singleton’s can be make it hard to introduce concurrency by
      creating race conditions

## Summary

- The singleton pattern enforces the existence of one global instance of
  a given class
- It can be implemented in python, but in general is regarded as an
  anti-pattern
- Instead implement singleton’s either as modules or through global
  objects
