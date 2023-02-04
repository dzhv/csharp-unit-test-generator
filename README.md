# C# Unit test generator

Time and time again when writing C# applications I noticed the same pattern: I have an existing C# class with dependencies for which I need to write unit tests. To do this the first step was always very robotic and cumbersome: create a new test file with the usual template, mock all of the class under test dependencies and initialize the class. I always felt like this step could be automated.

This repository contains a Python command line tool that automates creating an elementary unit test class, from a given C# class file.

This project is inspired by Visual Studio [Unit Test Boilerplate Generator](https://marketplace.visualstudio.com/items?itemName=RandomEngy.UnitTestBoilerplateGenerator) extension. However, since I am using another IDE, where no equivalent extension exists, the need for a command line tool was born.


## Currently unsupported or will behave strangely with

- Unmockable classes starting with letter "I"
- Multiple class constructors
