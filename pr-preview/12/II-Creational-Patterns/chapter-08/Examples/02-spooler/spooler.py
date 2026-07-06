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


def main():
    name = "Fred"
    Spooler.print_text(name)


if __name__ == "__main__":
    main()
