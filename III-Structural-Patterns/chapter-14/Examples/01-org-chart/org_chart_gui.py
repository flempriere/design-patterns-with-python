"""
Tree-based GUI front-end to the Employee Library
for presenting an organisation chart using the
Composite Pattern
"""

import decimal
import random
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk

import employees


class UIBuilder:
    """
    Build and run the UI

    `build` must be called to configure the UI, `build_tree` can then be used
    to run the program
    """

    def _calculate_cost(self, name) -> decimal.Decimal | None:
        if name == self.org_chart.name:
            cost = self.org_chart.cost
        elif department := self.org_chart.get_child(name):
            cost = department.cost
        else:
            return None
        return cost

    def build_org_chart(self):

        ceo = employees.ManagingPosition("CEO", decimal.Decimal(200_000))

        # Create marketing hierarchy
        marketing_vp = employees.ManagingPosition(
            "Vice President (Marketing)", salary=decimal.Decimal(100_000)
        )

        sales_mgr = employees.ManagingPosition(
            "Manager (Sales)", salary=decimal.Decimal(50_000)
        )
        marketing_mgr = employees.ManagingPosition(
            name="Manager (Marketing)", salary=decimal.Decimal(50_000)
        )

        ceo.add_direct_report(marketing_vp)

        marketing_vp.add_direct_report(sales_mgr)
        marketing_vp.add_direct_report(marketing_mgr)

        SALARY_MAX_SHIFT = 10_000
        for i in range(0, 3):
            sales_mgr.add_direct_report(
                employees.JobPosition(
                    f"Sales ({i})",
                    salary=decimal.Decimal(
                        30_000 + random.randint(0, SALARY_MAX_SHIFT)
                    ),
                )
            )

        marketing_mgr.add_direct_report(
            employees.JobPosition("Secy", salary=decimal.Decimal(20_000))
        )

        # create production hierarchy
        production_vp = employees.ManagingPosition(
            name="Vice President (Production)", salary=decimal.Decimal(100_0000)
        )

        ceo.add_direct_report(production_vp)

        production_mgr = employees.ManagingPosition(
            "Manager (Production)", salary=decimal.Decimal(40_000)
        )
        shipping_mgr = employees.ManagingPosition(
            "Manager (Shipping)", salary=decimal.Decimal(35_000)
        )

        production_vp.add_direct_report(production_mgr)
        production_vp.add_direct_report(shipping_mgr)

        for i in range(0, 4):
            production_mgr.add_direct_report(
                employees.JobPosition(
                    f"Manufacturing ({i})",
                    salary=decimal.Decimal(
                        25_000 + random.randint(0, SALARY_MAX_SHIFT)
                    ),
                )
            )

        for i in range(0, 4):
            shipping_mgr.add_direct_report(
                employees.JobPosition(
                    f"Clerk ({i})",
                    salary=decimal.Decimal(
                        20_000 + random.randint(0, SALARY_MAX_SHIFT)
                    ),
                )
            )

        self.org_chart = ceo

    def build(self):

        self.build_org_chart()

        self.root = tk.Tk()
        self.root.geometry("200x300")
        self.root.title("Organisation Chart")

        self.frame = tk.ttk.Frame(self.root)
        self.frame.pack()

        self.tree = tk.ttk.Treeview(self.frame)
        entry = tk.ttk.Entry(self.frame)

        def calculate_salary():
            tree_focus = self.tree.focus()
            tree_item = self.tree.item(tree_focus)
            name = tree_item["text"]

            cost = self._calculate_cost(name)
            if cost is not None:
                entry.delete(0, tk.END)
                entry.insert(0, str(cost))
            else:
                tk.messagebox.showwarning(
                    title="Search Failed", message="Job Position Not Found!"
                )

        salary_button = tk.ttk.Button(
            self.frame, text="Calculate Costs", command=calculate_salary
        )

        self.tree.column("#0", width=250, minwidth=250, stretch=tk.NO)
        self.tree.pack()
        salary_button.pack()
        entry.pack()

    def build_tree(self) -> None:

        self.tree.heading("#0", text="Organisation Chart")

        def traverse_org(treeview_node: str, position: employees.JobPosition):

            subordinates = position.subordinates
            if not subordinates:
                return
            for sub_position in subordinates:
                new_node = self.tree.insert(
                    treeview_node, tk.END, text=sub_position.name
                )
                traverse_org(new_node, sub_position)

        root_node = self.tree.insert("", index=tk.END, text=self.org_chart.name)
        traverse_org(root_node, self.org_chart)
        tk.mainloop()


def main():
    ui = UIBuilder()
    ui.build()
    ui.build_tree()


if __name__ == "__main__":
    main()
