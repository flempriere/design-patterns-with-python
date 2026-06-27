import tkinter as tk
import tkinter.messagebox


class OKButton(tk.Button):
    def __init__(self, root, boxes):
        super().__init__(root, text="Order", command=self.clicked)

        self.boxes = boxes

    def clicked(self):

        order = "\n".join([f"{box.text} {box.get_state()}" for box in self.boxes])
        tk.messagebox.showinfo(title="Order Confirmed", message=order)


class CheckBox(tk.Checkbutton):
    def __init__(self, root, text, group):
        super().__init__(root, text=text, variable=group)

        self.text = text
        self.group = group

        if self.text.lower() == "pineapple":
            self.configure(state=tk.DISABLED)

    def get_state(self):
        return self.group.get()


class PizzaToppingsSelection:
    def build(self):

        root = tk.Tk()

        names = ["Cheese", "Pepperoni", "Mushrooms", "Sausage", "Peppers", "Pineapple"]
        boxes = [CheckBox(root, name, tk.IntVar()) for name in names]
        for idx, box in enumerate(boxes):
            box.grid(column=0, row=idx, sticky=tk.W)

        OKButton(root, boxes).grid(column=1, row=3, padx=20)

        tk.mainloop()


if __name__ == "__main__":
    pizza_toppings_selection = PizzaToppingsSelection()
    pizza_toppings_selection.build()
