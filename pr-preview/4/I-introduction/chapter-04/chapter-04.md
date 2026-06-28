# Chapter 4: What are Design Patterns?


- [Notes](#notes)
  - [Defining Design Patterns](#defining-design-patterns)
  - [The Learning Process](#the-learning-process)
  - [Notes on Object-Oriented
    Approaches](#notes-on-object-oriented-approaches)
  - [Python Design Patterns](#python-design-patterns)
- [Summary](#summary)

## Notes

- As code is developed and extended it tends to *age* or develop *code
  smells*
  - These occur when is developed beyond what is originally intended to
    do
- At some point, code that has sufficiently deviated from it’s original
  use-case needs to be *refactored*
- The study of the particular design problems and issues that can arise
  that require refactoring is typically captured by the study of *design
  patterns*
  - Design patterns were popularised by the [Gang of
    Four](https://www.amazon.com.au/dp/0201633612?ref_=mr_referred_us_au_au)
    and are effectively templates for solving these common problems
- There is a distinction and similarity between *design patterns* and
  *architectural patterns*
  - Design patterns typically deal with the design of one specific
    component and its interactions
  - Architectural patterns deal with the higher level
    systems-engineering
- One common *architectural pattern* is the *Model-View-Controller*
  (MVC) pattern popularised by the Smalltalk language
  - Divides the problem of structuring an user interface into three
    stages

    1.  *(Data) Model*
        - Computational core of the program
    2.  *View*
        - Presentation of the user interface
    3.  *Controller*
        - Mediates interactions between the view and the model

``` mermaid
---
title: Model-View-Controller Pattern
config:
  htmlLabels: false
---
flowchart LR
    user(("User"))
    model["Model"]
    view["View"]
    control["Controller"]

    model --|Updates|--> view
    view --|Sees|--> user
    user --|Uses|--> control
    controller --|Manipulates|--> model
```

- Each component of the MVC architecture becomes it’s own system to be
  designed
  - Each has rules for how it communicates with the broader system
  - Achieves separation between,
    - Communicating with the user,
    - the GUI,
    - Control over data
- Design and architectural patterns help objects communicate without
  becoming *tightly coupled* to each other’s implementation
  - Good programming, including Object-Oriented programming should aim
    to program to behaviours across a boundary rather than the
    implementation
- [Python Patterns](https://python-patterns.guide/) is a good site
  specifically looking at design patterns in Python

### Defining Design Patterns

- Design patterns help us recognise repeated structures in architecture
  much like in physical domains, for example

  - Sticky buns are like dinner rolls, *but* we add brown sugar and nut
    filling to them
  - Her front garden is like *mine*, *but* I use *abstile*
  - The end table is constructed like that one but has doors instead of
    drawers

- Similarly, code often finds such repeated patterns

  - Identifying and capturing these patterns is one of the goals of
    *design patterns*

- The tl:dr?

  - **Design patterns are frequently used mechanisms that describe
    convenient ways to structure inter-class communication**

- The process of discovering or creating new design patterns is
  sometimes called *pattern mining*

- Design patterns are generally talked about in the context of three
  different types

  1.  *Creational Patterns*
      - Handle creating objects other than via direct instantiation
      - Provide flexibility in how and when objects are created
  2.  *Structural Patterns*
      - Describe how to compose groups of objects into larger objects or
        collections
  3.  *Behavioural Patterns*
      - Define communication between objects
      - Control flow of logic and data in a complex system

### The Learning Process

- Typically learning follows a rough three-step process

  1.  Acceptance
      - Develop an awareness of *design patterns* and the problems they
        solve
  2.  Recognition
      - Recognise design patterns and where they can be applied to solve
        problems in your code
  3.  Internalisation
      - Develop sufficient understanding and experience with patterns to
        be able to instinctively use appropriate patterns when creating
        new systems

### Notes on Object-Oriented Approaches

- Design patterns are designed to provide solutions to common problems
  while preserving the principles of OOP

- These fundamental principles are important to follow even when not
  explicitly using a design pattern

- The basic idea is,

  - *Keep classes separate and not rely extensively on knowing about the
    internals of other classes*
  - A common phrasing for this is that classes should be,
    - *Loosely coupled*
      - Not dependent strongly on another class to function
    - *Highly cohesive*
      - Centralise all the behaviour they are responsible for within the
        class

- A number of common OOP mechanisms are used to achieve these, with two
  prominent ones being

  1.  *Encapsulation*
      - Hiding internals and implementation specifics of a class from
        other classes
      - Harder in Python due to the lack of support for true private
        variables
  2.  *Inheritance*
      - Enables reuse and defining common interfaces through
        sub-classing and polymorphic behaviour
      - Typically the root of an inheritance tree is an abstract class
        - Defines only methods and attributes
        - Not actively instantiated itself
        - Acts as a pattern for concrete subclasses

- Two good principles to follow when designing OOP code regardless of
  design patterns are

  1.  **Design to an interface not and implementation**

      - Define the top of an inheritance hierarchy with an abstract or
        base class
      - Simply defines the methods and attributes common to all
        sub-classes
      - Methods can then be flexibly reimplemented by sub-classes
      - The most basic way to write an abstract class in python is to
        define a method with `pass`
        - `pass` is a placeholder statement that does nothing

        ``` python
         import tkinter as tk

         class DButton(tk.Button):
             def __init__(self, master, **kwargs):
                 super().__init__(master, **kwargs)
                 super().config(command=sel)

             # Abstract method
             def command(self):
                 pass
        ```
      - Python also provides more formal mechanisms for abstract classes
        via the [`abc` built-in
        module](https://docs.python.org/3/library/abc.html)
      - A concrete sub-class of `DButton` defines it’s own `command` to
        override the abstract method

  2.  **Prefer object composition over inheritance**

      - Object composition is the process of creating objects such that
        they contain other objects
      - Results in multiple object instances being encapsulated by the
        larger class
        - Can be more difficult to set up initially than inheritance
          - Mostly due to message-passing boilerplate
        - However, inheritance is a powerful but is a bit of a
          sledgehammer
          - Easy to get stuck in hart to modify code due to an
            overreliance on inheritance making a program hard to change

### Python Design Patterns

- In the remainder of these notes we will summarise the application of
  common design patterns in Python
- Again the emphasis here is on the use of the patterns
  - The code may not necessarily be the *most* Pythonic way of doing
    things
  - Often times procedural, functional or other programming techniques
    outside of OOP can be an alternative way to solve a design problem
    than a pure OOP approach
  - However the goal here is to discuss and demonstrate design patterns

## Summary

- Design patterns are resuable code templates that identify common
  problems with software design and propose potential solutions
- They are distinct from Architectural patterns which examine the
  systems-level structure of a program
- Design patterns do not replace or resolve basic OOP design principles
  and one should still
  1.  Strive to code to an interface over an implementation
  2.  Prefer object composition over inheritance
- When coding in a multi-paradigm language like Python it’s always worth
  considering if a design pattern and OOP is the correct approach or if
  a different paradigm-based approach can solve the problem in a cleaner
  mechanism
