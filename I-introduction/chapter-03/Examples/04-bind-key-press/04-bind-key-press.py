import bisect
import csv
import dataclasses
import tkinter as tk


def generate_csv(file_path):
    with open(file_path, newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            yield tuple([val.strip() for val in row])


@dataclasses.dataclass
class State:
    name: str
    abbrev: str
    capital: str
    founded: str
    population: str

    def to_dict(self):
        return {
            "State": self.name,
            "Abbrev": self.abbrev,
            "Capital": self.capital,
            "Founded": self.founded,
            "Capital Population": self.population,
        }


class StatesLoader:
    def __init__(self, states_file):
        header, *rows = generate_csv(states_file)
        self.header = header
        self.states = [State(*row) for row in rows]


class UIBuilder:
    def __init__(self, root, states_loader):

        states_loader = states_loader
        self.states = states_loader.states
        self.header = states_loader.header

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox.grid(column=0, row=0, rowspan=4, padx=10)
        for state in self.states:
            self.listbox.insert(tk.END, state.name)

        # create scrollbar and link to the listbox
        scrollbar = tk.Scrollbar(root, command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, rowspan=4, sticky=tk.N + tk.S)

        # make it so scrolling on the listbox adjusts the scroll bar in turn
        self.listbox.config(yscrollcommand=scrollbar.set)

        # create labels for data in the state list
        self.state_labels = {
            column_name: tk.Label(root, text="") for column_name in self.header
        }
        try:
            self.state_labels["Abbrev"].config(fg="red")
        except KeyError:
            pass

        for idx, label in enumerate(self.state_labels.values()):
            label.grid(column=2, row=idx, sticky=tk.W)

        self.listbox.bind("<<ListboxSelect>>", self.state_selected)

        # create Entry so that we can jump alphabetically
        self.entry = tk.Entry(root)
        self.entry.grid(column=0, row=4, pady=4)
        self.entry.focus_set()  # makes this the focus of the window
        self.entry.bind("<Key>", self.key_press)

    def state_selected(self, event):
        idx = int(self.listbox.curselection()[0])
        state = self.states[idx]

        for key, val in state.to_dict().items():
            self.state_labels[key].config(text=val)

    def key_press(self, event):
        char = event.char.upper()

        def find_closest():
            idx = bisect.bisect_left(self.states, char, key=lambda x: x.name)
            if idx != len(self.states):
                return idx
            return 0

        idx = find_closest()

        # reset the entry
        self.entry.delete(0, tk.END)

        # Update the listbox to the new selection, discarding the old and scrolling so its visible
        self.listbox.select_clear(0, tk.END)
        self.listbox.select_set(idx)
        self.listbox.see(idx)

        # call the function triggered a new selection
        self.state_selected(event)


def main():
    states_file = "../sample_data.csv"

    root = tk.Tk()
    root.geometry("300x200")
    root.title("State Data Demo")

    UIBuilder(root, StatesLoader(states_file))

    tk.mainloop()


if __name__ == "__main__":
    main()
