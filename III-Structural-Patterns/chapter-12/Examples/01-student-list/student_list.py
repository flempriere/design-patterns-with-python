import tkinter as tk
import tkinter.ttk


class DerivedListbox(tk.Listbox):
    def __init__(self, root) -> None:
        super().__init__(root)

    def selected(self):
        selection = self.curselection()
        selected_index = selection[0]
        return self.get(selected_index)

    def delete_selected(self) -> None:
        selection = self.curselection()
        selected_index = selection[0]
        self.delete(selected_index)

    def append(self, text: str) -> None:
        self.insert(tk.END, text)


class UIBuilder:
    def __init__(self, root):
        self.root = root

    def build(self):
        self.root.geometry("300x200")
        self.root.title("Student List")

        self.entry = tk.Entry(self.root)
        self.entry.grid(row=0, column=0)

        self.left_list = DerivedListbox(self.root)
        self.left_list.grid(row=1, column=0, rowspan=4)

        self.right_list = DerivedListbox(self.root)
        self.right_list.grid(row=1, column=2, rowspan=4)

        def enter_name():
            text = self.entry.get()
            self.left_list.append(text)
            self.entry.delete(0, tk.END)

        entry_button = tk.ttk.Button(self.root, text="Insert", command=enter_name)
        entry_button.grid(row=0, column=1, sticky=tk.W)

        def move_selection(source: DerivedListbox, destination: DerivedListbox):

            selected = source.selected()
            destination.append(selected)
            source.delete_selected()

        add_button = tk.ttk.Button(
            self.root,
            text="Add",
            command=lambda: move_selection(self.left_list, self.right_list),
        )
        add_button.grid(row=1, column=1)

        remove_button = tk.ttk.Button(
            self.root,
            text="Remove",
            command=lambda: move_selection(self.right_list, self.left_list),
        )
        remove_button.grid(row=2, column=1)


def main():
    root = tk.Tk()
    builder = UIBuilder(root)
    builder.build()
    tk.mainloop()


if __name__ == "__main__":
    main()
