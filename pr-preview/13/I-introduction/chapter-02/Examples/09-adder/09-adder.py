import tkinter as tk
import tkinter.messagebox


class NumberEntry(tk.Frame):
    def __init__(self, master, label):

        super().__init__(master)

        label = tk.Label(self, text=label, width=3, fg="blue")
        label.pack(side=tk.LEFT, padx=5, pady=5)

        self.entry = tk.Entry(self)
        self.entry.pack(fill=tk.X, padx=5, pady=5)

    def get(self):
        return self.entry.get()


class Adder:
    def build(self):
        root = tk.Tk()
        tk.Label(
            root,
            text="Enter numbers to add",
            justify=tk.LEFT,
            fg="blue",
            pady=10,
            padx=20,
        ).pack()

        # Create each row of numbers
        self.x_row = NumberEntry(root, "x = ")
        self.x_row.pack()

        self.y_row = NumberEntry(root, "y = ")
        self.y_row.pack()

        # associate button to read the entry
        self.ok_button = tk.Button(root, text="Ok", command=self.add_numbers)
        self.ok_button.pack()

        # set up output
        self.sum_label = tk.Label(root, text="", fg="blue")
        self.sum_label.pack()

        tk.mainloop()

    def add_numbers(self):
        try:
            x = float(self.x_row.get())
            y = float(self.y_row.get())
            self.sum_label.configure(text="Sum = " + str(x + y))
        except ValueError:
            tk.messagebox.showerror("Conversion Error", "Not a number")


if __name__ == "__main__":
    adder = Adder()
    adder.build()
