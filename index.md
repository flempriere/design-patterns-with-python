# Python Programming with Design Patterns: Notes


- [Contents](#contents)
  - [I: Introduction](#i-introduction)
  - [II: Creational Patterns](#ii-creational-patterns)
  - [III: Structural Patterns](#iii-structural-patterns)
  - [IV: Behavioural Patterns](#iv-behavioural-patterns)
- [Attribution](#attribution)
- [Code Style](#code-style)

[![pre-commit.ci
status](https://results.pre-commit.ci/badge/github/flempriere/design-patterns-with-python/main.svg)](https://results.pre-commit.ci/latest/github/flempriere/design-patterns-with-python/main)
[![pages-build-deployment](https://github.com/flempriere/design-patterns-with-python/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/flempriere/design-patterns-with-python/actions/workflows/pages/pages-build-deployment)

This repository contains notes and code examples from the book, [Python
Programming with Design
Patterns](https://www.amazon.com.au/Python-Programming-Design-Patterns-Cooper/dp/0137579934)

## Contents

### I: Introduction

- [Chapter 1: Introduction to
  Objects](I-introduction/chapter-01/chapter-01.qmd)
- [Chapter 2: Visual Programming in
  Python](I-introduction/chapter-02/chapter-02.qmd)
- [Chapter 3: Visual Programming of Tables of
  Data](I-introduction/chapter-03/chapter-03.qmd)
- [Chapter 4: What are Design
  Patterns?](I-introduction/chapter-04/chapter-04.qmd)

### [II: Creational Patterns](II-Creational-Patterns/ii-creational-patterns.qmd)

- [Chapter 5: The Factory
  Pattern](II-Creational-Patterns/chapter-05/chapter-05.qmd)
- [Chapter 6: The Factory Method
  Pattern](II-Creational-Patterns/chapter-06/chapter-06.qmd)
- [Chapter 7: The Abstract Factory
  Pattern](II-Creational-Patterns/chapter-07/chapter-07.qmd)
- [Chapter 8: The Singleton
  Pattern](II-Creational-Patterns/chapter-08/chapter-08.qmd)
- [Chapter 9: The Builder
  Pattern](II-Creational-Patterns/chapter-09/chapter-09.qmd)
- [Chapter 10: The Prototype
  Pattern](II-Creational-Patterns/chapter-10/chapter-10.qmd)

### III: Structural Patterns

### IV: Behavioural Patterns

> [!NOTE]
>
> This repository will not cover Section V which deals with introducing
> the Python Language.

## Attribution

The notes and code in this repository are based on the work of the
original author. You can find their original supplied code at the
attached submodule, or at the following [github
repository](https://github.com/jwcnmr/jameswcooper). The original code
is also supplied as a submodule.

## Code Style

I’m personally not a fan of the way the original code examples have been
written. There is a lack of consistency in name conventions and the code
is (in my opinion) written in a way that is very rigid and not very
pythonic. In general the the code has been rewritten to follow PEP 8
conventions and make for greater clarity. For example, the use of
*closures* to write callback’s for GUI triggers over proliferating
object methods, and giving objects generic constructors for their
parameters and using free functions or class methods to handle
construction from sources like files and strings.
