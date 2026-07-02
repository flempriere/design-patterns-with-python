from typing import Sequence

import swim_events


def load_swimmers(filename: str, delimiter=" ") -> list[swim_events.Swimmer]:
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
    list[swim_events.Swimmer]
        list of Swimmer objects corresponding to rows in the file
    """
    # extract swimmers from file, slicing off the initial "idx " substring
    with open(filename, "r") as f:
        swimmers = [
            swim_events.Swimmer.from_string(line.partition(" ")[2], delimiter=delimiter)
            for line in f.readlines()
        ]
    return swimmers


def select_event(event_id: int) -> Sequence[swim_events.Swimmer]:
    """
    Select and seed a corresponding event

    Parameters
    ----------
    event_id : int
        integer id corresponding to a specific event

    Returns
    -------
    Sequence[swim_events.Swimmer]
        Swimmers competing in the event seeded into heats and lanes, sorted
        in ascending seed time

    Raises
    ------
    ValueError
        Raised if `event_id` does not correspond to an event
    """
    if event_id == 1:
        print("loading swimmers")
        swimmers = load_swimmers("100free.txt")
        print("swimmers loaded\nGenerating event")
        event = swim_events.PreliminaryEvent(swimmers, 6)
        print("Event retrieved")
    elif event_id == 5:
        swimmers = load_swimmers("500free.txt")
        event = swim_events.TimedFinalEvent(swimmers, 6)
    else:
        raise ValueError(f"No event found corresponding to {event_id}")

    print("Seeding")
    seeding = event.seeding()
    swimmers = seeding.swimmers  # get's the sorted swimmers list
    print("Finished seeding")
    return swimmers


class SwimEventConsoleUI:
    def build(self):
        while distance := int(input("Select Event (1 - 100 m, 5 - 500 m, 0 - quit): ")):
            try:
                swimmers = select_event(distance)
            except ValueError as e:
                print(e)
            else:
                for swimmer in swimmers:
                    print(
                        f"{swimmer.heat:3}{swimmer.lane:3} {swimmer.name:20}{swimmer.age:3}{swimmer.seed_time:9}"
                    )


def main():
    console = SwimEventConsoleUI()
    console.build()


if __name__ == "__main__":
    main()
