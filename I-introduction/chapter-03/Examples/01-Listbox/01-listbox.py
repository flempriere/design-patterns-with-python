import csv
import dataclasses
import tkinter as tk


def generate_csv(file_path):
    with open(file_path, newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            yield tuple(row)


@dataclasses.dataclass
class State:
    name: str
    abbrev: str
    capital: str
    founded: str
    population: str


class StatesList:
    def __init__(self, states_file):
        header, *rows = generate_csv(states_file)
        self.states = [State(*row) for row in rows]


class UIBuilder:
    def __init__(self, root, states_list):
        self.states = states_list
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox.grid(column=0, row=0, rowspan=4, padx=10)
        for state in self.states.states:
            self.listbox.insert(tk.END, state.name)


def main():
    states_file = "../sample_data.csv"

    root = tk.Tk()
    root.geometry("300x200")
    root.title("Simple Listbox Demo")

    UIBuilder(root, StatesList(states_file))

    tk.mainloop()


if __name__ == "__main__":
    main()
