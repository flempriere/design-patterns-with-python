import csv
import dataclasses
import tkinter as tk
import tkinter.ttk
from typing import Iterator


def generate_csv(file_path) -> Iterator[tuple[str, ...]]:
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

    def to_tuple(self) -> tuple[str, ...]:
        return (self.name, self.abbrev, self.capital, self.founded, self.population)


class StatesLoader:
    def __init__(self, states_file):
        header, *rows = generate_csv(states_file)
        self.header = header
        self.states = [State(*row) for row in rows]


class UIBuilder:
    def __init__(self, root, states_loader):

        states_loader: StatesLoader = states_loader
        self.states = states_loader.states
        self.header = states_loader.header

        # slice off the first header since that's column #0
        columns = self.header[1:]

        tree = tk.ttk.Treeview(root, columns=columns)
        tree.column("#0", width=120, minwidth=120, stretch=tk.NO)

        for column in columns:
            tree.column(column, width=120, minwidth=120, stretch=tk.NO)

        # create headings
        style = tk.ttk.Style()
        style.configure("Treeview.Heading", font=(None, 10, "bold"))

        for column, label in zip(("#0",) + columns, self.header):
            tree.heading(column, text=label)

        # insert the data rows
        for idx, state in enumerate(self.states):
            tree.insert("", idx, text=state.name, values=state.to_tuple()[1:])

        tree.pack(side=tk.TOP, fill=tk.X)


def main():
    states_file = "../sample_data.csv"

    root = tk.Tk()
    root.geometry("600x200")
    root.title("Treeview Demo")

    UIBuilder(root, StatesLoader(states_file))

    tk.mainloop()


if __name__ == "__main__":
    main()
