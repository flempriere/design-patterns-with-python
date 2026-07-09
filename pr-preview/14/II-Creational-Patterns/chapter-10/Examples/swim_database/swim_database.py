"""
Demonstrates the Prototype Pattern by showing
how we can clone a table of data to present it
in different formats without modifying the original
"""

import tkinter as tk
import tkinter.ttk
from typing import Sequence

import swimmer


class UIBuilder:
    """
    Builder class to construct the user interface

    The user interface is not fully initialised until the `build` method is called

    Attributes
    ----------
    root
        The parent widget to place the UI in
    swimmers : Sequence[swimmer.Swimmer]
        The loaded database of swimmers
    left_list : tkinter.Listbox
        Left listbox containing the initial loaded data
    right_list : tkinter.Listbox
        Right listbox containing the modified data
    """

    def __init__(self, root) -> None:
        """
        Construct a new UIBuilder instance

        Defines the main window and widget's but doesn't populate the data

        Parameters
        ----------
        root
            parent widget to the UI into
        """
        self.root = root
        root.geometry("560x150")
        root.title("Swimmer Rankings")

        self.left_list = tk.Listbox(root, width=40)
        self.left_list.grid(row=0, column=0, rowspan=4, sticky=tk.W)

        self.right_list = tk.Listbox(width=40)
        self.right_list.grid(row=0, column=2, rowspan=4, sticky=tk.E)

    def build(self) -> None:
        """
        Finalises construction of the UI

        Loads swim data and constructs the buttons
        to load and manipulate the data
        """

        swimmers = swimmer.load_swimmers("Swimmers.txt")
        self.swimmers = sorted(swimmers, key=lambda x: x.seed_time)
        self.fill_list(self.left_list, self.swimmers)

        def reference() -> None:
            """
            Perform reference binding and sort,
            then update the displayed right-hand list
            """
            swimmers = self.swimmers
            swimmers.sort(key=lambda x: x.sex)
            self.fill_list(self.right_list, swimmers)

        reference_button = tk.ttk.Button(self.root, text="Reference", command=reference)
        reference_button.grid(row=0, column=1)

        def copy() -> None:
            """
            Copy the swimmers list using `sorted`
            then update the displayed right-hand list
            """
            swimmers = sorted(self.swimmers, key=lambda x: x.sex)
            self.fill_list(self.right_list, swimmers)

        copy_button = tk.ttk.Button(self.root, text="Copy", command=copy)
        copy_button.grid(row=1, column=1)

        def refresh() -> None:
            """
            Refresh the left-hand list with the current `self.swimmers` value
            """
            self.left_list.delete(0, tk.END)
            self.fill_list(self.left_list, self.swimmers)

        refresh_button = tk.ttk.Button(self.root, text="Refresh", command=refresh)
        refresh_button.grid(row=2, column=1)

        def restore() -> None:
            """
            Restore the left-hand list from the file
            """
            swimmers = swimmer.load_swimmers("Swimmers.txt")
            self.swimmers = sorted(swimmers, key=lambda x: x.seed_time)
            self.fill_list(self.left_list, self.swimmers)

        restore_button = tk.ttk.Button(self.root, text="Restore", command=restore)
        restore_button.grid(row=3, column=1)

    def fill_list(
        self, listbox: tk.Listbox, swimmers: Sequence[swimmer.Swimmer]
    ) -> None:
        """
        Fill a given listbox with the provided swimmers

        Parameters
        ----------
        listbox : tk.Listbox
            The listbox to populate
        swimmers : Sequence[swimmer.Swimmer]
            Swimmers to load into the listbox
        """
        listbox.delete(0, tk.END)
        for swim in swimmers:
            text = str(swim)
            listbox.insert(tk.END, text)


def main():
    root = tk.Tk()
    builder = UIBuilder(root)
    builder.build()
    tk.mainloop()


if __name__ == "__main__":
    main()
