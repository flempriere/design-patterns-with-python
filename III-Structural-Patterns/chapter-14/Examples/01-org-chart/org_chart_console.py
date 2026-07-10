"""
Console-based front-end to the Employee Library
for presenting an organisation chart using the
Composite Pattern
"""

import decimal
import random

import employees


class UIBuilder:
    """
    Build and run the UI

    `build` must be called to configure the UI, `build_tree` can then be used
    to run the program
    """

    def build(self):
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

    def salary_span(self, name) -> None:
        if name == self.org_chart.name:
            cost = self.org_chart.cost
        elif department := self.org_chart.get_child(name):
            cost = department.cost
        else:
            print("Job Position not found!")
            return
        print(f"Salary span for {name}: {cost}")

    def build_tree(self) -> None:
        self.org_chart.print_hierarchy()

        while (name := input("Enter position to determine cost (q for quit): ")) != "q":
            self.salary_span(name)


def main():
    ui = UIBuilder()
    ui.build()
    ui.build_tree()


if __name__ == "__main__":
    main()
