"""
Demonstrates the builder pattern by using
a configurable GUI
"""

import abc
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk


class MultiChoiceWidget(abc.ABC):
    def __init__(self, frame, choice_list):
        self.choices = choice_list
        self.frame = frame

    @abc.abstractmethod
    def make_ui(self):
        pass

    @abc.abstractmethod
    def get_selected(self):
        pass

    def clear_all(self):
        for widget in self.frame.winfo_children():
            widget.destroy()


class ListboxChoice(MultiChoiceWidget):
    def __init__(self, frame, choices):
        super().__init__(frame, choices)

    def make_ui(self):

        self.clear_all()
        self.list = tk.Listbox(self.frame, selectmode=tk.MULTIPLE)
        self.list.pack()

        for choice in self.choices:
            self.list.insert(tk.END, choice)

    def get_selected(self):

        selection = [self.list.get(idx) for idx in self.list.curselection()]
        return selection


class Checkbox(tk.ttk.Checkbutton):
    def __init__(self, root, text) -> None:

        self.checked = tk.BooleanVar()
        super().__init__(root, text=text, variable=self.checked)

    @property
    def text(self) -> str:
        return self.cget("text")

    def is_checked(self) -> bool:
        return bool(self.checked.get())


class CheckboxChoice(MultiChoiceWidget):
    def __init__(self, panel, choices):
        super().__init__(panel, choices)

    def make_ui(self):
        self.clear_all()

        self.boxes = []
        for row, name in enumerate(self.choices):
            cb = Checkbox(self.frame, name)
            cb.grid(row=row, column=0, sticky=tk.W)
            self.boxes.append(cb)

    def get_selected(self):
        items = [box.text for box in self.boxes if box.is_checked()]
        return items


class Securities:
    def __init__(self, name, investments):
        self.name = name
        self.investments = investments


class UIBuilder:
    def __init__(self, root) -> None:

        self.root = root
        self.root.geometry("250x200")
        self.root.title("Wealth Tracker")

    def build(self):
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

        def show_selected():
            securities = self.choice_ui.get_selected()
            text = "\n".join(securities)
            tk.messagebox.showinfo(title="Selected securities", message=text)

        show_button = tk.ttk.Button(self.root, text="Show", command=show_selected)
        show_button.grid(row=1, column=0, columnspan=2)

    def selection_changed(self, event):
        index = int(self.security_type_selector.curselection()[0])
        security_category = self.securities[index]

        self.choice_ui = self.construct_choice_ui(
            security_category.investments, self.right_frame
        )
        self.choice_ui.make_ui()

    def selected(self):
        return self.choice_ui.get_selected()

    def construct_choice_ui(self, choices, frame) -> MultiChoiceWidget:
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
