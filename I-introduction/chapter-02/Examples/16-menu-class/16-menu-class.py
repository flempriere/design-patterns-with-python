import sys
import tkinter as tk
import tkinter.filedialog


class MenuBar(tk.Menu):
    def __init__(self, root):
        super().__init__(root)
        root.config(menu=self)


class TopMenu:
    def __init__(self, root, label, menu_bar):

        self.menu_bar = menu_bar
        self.root = root
        self.menu = tk.Menu()

        self.menu_bar.add_cascade(label=label, menu=self.menu)

    def add_menu_item(self, menu_item):
        self.menu.add_command(label=menu_item.get_label(), command=menu_item.command)

    def add_separator(self):
        self.menu.add_separator()


# Abstract base class for menu's
class MenuCommand:
    def __init__(self, root, label):
        self.root = root
        self.label = label

    def get_label(self):
        return self.label

    def command(self):
        pass


class QuitCommand(MenuCommand):
    def command(self):
        sys.exit()


class NewCommand(MenuCommand):
    def command(self):
        self.root.title("")


class OpenCommand(MenuCommand):
    def command(self):

        file_path = tk.filedialog.askopenfilename(title="Select File")
        if len(file_path.strip()) > 0:
            path_components = file_path.split("/")
            if len(path_components):
                file_name = path_components[-1]
                self.root.title(file_name)


class DrawCircle(MenuCommand):
    def __init__(self, root, canvas, label):
        super().__init__(root, label)
        self.canvas = canvas

    def command(self):
        self.canvas.create_oval(130, 40, 200, 110, fill="red")


class DrawSquare(MenuCommand):
    def __init__(self, root, canvas, label):
        super().__init__(root, label)
        self.canvas = canvas

    def command(self):
        self.canvas.create_rectangle(10, 80, 110, 180, fill="blue")


def build_menu(root):

    root.title("Menu Demo")
    root.geometry("300x200")
    canvas = tk.Canvas(root)
    canvas.pack()

    menu_bar = MenuBar(root)

    file_menu = TopMenu(root, "File", menu_bar)
    file_menu.add_menu_item(NewCommand(root, "New"))
    file_menu.add_menu_item(OpenCommand(root, "Open"))
    file_menu.add_separator()
    file_menu.add_menu_item(QuitCommand(root, "Quit"))

    draw_menu = TopMenu(root, "Draw", menu_bar)
    draw_menu.add_menu_item(DrawCircle(root, canvas, "Circle"))
    draw_menu.add_menu_item(DrawSquare(root, canvas, "Square"))


def main():
    root = tk.Tk()
    build_menu(root)
    tk.mainloop()


if __name__ == "__main__":
    main()
