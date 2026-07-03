"""
Swim Events
-----------

A basic library demonstrating the Factory Method Pattern via implementing a
seeding system for swimming events

Classes
-------

* Swimmer  -- A swimmer competing in events
* Event -- Abstract class representing swimming events

    * PreliminaryEvent -- Represents a Preliminary Event in a Swimming Competition
    * TimedFinalEvent -- Represents a Timed Final in a Swimming Competition

* Seeding -- Abstract class representing a Seeding Method for Swimming Events

    * StraightSeeding -- Implementation of the Straight Seeding Method

        * CircleSeeding -- Implementation of the Circle Seeding Method
"""

import abc
import datetime
import itertools
from typing import Sequence, override


def parse_time(timecode: str) -> datetime.time:
    """Parse a seed timecode to a time

    Parameters
    ----------
    timecode : str
        seed time represented in either `%M:%S.%f` or `%S.%f` ISO format

    Returns
    -------
    `datetime.time`
        time corresponding to the provided time code

    Raises
    ------
    ValueError
        Raised if `timecode` is not in a supported format
    """
    try:
        time = datetime.time.strptime(timecode, "%M:%S.%f")
    except ValueError:
        time = datetime.time.strptime(timecode, "%S.%f")
    return time


class Swimmer:
    """Represents a Swimmer competing in an Event

    Attributes
    ----------
    first_name: str
        swimmer's first name
    last_name: str
        swimmer's last name
    age : int
        swimmer's current age in years
    club : str
        club the swimmer is representing
    seed_time : datetime.time
        swimmer's seed time
    heat: int
        swimmer's allocated heat, 0 represents an unallocated swimmer
    lane: int
        swimmer's allocated lane, 0 represents an unallocated swimmer
    """

    @classmethod
    def from_string(cls, swimmer: str, delimiter=" ") -> Swimmer:
        """Create a swimmer from a delimited string

        Converts a delimited string into a `Swimmer`, the string is split into
        arguments to the `Swimmer` constructor by the delimiter, and must follow
        the structure below, where ``[x]`` represents a delimited chunk
        corresponding to the parameter `x`

        ``[first_name][last_name][age][club][seed_time]``

        The parameters must be represented in the following formats,

        * `first_name` - `str`
        * `last_name` - `str`
        * `age` - `int`
        * `club` - `str`
        * `seed_time` - either `%M:%S.%f` or `%S.%f`

        Parameters
        ----------
        swimmer : str
            swimmer represented as parameter delimited by the delimiter

        delimiter : str, optional
            The delimiting symbol uses to split the string, by default " "

        Returns
        -------
        Swimmer
            swimmer described by the provided string

        Raises
        ------
        ValueError
            Could not convert the provided string to a `Swimmer` instance
        """

        swimmer_parameters = [
            parameter for parameter in swimmer.split(sep=delimiter) if parameter
        ]

        if len(swimmer_parameters) != 5:
            raise ValueError(
                f"Swimmer requires 5 parameters, got {len(swimmer_parameters)}\n{swimmer_parameters}"
            )

        swimmer_parameters = [parameter.strip() for parameter in swimmer_parameters]

        first_name = swimmer_parameters[0]
        last_name = swimmer_parameters[1]
        age = int(swimmer_parameters[2])
        club = swimmer_parameters[3]

        seed_time = parse_time(swimmer_parameters[4])

        return cls(first_name, last_name, age, club, seed_time)

    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        club: str,
        seed_time: datetime.time,
    ):
        """
        Create a new instance based on the provided details

        Parameters
        ----------

        first_name: str
            swimmer's first name
        last_name: str
            swimmer's last name
        age : int
            swimmer's current age in years
        club : str
            club the swimmer is representing
        seed_time : datetime.time
            swimmer's seed time
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.club = club
        self.seed_time = seed_time
        self.heat = 0
        self.lane = 0

    @property
    def name(self) -> str:
        """
        The Swimmer's full name
        """
        return self.first_name + " " + self.last_name


class Event(abc.ABC):
    """
    Abstract Class representing a generic swimming event

    Subclasses should override the `seeding` factory method to create the
    appropriate seeding instance for the event type

    Attributes
    ----------
    swimmers: Sequence[Swimmer]
        swimmers competing in the event
    number_of_lanes: int
        number of lanes in each heat
    """

    def __init__(self, swimmers: Sequence[Swimmer], lanes: int):
        """
        Create a new event instance with the provided swimmers and the
        given number of lanes per heat

        Parameters
        ----------
        swimmers: Sequence[Swimmer]
            Swimmers competing in the event
        lanes: int
            Number of lanes per heat
        """
        self.number_of_lanes = lanes
        self.swimmers = swimmers

    @abc.abstractmethod
    def seeding(self) -> Seeding:
        """
        Create the seeding for the event

        Returns
        -------
        Seeding
            The seeding methodology to be used for the event
        """
        pass


class PreliminaryEvent(Event):
    """
    A Preliminary Swimming Competition Event
    """

    @override
    def seeding(self) -> Seeding:
        return CircleSeeding(self.swimmers, self.number_of_lanes)


class TimedFinalEvent(Event):
    """
    A Timed Swimming Competition Event
    """

    @override
    def seeding(self) -> Seeding:
        return StraightSeeding(self.swimmers, self.number_of_lanes)


class Seeding(abc.ABC):
    """
    Abstract Class representing a methodology for seeding an event

    Distributes a roster of swimmer's across heats and lanes according to
    the desired seeding method. Seeding is performed on object creation and
    does not require an explicit call to `seed`


    Subclasses should override the `seed` method to implement the desired
    seeding methodology

    Attributes
    ----------
    swimmers: Sequence[Swimmer]
        swimmers to be seeded, sorted by increasing seed time
    number_of_lanes: int
        number of lanes in each heat
    number_of_heats: int
        number of heats in the event
    """

    def __init__(self, swimmers: Sequence[Swimmer], number_of_lanes: int):
        self.swimmers = sorted(swimmers, key=lambda x: x.seed_time)
        self.number_of_lanes = number_of_lanes
        self.number_of_heats = 0

        self.seed()

    @abc.abstractmethod
    def seed(self) -> None:
        """
        Seed swimmers into a designated heat and lane

        Each swimmer in `self.swimmers` must have their `heat` and `lane`
        attribute assigned after `seed` is called. A `(heat, lane)` pair
        must be unique
        """
        pass


class StraightSeeding(Seeding):
    """
    Straight seeds an event

    Heats are seeded slowest to fastest, with the fastest swimmers
    in the center lanes
    """

    @override
    def seed(self) -> None:
        """
        Seed swimmers into a designated heat and lane

        Heats are seeded slowest to fastest, with the fastest swimmers
        in the center lanes
        """
        print("Straight seeding...")
        # calculate number of swimmers in the last heat, we want it to be a minimum of three
        # unless there are only two competitors
        n_swimmers_in_last_heat = len(self.swimmers) % self.number_of_lanes
        if n_swimmers_in_last_heat < 3:
            n_swimmers_in_last_heat = min(3, len(self.swimmers))

        # calculate number of lanes in the normal heat
        # and the total number of heats
        remaining_lanes = len(self.swimmers) - n_swimmers_in_last_heat
        self.number_of_heats = len(self.swimmers) // self.number_of_lanes + (
            1 if remaining_lanes else 0
        )

        # generate the lane orderings and set to repeat for as we cycle over the heats
        lane_ordering = itertools.cycle(self.generate_lane_order())

        # cycle over the heats performing the seeding
        for idx, (lane, swimmer) in enumerate(
            zip(lane_ordering, self.swimmers[:remaining_lanes])
        ):
            print(f"Seeding {swimmer.name} ({idx}, {lane})")
            swimmer.lane = lane
            swimmer.heat = self.number_of_heats - (idx // self.number_of_lanes)

        # if no left over heat, return now
        if not n_swimmers_in_last_heat:
            return

        print("Seeding final heat")
        # otherwise seed the final heat
        for lane, swimmer in zip(
            self.generate_lane_order(), self.swimmers[-n_swimmers_in_last_heat:]
        ):
            swimmer.lane = lane
            swimmer.heat = 1

    def generate_lane_order(self) -> Sequence[int]:
        """
        The order to assign lanes within a heat

        Returns
        -------
        Sequence[int]
            The order in which lanes are seeded.
            Lanes start at 1.
        """

        mid = self.number_of_lanes // 2 + self.number_of_lanes % 2

        incr = 1
        lane = mid
        lanes = []
        for i in range(self.number_of_lanes):
            lanes.append(lane)
            lane = mid + incr
            incr = -incr + (1 if incr < 0 else 0)

        print(f"Ordering: {lanes}")
        return lanes


class CircleSeeding(StraightSeeding):
    """
    Circle seeds an event

    As for straight seeding but the fastest swimmers are distributed to the
    top three heats as in the diagram below

    ``(7, 1, 4), (8, 2, 5), (9, 3, 6)``
    """

    @override
    def seed(self) -> None:
        """
        Seed swimmers into a designated heat and lane

        Heats are seeded slowest to fastest, with the fastest swimmers
        in the center lanes. The fastest swimmers are distributed across the
        top 3 heats.

        ``(7, 1, 4), (8, 2, 5), (9, 3, 6)``
        """

        print("Circle seeding\nInitial Straight seeding")
        # start by straight-seeding
        super().seed()
        if self.number_of_heats <= 1:
            return

        # Calculate, number of heats to be circle seeded, if only one heat
        # return early
        number_to_circle_seed = min(3, self.number_of_heats)

        # Reseed the final `number_to_circle_seed`
        lane_ordering = itertools.cycle(self.generate_lane_order())

        for swimmer, (lane, heat) in zip(
            self.swimmers[: self.number_of_lanes * number_to_circle_seed],
            itertools.product(
                itertools.islice(
                    lane_ordering, number_to_circle_seed * self.number_of_lanes
                ),
                range(number_to_circle_seed),
            ),
        ):
            print(f"Seeding {swimmer.lane} ({lane}{heat})")
            swimmer.lane = lane
            swimmer.heat = self.number_of_heats - heat


def load_swimmers(filename: str, delimiter=" ") -> list[Swimmer]:
    """
    Load swimmers from a delimited file

    Load's swimmer's from a delimited file into a list of `swim_events.Swimmer`
    instances. Does not populate their heat and lane.

    Assumes the file follow's the interface of `swim_events.Swimmer.from_string`

    Parameters
    ----------
    filename : str
        path to the file containing swimmers, can be absolute or relative

    Returns
    -------
    list[Swimmer]
        list of Swimmer objects corresponding to rows in the file
    """
    # extract swimmers from file, slicing off the initial "idx " substring
    with open(filename, "r") as f:
        swimmers = [
            Swimmer.from_string(line.partition(" ")[2], delimiter=delimiter)
            for line in f.readlines()
        ]
    return swimmers
