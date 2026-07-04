import tkinter


class Rectangle:
    def __init__(self, canvas: tkinter.Canvas):
        self.canvas = canvas

    def draw(self, x, y, width, height):
        self.canvas.create_rectangle(x, y, x + width, y + height)


class Square(Rectangle):
    def __init__(self, canvas: tkinter.Canvas):
        super().__init__(canvas)

    def draw(self, x: int | float, y: int | float, width: int | float):  # ty:ignore[invalid-method-override]
        super().draw(x, y, width, width)


def main():
    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, width=500, height=500)
    canvas.grid(row=0, column=0)

    rectangle = Rectangle(canvas)
    rectangle.draw(30, 10, 120, 80)

    square = Square(canvas)
    square.draw(200, 50, 60)

    root.mainloop()


if __name__ == "__main__":
    main()
