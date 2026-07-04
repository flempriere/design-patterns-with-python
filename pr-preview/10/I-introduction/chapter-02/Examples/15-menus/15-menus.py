import tkinter as tk


def build_menu(root):

    root.title("Menu Demo")
    root.geometry("300x200")

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_separator()
    file_menu.add_command(label="Exit")

    draw_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Draw", menu=draw_menu)
    draw_menu.add_command(label="Circle")
    draw_menu.add_command(label="Square")


def main():
    root = tk.Tk()
    build_menu(root)
    tk.mainloop()


if __name__ == "__main__":
    main()
