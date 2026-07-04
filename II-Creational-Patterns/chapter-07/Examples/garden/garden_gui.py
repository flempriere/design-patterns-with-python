"""
GUI-based program for planning a garden
"""

import abc
import sys
import tkinter as tk
import tkinter.ttk

import garden


class DerivedButton(tk.ttk.Button):
    """
    A button that contains it's own callback

    Subclasses should implement the `command` method

    Parameters
    ----------
    gardener : Gardener
        gardener object responsible for drawing the
        garden
    """

    def __init__(self, master, gardener: Gardener, **kwargs) -> None:
        """
        Create a new instance for the given `gardener`

        Parameters
        ----------
        master :
            Parent widget
        gardener : Gardener
            gardener object responsible for drawing the
            garden
        """

        super().__init__(master, command=self.command, **kwargs)
        self.gardener = gardener

    @abc.abstractmethod
    def command(self) -> None:
        """
        The callback to be executed the button is clicked
        """
        pass


class ShadeButton(DerivedButton):
    """
    Button for setting a shade plant
    """

    def __init__(self, master, gardener: Gardener, **kwargs) -> None:
        super().__init__(master, gardener, **kwargs)

    def command(self) -> None:
        self.gardener.set_shade_plant()


class CentreButton(DerivedButton):
    """
    Button for setting the centre plant
    """

    def __init__(self, master, gardener: Gardener, **kwargs) -> None:
        super().__init__(master, gardener, **kwargs)

    def command(self) -> None:
        self.gardener.set_centre_plant()


class BorderButton(DerivedButton):
    """
    Button for setting the border plant
    """

    def __init__(self, master, gardener: Gardener, **kwargs) -> None:
        super().__init__(master, gardener, **kwargs)

    def command(self) -> None:
        self.gardener.set_border_plant()


class GardenChoiceButton(tk.Radiobutton):
    """
    Specialised Radio Button for selecting a type of garden

    Attributes
    ----------
    garden : garden.Garden
        garden associated with this choice
    gardener : Gardener
        gardener object responsible for drawing the
        garden
    """

    def __init__(
        self,
        root,
        name: str,
        garden: garden.Garden,
        gardener: Gardener,
        index: int,
        group: tk.IntVar,
    ) -> None:
        """
        Create a new choice and associate it to a given radio button group

        Parameters
        ----------
        root :
            parent widget
        name : str
            display name for this choice
        garden : garden.Garden
            garden instance associated with this class
        gardener : Gardener
            gardener object responsible for drawing the
            garden
        index : int
            index for this choice within the group
        group : tk.IntVar
            variable corresponding to the choice button group
        """

        super().__init__(
            root, text=name, command=self.command, variable=group, value=index
        )

        self.pack(anchor=tk.W)
        self.garden = garden
        self.gardener = gardener

    def command(self) -> None:
        """
        Set the gardener to draw the current garden and clear the canvas
        """
        self.gardener.garden = self.garden
        self.gardener.clear_canvas()


class Gardener:
    """
    Maintains and draws the Garden onto a canvas

    Methods should not called until the `build` method has been invoked

    Attributes
    ----------
    garden: garden.Garden
        The current garden to actively draw
    canvas: tk.Canvas
        The canvas to draw the garden on
    """

    def __init__(self) -> None:
        """
        Create a new `Gardener` instance

        By default draw's a vegetable garden
        """
        self.garden: garden.Garden = garden.VegetableGarden()

    def clear_canvas(self) -> None:
        """
        Clear the associated canvas and draw a blank garden
        """
        self.canvas.delete("all")
        self.canvas.create_oval(20, 20, 100, 100, fill="lightgray")

    def set_shade_plant(self) -> None:
        """
        Add the shade plant to the garden
        """
        self.canvas.create_text(60, 60, text=self.garden.get_shade_plant().name)

    def set_centre_plant(self) -> None:
        """
        Add the centre plant to the garden
        """
        self.canvas.create_text(100, 120, text=self.garden.get_centre_plant().name)

    def set_border_plant(self) -> None:
        """
        Add the border plant to the garden
        """
        self.canvas.create_text(75, 180, text=self.garden.get_border_plant().name)

    def build(self, root) -> None:
        """
        Build the user interface

        Parameters
        ----------
        root :
            The parent widget
        """
        root.title("Garden Planner")

        left_frame = tk.ttk.Frame(root)
        left_frame.grid(row=0, column=0)
        right_frame = tk.ttk.Frame(root)
        right_frame.grid(row=0, column=1)

        style = tk.ttk.Style()
        style.theme_use("alt")

        garden_type_label_frame = tk.ttk.LabelFrame(left_frame, text="Garden Type")
        garden_type_label_frame.grid(row=0)
        garden_selected = tk.IntVar()

        GardenChoiceButton(
            garden_type_label_frame,
            "Vegetable",
            index=0,
            garden=garden.VegetableGarden(),
            gardener=self,
            group=garden_selected,
        )

        GardenChoiceButton(
            garden_type_label_frame,
            "Annual",
            index=1,
            garden=garden.AnnualGarden(),
            gardener=self,
            group=garden_selected,
        )

        GardenChoiceButton(
            garden_type_label_frame,
            "Perennial",
            index=2,
            garden=garden.PerennialGarden(),
            gardener=self,
            group=garden_selected,
        )

        self.canvas = tk.Canvas(right_frame, width=200, height=200, bg="white")
        self.canvas.pack()
        self.canvas.create_oval(20, 20, 100, 100, fill="lightgrey")
        self.clear_canvas()

        right_subframe = tk.ttk.Frame(right_frame)
        right_subframe.pack()

        shade_button = ShadeButton(right_subframe, self, text="Shade")
        centre_button = CentreButton(right_subframe, self, text="Central")
        border_button = BorderButton(right_subframe, self, text="Border")

        quit_button = tk.ttk.Button(left_frame, text="Quit", command=sys.exit)

        shade_button.grid(row=0, column=0)
        centre_button.grid(row=0, column=1)
        border_button.grid(row=0, column=2)
        quit_button.grid(row=2, pady=50)


def main() -> None:
    root = tk.Tk()
    gardener = Gardener()
    gardener.build(root)

    tk.mainloop()


if __name__ == "__main__":
    main()
