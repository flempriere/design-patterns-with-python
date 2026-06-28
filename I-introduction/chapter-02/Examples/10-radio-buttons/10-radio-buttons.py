import tkinter as tk


class TrafficLightModeSelection:
    def build(self):
        root = tk.Tk()

        # set up the heading label
        tk.Label(
            root, text="Choose your favourite colour:", justify=tk.LEFT, padx=20
        ).pack()

        # label to be updated
        current_light_colour = tk.Label(root, text="")

        # set up the radio buttons
        traffic_light_choice = tk.IntVar()
        colours = ["red", "yellow", "green"]

        # closure function to be called
        def update_light_colour():

            colour_idx = traffic_light_choice.get()
            colour = colours[colour_idx]

            current_light_colour.configure(
                fg=colour,
                text=f"The light is {colour}",
            )

        buttons = [
            tk.Radiobutton(
                root,
                text=colour,
                padx=20,
                command=update_light_colour,
                variable=traffic_light_choice,
                value=i,
            )
            for i, colour in enumerate(colours)
        ]

        # set up the layout

        for button in buttons:
            button.pack()

        current_light_colour.pack()

        tk.mainloop()


if __name__ == "__main__":
    traffic_light_controller = TrafficLightModeSelection()
    traffic_light_controller.build()
