"""
Simple Demonstration of a Singleton Class

Classes
-------

* `Singleton` -- A representative `Singleton` class

Exceptions
----------

* `SingletonException` -- Base Exception for all singleton related exceptions
"""


class SingletonException(Exception):
    """
    Raised when trying to create multiple instances
    of a singleton
    """

    pass


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


def main():
    first = Singleton()
    second = Singleton.instance()

    # assert accessing singleton instance returns same global instance
    assert first == second, "multiple singleton instances detected"

    # ensure we can't make another instance by invoking the `__init__` directly
    try:
        Singleton()
    except SingletonException as e:
        print(f"Failed to invoke additional singleton instance, caught exception {e}")
        print("All tests passed!")
    else:
        print("Test failed, invoked an additional singleton instance")


if __name__ == "__main__":
    main()
