import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
from typing import Iterable

import swim_events


class UIBuilder:
    """
    Simple builder class which constructs and stores the UI

    Attributes
    ----------
    self.root:
        Parent tk widget
    self.event_list: tk.Listbox
        Menu containing the list of swim events
        that can be displayed
    self.swimmer_table: tk.ttk.Treeview
        The currently displayed swim event

    Warning
    -------
    UI attributes are not defined until the `build`
    method has been called on an instance
    """

    def __init__(self, root):
        """
        Create a new UIBuilder instance

        Parameters
        ----------
        root:
            Parent widget
        """
        self.root = root
        root.title("Swim Events")

    def build(self):
        """
        Construct the UI

        Populates the `self.event_list` and `self.swimmer_table` attributes
        """

        self.root.geometry("400x200")

        self.event_list = tk.Listbox(self.root)
        self.event_list.insert(tk.END, "500 Free")
        self.event_list.insert(tk.END, "100 Free")
        self.event_list.grid(row=0, column=0)
        self.event_list.bind("<<ListboxSelect>>", self.select_swim_event)

        tree = tk.ttk.Treeview(self.root)

        def configure_column(column, width, text, minwidth=None):
            if minwidth is not None:
                tree.column(column, width=width, minwidth=minwidth, stretch=tk.NO)
            else:
                tree.column(column, width=width, stretch=tk.NO)
            tree.heading(column, text=text)

        tree["columns"] = ("lane", "name", "age", "seed")
        configure_column("#0", width=40, minwidth=10, text="H")
        configure_column("lane", width=30, text="L")
        configure_column("name", width=100, text="Name")
        configure_column("age", width=40, text="Age")
        configure_column("seed", width=50, text="Seed")

        style = tk.ttk.Style()
        style.configure("Treeview.Heading", font=(None, 10, "bold"))

        self.swimmer_table = tree
        self.swimmer_table.grid(row=0, column=1, pady=10, sticky="nsew")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)

    def select_swim_event(self, event):
        """
        Callback to handle when the currently selected event changes

        Updates the displayed table to correspond to the selected event
        in `self.event_list`

        Parameters
        ----------
        event:
            tkinter event that triggered this callback
        """
        index = int(self.event_list.curselection()[0])

        # store events in an internal look-up table of
        # the data file and the corresponding event type
        events = [
            ("500free.txt", swim_events.TimedFinalEvent),
            ("100free.txt", swim_events.PreliminaryEvent),
        ]

        try:
            event_file, event_format = events[index]
            swimmers = swim_events.load_swimmers(event_file, delimiter=" ")
        except IndexError:
            tk.messagebox.showerror(
                title="Invalid Event Selected",
                message="Current Selection does not match any event",
            )
            return
        except FileNotFoundError:
            tk.messagebox.showerror(
                title="File Missing", message=f"Could not find event file {event_file}"
            )
            return
        swim_event = event_format(swimmers, lanes=6)
        seeded_swimmers = swim_event.seeding().swimmers

        self.update_table(seeded_swimmers)

    def update_table(self, swimmers: Iterable[swim_events.Swimmer]):
        """
        Update the table to show the provided swimmers

        Clears the existing swimmers displayed in the table and
        inserts the swimmers provided

        Parameters
        ----------
        swimmers : Iterable[swim_events.Swimmer]
            swimmers to be displayed
        """
        # clear existing rows
        self.swimmer_table.delete(*self.swimmer_table.get_children())

        # Add new event
        for row, swimmer in enumerate(swimmers, start=1):
            text = str(swimmer.heat)
            values = (
                str(swimmer.lane),
                swimmer.name,
                str(swimmer.age),
                swimmer.seed_time.strftime(
                    "%M:%S.%f" if swimmer.seed_time.minute else "%S.%f"
                ),
            )
            self.swimmer_table.insert(parent="", index=row, text=text, values=values)


def main():
    root = tk.Tk()
    builder = UIBuilder(root)
    builder.build()
    root.mainloop()


if __name__ == "__main__":
    main()
