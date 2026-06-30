import sys
import tkinter as tk
import tkinter.ttk


class Name:
    def __init__(self):
        self.first = ""
        self.last = ""

    def __str__(self):
        if self.first:
            return self.first + " " + self.last
        else:
            return self.last


class FirstNameFirst(Name):
    def __init__(self, name_string: str):
        super().__init__()
        if (i := name_string.rfind(" ")) > 0:
            self.first = name_string[0:i].strip()
            self.last = name_string[i + 1 :].strip()
        else:
            self.last = name_string.strip()


class LastNameFirst(Name):
    def __init__(self, name_string: str):
        super().__init__()
        if (i := name_string.find(",")) > 0:
            self.first = name_string[0:i].strip()
            self.last = name_string[i + 1 :].strip()
        else:
            self.last = name_string.strip()


class NameFactory:
    def __init__(self, name_string: str):
        self.name = name_string

    def get_name(self):
        if self.name.find(",") > 0:
            return LastNameFirst(self.name)
        else:
            return FirstNameFirst(self.name)


class NameEntryForm:
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
        raw_name = self.name_entry.get()
        name = NameFactory(raw_name).get_name()

        self.first_name_display.insert(0, name.first)
        self.last_name_display.insert(0, name.last)

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.first_name_display.delete(0, tk.END)
        self.last_name_display.delete(0, tk.END)


def main():
    root = tk.Tk()
    NameEntryForm(root)
    tk.mainloop()


if __name__ == "__main__":
    main()
