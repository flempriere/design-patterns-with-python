import tkinter as tk
from typing import Literal


class ColourButton(tk.Radiobutton):
    # define the group variable
    # We have to wait until we create a root window before we can set it
    group: tk.IntVar | Literal[""] = ""

    def __init__(self, master, colour, index, colour_label):
        super().__init__(
            master,
            text=colour,
            padx=20,
            command=self.clicked,
            variable=ColourButton.group,
            value=index,
        )

        self.pack(anchor=tk.W)
        self.colour = colour
        self.colour_label = colour_label
        self.index = index

    def clicked(self):
        self.colour_label.configure(fg=self.colour, text=f"The light is {self.colour}")


class TrafficLightModeSelection:
    def build(self):
        root = tk.Tk()

        # set up the heading label
        tk.Label(
            root, text="Choose your favourite colour:", justify=tk.LEFT, padx=20
        ).pack()

        # set up the output label
        colour_label = tk.Label(root, text="")

        # set up radio buttons
        ColourButton.group = tk.IntVar()
        colours = ["red", "yellow", "green"]
        for idx, colour in enumerate(colours):
            ColourButton(root, colour, idx, colour_label=colour_label)

        colour_label.pack()
        root.mainloop()


if __name__ == "__main__":
    traffic_light_selection = TrafficLightModeSelection()
    traffic_light_selection.build()
