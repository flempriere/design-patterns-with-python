"""
Library containing classes to manage an employment hierarchy

Demonstrates the Composite Pattern

Classes
-------

* Employee -- A basic employee that cannot supervise

  * Supervisor -- Extends Employee to allow for managing subordinates

Exceptions
----------

* EmployeeException -- Base Exception class for all Exceptions raised by this module

"""

import decimal
from typing import override


class EmployeeException(Exception):
    """
    Base Exception for the employees module
    """

    pass


class JobPosition:
    """
    Represents an job position with a name and salary

    The base class is not able to manage a position

    Attributes
    ----------
    name: str
        The name of the job position
    salary: decimal.Decimal
        Salary attached to this position
    """

    def __init__(
        self, name: str, salary: decimal.Decimal, parent: JobPosition | None = None
    ) -> None:
        """
        Create a new `JobPosition` with an associated name and salary

        Parameters
        ----------
        name : str
            The job title
        salary : decimal.Decimal
            Role's salary
        parent : JobPosition | None, optional
            Role's direct supervisor if it exists, by default None
        """
        self.name = name
        self.salary = salary
        self.parent = parent

    def __str__(self) -> str:
        return f"{self.name} {self.salary}"

    @property
    def cost(self) -> decimal.Decimal:
        """
        The cost of this position and all subordinate positions

        Returns
        -------
        decimal.Decimal
            cost of this job position
        """
        return self.salary

    @property
    def supervisor(self) -> JobPosition | None:
        """
        Job Position's direct supervisor

        Returns
        -------
        JobPosition | None
            Immediate supervisor if the position exists, else `None`
        """
        return self.parent

    @property
    def subordinates(self) -> list[JobPosition]:
        """
        The list of direct subordinates to this role

        Returns
        -------
        list[JobPosition]
            Direct reports to this position, empty if none exist
        """
        return []

    def add_direct_report(self, employee: JobPosition) -> None:
        """
        Add a direct report to this employee

        Parameters
        ----------
        employee : JobPosition
            The position to add as a direct report

        Raises
        ------
        EmployeeException
            Raised if this employee cannot accept direct reports
        """
        raise EmployeeException("Employee is not authorised to supervise")

    def print_hierarchy(self, indent: int = 0) -> None:
        """
        Pretty print the job with a given indent

        Designed to be able to recursively pretty print an org chart

        Parameters
        ----------
        indent : int, optional
            amount of whitespace to indent this job description, by default 0
        """
        print(" " * indent + self.__str__())

    def get_child(self, name: str) -> JobPosition | None:
        """
        Retrieve the child job position with the given name

        Recursively searches through all reports and returns the first match

        Parameters
        ----------
        name : str
            position title to retrieve

        Returns
        -------
        JobPosition | None
            First JobPosition found matching the name,
            or `None` if no matches found
        """
        return None


class ManagingPosition(JobPosition):
    """
    Represents an job position capable of managing
    subordinates

    Attributes
    ----------
    name: str
        The name of the job position
    salary: decimal.Decimal
        Salary attached to this position
    """

    def __init__(
        self, name, salary: decimal.Decimal, parent: JobPosition | None = None
    ) -> None:
        super().__init__(name, salary, parent)
        self._subordinates: list[JobPosition] = []

    @override
    @property
    def cost(self) -> decimal.Decimal:
        total_cost = self.salary + sum(
            [subordinate.cost for subordinate in self.subordinates]
        )
        if total_cost:
            return total_cost
        else:
            return decimal.Decimal(0)

    @override
    @property
    def subordinates(self) -> list[JobPosition]:
        return self._subordinates

    @override
    def add_direct_report(self, employee: JobPosition) -> None:
        self._subordinates.append(employee)

    @override
    def print_hierarchy(self, indent: int = 0) -> None:
        super().print_hierarchy(indent)  # print this level
        for child in self.subordinates:
            child.print_hierarchy(indent=indent + 2)

    @override
    def get_child(self, name: str) -> JobPosition | None:
        for child in self.subordinates:
            if child.name == name:
                return child
            elif found := child.get_child(name):
                return found
        return None
