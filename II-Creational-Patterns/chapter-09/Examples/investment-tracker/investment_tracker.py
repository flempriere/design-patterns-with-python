"""
Demonstrates the builder pattern by using
a configurable GUI
"""

import abc
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
from typing import Sequence, override


class MultiChoiceWidget(abc.ABC):
    """
    Abstract widget that allows the user to select multiple options from a collection

    Once instantiated the UI must be constructed via the `make_ui` method.
    Subclasses should override the `make_ui` and `get_selected` methods.

    Parameters
    ----------
    frame
        parent widget
    choices : Sequence[str]
        options that can be selected
    """

    def __init__(self, frame, choices: Sequence[str]) -> None:
        """
        Construct a new MultiChoiceWidget for the given choices

        Parameters
        ----------
        frame :
            parent widget

        choices : Sequence[str]
            choices to add to this widget
        """
        self.choices = choices
        self.frame = frame

    @abc.abstractmethod
    def make_ui(self) -> None:
        """
        Construct the Widget
        """
        pass

    @abc.abstractmethod
    def get_selected(self) -> Sequence[str]:
        """
        Retrieve the currently selected elements

        Returns
        -------
        Sequence[str]
            The currently selected choices
        """
        pass

    def clear_all(self) -> None:
        """
        Delete the current widget from the screen
        """
        for widget in self.frame.winfo_children():
            widget.destroy()


class ListboxChoice(MultiChoiceWidget):
    """
    MultipleChoiceWidget implemented via a Listbox

    Parameters
    ----------
    list : tkinter.Listbox
        The listbox
    """

    def __init__(self, frame, choices: Sequence[str]) -> None:
        super().__init__(frame, choices)

    @override
    def make_ui(self) -> None:

        self.clear_all()
        self.list = tk.Listbox(self.frame, selectmode=tk.MULTIPLE)
        self.list.pack()

        for choice in self.choices:
            self.list.insert(tk.END, choice)

    @override
    def get_selected(self) -> Sequence[str]:

        selection: list[str] = [self.list.get(idx) for idx in self.list.curselection()]
        return selection


class Checkbox(tk.ttk.Checkbutton):
    """
    Checkbox wrapper class to provide easy access to state and text

    Parameters
    ----------
    checked : tkinter.BooleanVar
        tkinter variable containing the state
    """

    def __init__(self, root, text: str) -> None:
        """
        Create a new checkbox with the provided `text` as a label

        Parameters
        ----------
        root :
            parent widget

        text : str
            checkbox text
        """
        self.checked = tk.BooleanVar()
        super().__init__(root, text=text, variable=self.checked)

    @property
    def text(self) -> str:
        """
        The text label of this checkbox

        Returns
        -------
        str
            The checkboxes text label
        """
        return self.cget("text")

    def is_checked(self) -> bool:
        """
        The current button state

        Returns
        -------
        bool
            Indicates the state of the button
        """
        return bool(self.checked.get())


class CheckboxChoice(MultiChoiceWidget):
    """
    MultipleChoiceWidget implemented via a Checkbox

    Parameters
    ----------
    boxes: Sequence[Checkbox]
        checkboxes associated with this widget
    """

    def __init__(self, panel, choices: Sequence[str]) -> None:
        super().__init__(panel, choices)

    def make_ui(self) -> None:
        self.clear_all()

        self.boxes: list[Checkbox] = []
        for row, name in enumerate(self.choices):
            cb = Checkbox(self.frame, name)
            cb.grid(row=row, column=0, sticky=tk.W)
            self.boxes.append(cb)

    def get_selected(self) -> Sequence[str]:
        items: list[str] = [box.text for box in self.boxes if box.is_checked()]
        return items


class Securities:
    """
    A simple class representing a type of securities

    Attributes
    ----------
    name : str
        name of the securities category

    investments: Sequence[str]
        securities associated with this category
    """

    def __init__(self, name: str, investments: Sequence[str]) -> None:
        """
        Create a new Securities instance

        Parameters
        ----------
        name : str
            category of the securities

        investments : Sequence[str]
            securities associated with this category
        """
        self.name = name
        self.investments = investments


class UIBuilder:
    """
    Builder class for assembling the user interface

    Attributes should not accessed until the `build` method has been
    called to construct the UI

    Attributes
    ----------
    root:
        Parent widget to place the UI in

    securities: Sequence[Securities]
        Securities to be loaded into the UI

    security_type_selector: tkinter.Listbox
        Widget to select the category of securities

    right_frame: tkinter.ttk.Frame | tkinter.Frame
        Widget to place the multichoice selection into

    choice_ui: MultiChoiceWidget
        Current multiple choice selection widget
    """

    def __init__(self, root) -> None:
        """
        Crreate a new UIBuilder instance for the given root widget

        Parameters
        ----------
        root :
            Parent widget to place the UI into
        """
        self.root = root
        self.root.geometry("250x200")
        self.root.title("Wealth Tracker")

    def build(self) -> None:
        """
        Create the UI and initialise the attributes
        """
        stocks = Securities(
            "Stocks",
            investments=[
                "Cisco",
                "Coca Cola",
                "General Electric",
                "Harley Davidson",
                "IBM",
            ],
        )
        bonds = Securities(
            "Bonds",
            investments=["CT State GO 2024", "New York GO 2026", "GE Corp Bonds"],
        )
        mutuals = Securities(
            "Mutuals",
            investments=[
                "Fidelity Magellan",
                "T Rowe Prices",
                "Vanguard Primecap",
                "Lindner",
            ],
        )

        self.securities = [stocks, bonds, mutuals]

        left_frame = tk.ttk.Frame(self.root)
        left_frame.grid(row=0, column=0)

        self.security_type_selector = tk.Listbox(left_frame, exportselection=tk.FALSE)
        self.security_type_selector.pack()

        for security in self.securities:
            self.security_type_selector.insert(tk.END, security.name)

        self.security_type_selector.bind("<<ListboxSelect>>", self.selection_changed)

        self.right_frame = tk.ttk.Frame(self.root)
        self.right_frame.grid(row=0, column=1)

        def show_selected() -> None:
            """
            Display the currently selected options

            Invokes a Messagebox
            """
            securities = self.choice_ui.get_selected()
            text = "\n".join(securities)
            tk.messagebox.showinfo(title="Selected securities", message=text)

        show_button = tk.ttk.Button(self.root, text="Show", command=show_selected)
        show_button.grid(row=1, column=0, columnspan=2)

    def selection_changed(self, event) -> None:
        """
        Callback function for when the selected securities category has changed

        Creates and applies the correct `MultiChoiceWidget`

        Parameters
        ----------
        event :
            event that triggered the callback
        """
        index = int(self.security_type_selector.curselection()[0])
        security_category = self.securities[index]

        self.choice_ui = self.construct_choice_ui(
            security_category.investments, self.right_frame
        )
        self.choice_ui.make_ui()

    def construct_choice_ui(self, choices: Sequence[str], frame) -> MultiChoiceWidget:
        """
        Build the appropriate `MultiChoiceWidget` for the given selection

        Parameters
        ----------
        choices : Sequence[str]
            options to add to the MultiChoiceWidget
        frame :
            parent widget to place the MultiChoiceWidget into

        Returns
        -------
        MultiChoiceWidget
            The newly constructed widget
        """
        if len(choices) <= 3:
            return CheckboxChoice(frame, choices)
        else:
            return ListboxChoice(frame, choices)


def main():
    root = tk.Tk()
    builder = UIBuilder(root)
    builder.build()

    tk.mainloop()


if __name__ == "__main__":
    main()
