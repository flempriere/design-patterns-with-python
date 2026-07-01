"""
Simple GUI
----------

Demonstrates the simple factory through a simple program that converts
names entered in either `first last` or `last, first` to their first and
last name components via factory
"""

import sys
import tkinter as tk
import tkinter.ttk


class Name:
    """
    A Name

    Represents a Person's name as a first name, second name pair.

    Subclasses should override the `__str__` method to control how a name
    is displayed

    Attributes
    ----------
    first: str
        first name
    last: str
        last name
    """

    def __init__(self):
        self.first = ""
        self.last = ""

    def __str__(self):
        pass


class FirstNameFirst(Name):
    """
    Name represented as *First Last.*
    """

    def __init__(self, name: str):
        """
        Create a new instance from a string.`

        The provided string `name` should follow the format `first last`.
        i.e. first name followed by a space-delimiter then the last name.
        If there is no delimiter the whole string is treated as the last name

        Parameters
        ----------
        name : str
            name represented as `first last`
        """
        super().__init__()
        if (i := name.rfind(" ")) > 0:
            self.first = name[0:i].strip()
            self.last = name[i + 1 :].strip()
        else:
            self.last = name.strip()

    def __str__(self) -> str:
        """
        Instance string representation as ``"first last"``

        Returns
        -------
        str
            string representation of the instance as ``"first last"``
        """
        name = ""
        if self.first:
            name += self.first + " "
        name += self.last
        return name


class LastNameFirst(Name):
    """
    Name represented as *Last, First*
    """

    def __init__(self, name_string: str):
        """
        Create a new instance from a string.

        The provided string `name` should follow the format `last, first`.
        i.e. last name followed by a comma-delimiter then the first name.
        If there is no delimiter the whole string is treated as the last name

        Parameters
        ----------
        name : str
            name represented as `last, first`
        """
        super().__init__()
        if (i := name_string.find(",")) > 0:
            self.first = name_string[0:i].strip()
            self.last = name_string[i + 1 :].strip()
        else:
            self.last = name_string.strip()


class NameFactory:
    """
    Creates `Name` instances for a provided `name`

    Provides the appropriate `Name` instance, either `FirstNameFirst` or
    `LastNameFirst` based on the provided `name` string.

    Attributes
    ----------
    name: str
        name used to create `Name` instances
    """

    def __init__(self, name: str):
        """Create a new instance for the provided `name`

        Parameters
        ----------
        name : str
            name to be used to create `Name` instances. Should be formatted as
            either `first last` or `last, first`
        """
        self.name = name

    def get_name(self) -> Name:
        """
        Create a new `Name` instance

        Returns
        -------
        Name
            A concrete instance of Name depending on the format of the currently
            stored name
        """
        if self.name.find(",") > 0:
            return LastNameFirst(self.name)
        else:
            return FirstNameFirst(self.name)


class NameEntryForm:
    """
    A Widget that allows users to enter a name and displays the first
    and last names
    """

    def __init__(self, master):

        master.title("Simple Factory")
        tk.Label(master, text="Enter Name:", foreground="blue").grid(
            row=0, columnspan=3
        )

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1, sticky=tk.E + tk.W)

        tk.Label(master, text="First name:", foreground="blue").grid(
            row=2, column=0, sticky=tk.W, pady=10
        )
        self.first_name_display = tk.Entry(master)
        self.first_name_display.grid(row=2, column=1, sticky=tk.E, pady=10)

        tk.Label(master, text="Last name:", foreground="blue").grid(
            row=3, column=0, sticky=tk.W, pady=10
        )
        self.last_name_display = tk.Entry(master)
        self.last_name_display.grid(row=3, column=1, sticky=tk.E, pady=5)

        compute_name_button = tk.ttk.Button(
            master, text="Process", command=self.compute_name
        )
        compute_name_button.grid(row=4, column=0, pady=5)

        clear_button = tk.ttk.Button(master, text="Clear", command=self.clear_form)
        clear_button.grid(row=4, column=1, pady=5)

        quit_button = tk.ttk.Button(text="Quit", command=sys.exit)
        quit_button.grid(row=4, column=2, pady=5)

    def compute_name(self):
        """
        Update the displayed name in response to the current user input
        """

        raw_name = self.name_entry.get()
        name = NameFactory(raw_name).get_name()

        self.first_name_display.insert(0, name.first)
        self.last_name_display.insert(0, name.last)

    def clear_form(self):
        """
        Clear the current form, deleting all Entries
        """

        self.name_entry.delete(0, tk.END)
        self.first_name_display.delete(0, tk.END)
        self.last_name_display.delete(0, tk.END)


def main():
    root = tk.Tk()
    NameEntryForm(root)
    tk.mainloop()


if __name__ == "__main__":
    main()
