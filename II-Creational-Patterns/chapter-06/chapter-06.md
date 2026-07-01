# Chapter 6: The Factory Method Pattern

- [Notes](#notes)
  - [The `Swimmer` Class](#the-swimmer-class)
  - [The `Event` Class](#the-event-class)
- [Summary](#summary)
- [Questions](#questions)

## Notes

- [Chapter 5](../chapter-05/chapter-05.qmd) demonstrates the concept of
  a *simple factory*
- The Factory Concept is a fundamental and common pattern in
  Object-Oriented Design
  - A single class acts as an authority deciding which subclass of a
    hierarchy is instantiated
- The **Factory Method Pattern** extends this concept
  - No single class decides which subclass to instantiate
  - Superclass defers construction to each subclass
- Programs define an abstract class that creates objects
  - Subclasses decide which object to create
- As a simple example, consider swimmers seeded into swim lanes
  - Swimmers competing in multiple heats are first sorted to compete
    from slowest in early heats to fastest in the last heat
    - Within a heat, the fastest swimmers are in the centre lanes
    - This is a process called *straight seeding*
  - In a championship, swimmers often swim an event twice
    - In preliminaries, everyone competes
    - In finals the top 12 of 16 compete against each other
    - To ensure greater equality, top heats are *circle seeded*
      - Fastest three swimmers are in the centre lane in the fastest
        three heats
      - Second fastest are in the lane next to the centre in the top
        three, etc.
- We want to create a program that can automatically perform this
  seeding for us
  - Need to create a class hierarchy to represent events and their
    seeding
  - The basic idea is as follows,
    - An `Event` acts as a factory class for `Seeding` via the
      `get_seeding` method
    - Concrete `Event` subclasses redefine `get_seeding` to control how
      they are seeded
      - In this case to chose which `Seeding` subclass they want to use
    - `Swimmer` is a utility class for keeping track of swimmers
- The UML below shows the rough structure

``` mermaid
---
title: Using the Factory Pattern to create an Event Seeding System
---
classDiagram

    class Event {
        Event: +get_seeding() Seeding
    }

    class TimedFinalEvent

    class PreliminaryEvent

    Event <|-- TimedFinalEvent
    Event <|-- PreliminaryEvent

    class Seeding {
        Seeding: +get_swimmers() List~Swimmer~
    }

    class StraightSeeding

    class CircleSeeding

    Seeding <|-- StraightSeeding
    Seeding <|-- CircleSeeding

    Event --> Seeding : get_seeding()
    TimedFinalEvent ..> StraightSeeding : Creates
    PreliminaryEvent ..> CircleSeeding : Creates

    class Swimmer {
        Swimmer: +String first_name
        Swimmer: +String last_name
        Swimmer: +int age
        Swimmer: +String club
        Swimmer: +String seed_time

        Swimmer: +get_name() String
    }

    Seeding --> Swimmer : get_swimmers()
```

### The `Swimmer` Class

- The `Swimmer` class is a basic class designed to store information
  about a Swimmer
  - Namely,
    1. Name
    2. Age
    3. Club
    4. Seed time
    5. Seeded lane
    6. Heat
- We’ll use a common Python pattern for handling object creation which
  is to define a generic `__init__` that accepts the required parameters
  - We then define *class methods* to handle the various ways that one
    might want to provide that data
    - For example, from a text file
    - Means we can extend to accept new formats like a database row by
      adding a new class method as opposed to re-tooling our `__init__`
    - This reduces coupling between the data storage format and the
      object creation mechanism

### The `Event` Class

- The `Event` class acts as our abstract base class for defining *what*
  seeding objects should be created
-

## Summary

## Questions
