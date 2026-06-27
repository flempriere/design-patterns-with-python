import tkinter as tk


class Greeter:
    def build(self):
        root = tk.Tk()
        tk.Label(
            root,
            text="What is your name?",
            justify=tk.LEFT,
            fg="blue",
            pady=10,
            padx=20,
        ).pack()

        # set up the Entry widget
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        # associate button to read the entry
        self.ok_button = tk.Button(root, text="Ok", command=self.get_name)
        self.ok_button.pack()

        # set up greater output
        self.greet_label = tk.Label(root, text="", fg="blue")
        self.greet_label.pack()

        tk.mainloop()

    def get_name(self):
        new_name = self.name_entry.get()
        self.greet_label.configure(text="Hi " + new_name + "!")


if __name__ == "__main__":
    greeter = Greeter()
    greeter.build()
