import tkinter as tk
import tkinter.messagebox


class DerivedButton(tk.Button):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        super().config(command=self.command)

    # abstract method to by overwritten by children
    def command(self):
        pass


class OKButton(DerivedButton):
    def __init__(self, root):
        super().__init__(root, text="OK")

    def command(self):
        tk.messagebox.showinfo("Our Message", "Tkinter is easy to use")


class QuitButton(DerivedButton):
    def __init__(self, root):
        super().__init__(root, text="Quit", fg="red")

    def command(self):
        quit()


def buildUI():
    root = tk.Tk()
    root.geometry("300x100+300+300")

    slogan = OKButton(root)
    slogan.pack(side=tk.LEFT, padx=10)

    button = QuitButton(root)
    button.pack(side=tk.RIGHT, padx=10)

    root.mainloop()


if __name__ == "__main__":
    buildUI()
