"""
Demonstrates the advantages of the bridge pattern in refactoring

Here we modify the bridge interface to provide the displays sorted in
alphabetical order without having to modify the underlying implementations
"""

import abc
import tkinter as tk
import tkinter.ttk
from typing import Sequence


class Product:
    """
    A basic class representing a product

    Parameters
    ----------
    name : str
        The name of the product
    count : int
        Stock level of the product
    """

    @classmethod
    def from_string(cls, product: str) -> Product:
        """
        Create a product from a delimited string

        The string must be delimited as `"name--count"`

        Parameters
        ----------
        product : str
            The delimited string to parse

        Returns
        -------
        Product
            Product created from the delimited string
        """
        name, count = product.split("--")
        name = name.strip()
        count = int(count.strip().replace(",", ""))

        return cls(name, count)

    def __init__(self, name: str, count: int) -> None:
        """
        Create a new Product

        Parameters
        ----------
        name : str
            Product name
        count : int
            Current product stock level
        """
        self.name = name
        self.count = count


def parse_products_from_file(file: str) -> Sequence[Product]:
    """
    Parse a list of products from a file

    Each of the products in the file must be a delimited string
    following the conventions of `Product.from_string`

    Parameters
    ----------
    file : str
        path to the file to parse

    Returns
    -------
    Sequence[Product]
        Products parsed from the file
    """
    with open(file) as file_stream:
        products = [Product.from_string(line) for line in file_stream.readlines()]
    return products


class Bridge(tk.ttk.Frame):
    """
    Bridge class defining a simple abstract interface
    """

    @abc.abstractmethod
    def add_data(self, products: Sequence[Product]) -> None:
        """
        Add data to a display
        """
        pass


class Display(tk.Widget):
    """
    Display class defining an abstract implementation
    """

    @abc.abstractmethod
    def add_lines(self, lines: Sequence[Product]) -> None:
        """
        Add lines to a display

        Parameters
        ----------
        lines : Sequence[Product]
            lines to add
        """
        pass


# Deprecated for this specific client in favour of the TreeDisplay
class ListBoxDisplay(Display, tk.Listbox):
    """
    A simple Product display using a Listbox
    """

    def __init__(self, frame) -> None:
        """
        Create a new ListBoxDisplay

        Parameters
        ----------
        frame : tk.ttk.Frame
            The frame to place the widget into
        """
        super().__init__(frame)

    def add_lines(self, lines: Sequence[Product]) -> None:
        for line in lines:
            self.insert(tk.END, line.name)


class TreeviewDisplay(Display, tk.ttk.Treeview):
    """
    A simple Product display using a Treeview to display a table
    """

    def __init__(self, frame) -> None:
        """
        Create a new TreeviewDisplay instance

        Parameters
        ----------
        frame :
            Frame to place the display within
        """
        super().__init__(frame)
        self["columns"] = "quantity"
        self.column("#0", width=150, minwidth=100, stretch=tk.NO)
        self.column("quantity", width=50, minwidth=50, stretch=tk.NO)

        self.heading("#0", text="Part")
        self.heading("quantity", text="Qty")

        self.idx = 0

    def add_lines(self, lines: Sequence[Product]) -> None:
        for line in lines:
            self.insert("", tk.END, text=line.name, values=(line.count,))


class TreeDisplay(Display, tk.ttk.Treeview):
    """
    A simple Product display using a Treeview to display a tree
    """

    def __init__(self, frame) -> None:
        """
        Create a new TreeDisplay instance

        Parameters
        ----------
        frame :
            Frame to place the display within
        """
        super().__init__(frame)
        self.column("#0", width=150, minwidth=100, stretch=tk.NO)
        self.idx = 0

    def add_lines(self, lines: Sequence[Product]) -> None:
        for line in lines:
            product_line = self.insert("", self.idx, text=line.name)
            self.insert(product_line, tk.END, text=str(line.count))
            self.idx += 1


class DisplayBridge(Bridge):
    """
    Concrete implementation of the Bridge connecting it to a display

    Attributes
    ----------
    display
        the display being bridged
    """

    def __init__(self, display: Display) -> None:
        """
        Create a new `DisplayBridge` instance

        Parameters
        ----------
        display : Display
            the display to bridge
        """
        self.display = display
        self.display.pack()

    def add_data(self, products: Sequence[Product]) -> None:
        self.display.add_lines(products)


class SortedDisplayBridge(Bridge):
    """
    Concrete implementation of the Bridge connecting it to a display,
    extended with additional functionality to sort the input alphabetically

    Attributes
    ----------
    display
        the display being bridged
    """

    def __init__(self, display: Display) -> None:
        """
        Create a new `SortedDisplayBridge` instance

        Parameters
        ----------
        display : Display
            the display to bridge
        """
        self.display = display
        self.display.pack()

    def add_data(self, products: Sequence[Product]) -> None:
        products = sorted(products, key=lambda x: x.name)
        self.display.add_lines(products)


class UIBuilder:
    """
    Creates the product UI

    The UI is not initialised until the `build` method is called
    """

    def __init__(self, root: tk.Tk) -> None:
        """
        Create a new UIBuilder

        Parameters
        ----------
        root : tk.Tk
            The base window to build the UI on
        """
        self.root = root

    def build(self) -> None:
        """
        Build the UI
        """
        self.root.geometry("335x200")
        self.root.title("Products")

        products = parse_products_from_file("../products.txt")
        left_frame = tk.ttk.Frame(self.root, width=200, borderwidth=2, relief=tk.GROOVE)
        left_label = tk.ttk.Label(left_frame, text="Customer View")
        left_label.pack(fill=tk.X)

        customer_display = TreeDisplay(left_frame)
        customer_bridge = SortedDisplayBridge(customer_display)
        customer_bridge.add_data(products)
        left_frame.grid(row=0, column=0, sticky=tk.N + tk.W)

        right_frame = tk.ttk.Frame(self.root)
        right_frame.grid(row=0, column=1, sticky=tk.E)
        right_label = tk.ttk.Label(right_frame, text="Executive View")
        right_label.pack(fill=tk.X)

        treeview_display = TreeviewDisplay(right_frame)
        treeview_bridge = SortedDisplayBridge(treeview_display)
        treeview_bridge.add_data(products)


def main():
    root = tk.Tk()
    ui = UIBuilder(root)
    ui.build()
    tk.mainloop()


if __name__ == "__main__":
    main()
