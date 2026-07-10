"""
Decorated Button

demonstrates the use of the Decorator Pattern
to modify the appearance of a button in response
to the user's mouse movements
"""

import sys
import tkinter as tk
import tkinter.ttk


class Decorator(tk.ttk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.style = tk.ttk.Style()
        self.style.configure(style="Flat.TButton", relief=tk.FLAT)
        self.style.theme_use("alt")

        self.hover_style = tk.ttk.Style()
        self.hover_style.configure(style="Raise.TButton", relief=tk.RAISED)
        self.hover_style.theme_use("alt")

        self.configure(style="Flat.TButton")
        self.bind("<Enter>", func=lambda x: self.configure(style="Raise.TButton"))
        self.bind("<Leave>", func=lambda x: self.configure(style="Flat.TButton"))


class UIBuilder:
    def build(self):
        root = tk.Tk()
        root.geometry("200x100")
        root.title("Tk Buttons")

        first_button = Decorator(root, text="A button")
        second_button = Decorator(root, text="B button")
        quit_button = tk.ttk.Button(root, text="Quit", command=sys.exit)

        first_button.pack(pady=5)
        second_button.pack(pady=5)
        quit_button.pack(pady=5)

        tk.mainloop()


def main():
    ui = UIBuilder()
    ui.build()


if __name__ == "__main__":
    main()
