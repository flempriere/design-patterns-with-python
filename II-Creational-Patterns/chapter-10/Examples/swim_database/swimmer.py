"""
Swimmer
-------

A basic library containing a swimmer class derived from the
implementation in Chapter 6

Classes
-------

* `Swimmer` -- A swimmer competing in events
"""

import datetime
from typing import Literal

type Sex = Literal["M"] | Literal["F"] | Literal["U"]


def parse_time(timecode: str) -> datetime.time:
    """
    Parse a seed timecode to a time

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


def parse_name(name: str) -> tuple[str, str]:
    """
    Parse a name into first and last name components

    Assumes the name is formatted as `"first last"`

    Parameters
    ----------
    name : str
        Name to be parsed

    Returns
    -------
    tuple[str, str]
        first, and last name components
    """
    first_name, _, last_name = name.partition(" ")
    first_name = first_name.strip()
    last_name = last_name.strip()

    return first_name, last_name


def parse_sex(raw_sex: str) -> Sex:
    """
    Parse a string into a Sex

    Parameters
    ----------
    raw_sex : str
        string representing the string to be parsed

    Returns
    -------
    Sex
        The provided sex

    Raises
    ------
    ValueError
        raised if `sex` could not be converted to a `Sex`
    """
    raw_sex = raw_sex.upper()
    if raw_sex not in ["M", "F", "U"]:
        raise ValueError(
            "invalid sex encountered {sex}, accepted values are 'M', 'F', 'U' and lowercase equivalent"
        )
    else:
        sex: Sex = raw_sex  # ty:ignore[invalid-assignment] previous check ensures, value is M, F or U
        return sex


class Swimmer:
    """
    Represents a Swimmer competing in an Event

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
    sex : Sex
        swimmer's sex, Male (M), Female (F) or Unspecified (U)
    """

    @classmethod
    def from_string(cls, swimmer: str, delimiter=" ") -> Swimmer:
        """
        Create a swimmer from a delimited string

        Converts a delimited string into a `Swimmer`, the string is split into
        arguments to the `Swimmer` constructor by the delimiter, and must follow
        the structure below, where ``[x]`` represents a delimited chunk
        corresponding to the parameter `x`

        ``[first_name last_name][age][club][seed_time][sex]``

        The parameters must be represented in the following formats,

        * `first_name` - `str`
        * `last_name` - `str`
        * `age` - `int`
        * `club` - `str`
        * `seed_time` - either `%M:%S.%f` or `%S.%f`
        * `sex` - `M`, `m`, `F`, `f`, `U` or `u`

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

        first_name, last_name = parse_name(swimmer_parameters[0])
        age = int(swimmer_parameters[1])
        club = swimmer_parameters[2]
        seed_time: datetime.time = parse_time(swimmer_parameters[3])
        sex = parse_sex(swimmer_parameters[4])

        return cls(first_name, last_name, age, club, seed_time, sex)

    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        club: str,
        seed_time: datetime.time,
        sex: Sex,
    ) -> None:
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
        sex : Sex
            swimmer's sex
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.club = club
        self.seed_time = seed_time
        self.sex = sex

    def __str__(self) -> str:
        """
        Create a space-delimited string representation of the swimmer

        The string is delimited as,
        [first name][last name][age][club][seed time][sex]

        Returns
        -------
        str
            the space-delimited string
        """
        if self.seed_time.minute:
            formatted_time = self.seed_time.strftime("%M:%S.%f")[:-3]
        else:
            formatted_time = self.seed_time.strftime("%S.%f")[:-3]

        return f"{self.name} {self.age} {self.club} {formatted_time} {self.sex}"

    @property
    def name(self) -> str:
        """
        The Swimmer's full name
        """
        return self.first_name + " " + self.last_name


def load_swimmers(filename: str, delimiter=",") -> list[Swimmer]:
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
            Swimmer.from_string(line, delimiter=delimiter) for line in f.readlines()
        ]
    return swimmers
