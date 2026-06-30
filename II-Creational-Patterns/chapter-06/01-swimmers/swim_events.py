import abc
import datetime
from typing import Sequence


class Swimmer:
    @classmethod
    def from_csv_row(cls, csv_row: str, delim=" "):

        swimmer_parameters = csv_row.split(sep=delim)

        if len(swimmer_parameters) != 5:
            raise ValueError("Swimmer requires 5 parameters")

        swimmer_parameters = [parameter.strip() for parameter in swimmer_parameters]

        first_name = swimmer_parameters[0]
        last_name = swimmer_parameters[1]
        age = int(swimmer_parameters[2])
        club = swimmer_parameters[3]

        def parse_time(time_str: str):
            if time_str.find(":") > 0:
                minutes_str, seconds_and_milliseconds_str = time_str.split(":")
                minutes = int(minutes_str)
            else:
                minutes = 0
                seconds_and_milliseconds_str = time_str
                seconds_str, milliseconds_str = seconds_and_milliseconds_str.split(".")

            seconds = int(seconds_str)
            microseconds = int(float(milliseconds_str) * 1e6)
            time = datetime.time(
                minute=minutes, second=seconds, microsecond=microseconds
            )
            return time

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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.club = club
        self.seed_time = seed_time

    @property
    def name(self):
        return self.first_name + " " + self.last_name


class Event(abc.ABC):
    def __init__(self, swimmers: Sequence[Swimmer], lanes: int):
        self.number_of_lanes = lanes
        self.swimmers = swimmers

    @abc.abstractmethod
    def seeding(self) -> Seeding:
        pass


class TimedFinalEvent(Event):
    def seeding(self):
        return StraightSeeding(self.swimmers, self.number_of_lanes)


class PreliminaryEvent(Event):
    def seeding(self):
        return CircleSeeding(self.swimmers, self.number_of_lanes)


class Seeding(abc.ABC):
    def __init__(self, swimmers: Sequence[Swimmer], number_of_lanes: int):
        self.swimmers = swimmers
        self.number_of_lanes = number_of_lanes

        self.seed()

    def seed(self):
        pass


class StraightSeeding(Seeding):
    def seed(self):
        pass


class CircleSeeding(StraightSeeding):
    def seed(self):
        pass
