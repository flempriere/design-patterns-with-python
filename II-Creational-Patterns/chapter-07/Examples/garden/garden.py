"""
Garden
------

A basic library demonstrating the Abstract Factory Method Pattern
via implementing a system for constructing different gardening events

Classes
-------

* `Plant` -- A plant type for a garden
* `Garden` -- Abstract class representing a garden

  * `VegetableGarden` -- Provides a factory for a vegetable garden
  * `AnnualGarden` -- Provides a factory for an annual garden
  * `PerennialGarden` -- Provides a factory for a perennial garden
"""

import abc
from typing import override


class Plant:
    """
    Represents a plant in a garden

    Attributes
    ----------
    self.name : str
        Plant's name (common or scientific)
    """

    def __init__(self, name) -> None:
        """
        Create a new plant instance with the given name

        Parameters
        ----------
        name : str
            name of the plant (common or scientific)
        """
        self.name = name


class Garden(abc.ABC):
    """
    Abstract class representing a garden

    Provides methods for retrieving plant's suitable
    for that garden.

    Subclasses should override the

    * `get_shade_plant`
    * `get_centre_plant`
    * `get_border_plant`

    methods to return the appropriate `Plant` instances
    """

    @abc.abstractmethod
    def get_shade_plant(self) -> Plant:
        """
        Retrieve a plant corresponding to this garden
        that can live in the shade

        Returns
        -------
        Plant
            A shade-loving plant
        """
        pass

    @abc.abstractmethod
    def get_centre_plant(self) -> Plant:
        """
        Retrieve a plant corresponding to this garden
        that can live in the centre

        Returns
        -------
        Plant
            A centre-loving plant
        """
        pass

    @abc.abstractmethod
    def get_border_plant(self) -> Plant:
        """
        Retrieve a plant corresponding to this garden
        that can live on the border

        Returns
        -------
        Plant
            A border-loving plant
        """
        pass


class VegetableGarden(Garden):
    """
    Factory for a Vegetable Garden
    """

    @override
    def get_shade_plant(self) -> Plant:
        return Plant("Broccoli")

    @override
    def get_centre_plant(self) -> Plant:
        return Plant("Corn")

    @override
    def get_border_plant(self) -> Plant:
        return Plant("Peas")


class AnnualGarden(Garden):
    """
    Factory for an Annual Garden
    """

    @override
    def get_shade_plant(self) -> Plant:
        return Plant("Coleus")

    @override
    def get_centre_plant(self) -> Plant:
        return Plant("Marigold")

    @override
    def get_border_plant(self) -> Plant:
        return Plant("Alyssum")


class PerennialGarden(Garden):
    """
    Factory for a Perennial Garden
    """

    @override
    def get_shade_plant(self) -> Plant:
        return Plant("Astible")

    @override
    def get_centre_plant(self) -> Plant:
        return Plant("Dicentrum")

    @override
    def get_border_plant(self) -> Plant:
        return Plant("Sedum")
