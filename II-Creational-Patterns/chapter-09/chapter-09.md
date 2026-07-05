# Chapter 9: The Builder Pattern

- [Notes](#notes)
  - [An Investment Tracker](#an-investment-tracker)
- [Summary](#summary)
- [Questions](#questions)

## Notes

- The factory patterns previously discussed ([Chapter
  5](../chapter-05/chapter-05.qmd), [Chapter
  6](../chapter-06/chapter-06.qmd), [Chapter
  7](../chapter-07/chapter-07.qmd)) deal with instantiating different
  subclass variants of a class hierarchy
- A related but similar problem is how to handle if we want to customise
  an instance of the one class
- For example, consider an address book
  - An address might be a,

    1. A Person, comprising

        - First name
        - Last name
        - Company
        - Email
        - Phone Number

    2. Group, comprising

        - Name
        - Purpose
        - Members
          - Their email addresses

  - We want a different display to be constructed for each address type

    - Not a factory here because each object has to be configured
      differently rather than just overriding methods

### An Investment Tracker

- We’ll work with a simpler example of an investment tracker program

- Tracks,

  1. Stocks
  2. Bonds
  3. Mutual Funds

- We want to be able to display each category

- Then select a sub-selection of investments in that category

  - Plot their comparative performance

- We need our display to handle a variable number of plots

  - For a large number of choices we use a listbox with multiple
    selections
  - For three or less we use a series of checkbox values

- We need a builder class that can choose how to configure the UI

## Summary

## Questions
