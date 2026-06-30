# II: Creational Patterns

- Creational Patterns deal with the *creation* of objects

- Help decouple a program implementation from the specifics of how an
  object is created

  - This is especially important in python where the standard creation
    mechanism always invokes the `__init__` method

  - Unlike other languages Python does not allow method overloading, so
    there is only ever *one* `__init__` method

    ``` python
        an_object = AClass()
    ```

- Direct invocation of the `__init__` method can lead to hard-coded
  object instances in some parts of the code

  - Often the nature of an object instantiated depends on the state of
    the program

- Generally it is more flexible to *abstract* the creation mechanism to
  improve flexibility and reduce coupling

- This section will cover the following creational patterns

  1. The Factory pattern
      - Object creation is delegated to a simple-decision making class
        that can decide between different subclasses of an abstract base
        class
  2. The Abstract Factory pattern
      - Extends the Factory pattern with an interface to create
        instances from a family of related objects
  3. The Builder pattern
      - Separate construction of a complex object from it’s
        representation
      - Several different representations of the same object can be
        constructed by different consumers
  4. The Prototype pattern
      - Start with an instantiated instance of a class and create new
        instances by cloning or copying the prototype
      - Instances are then able to be further customised via method
        calls
  5. The Singleton pattern
      - Define a class that can have no more than one instance
      - Provides a single global point of access to that instance
