Code Examples and descriptions for using the E3.series python library
====================================================================
You can find the e3series python library itself here: https://pypi.org/project/e3series/
It can be installed using "pip install e3series" (For further instructions take a look at the chapter "Basics" and "Environment  Setup")

# Code examples

## EnvironmentSetup

- Description on how to install the neccessary tools, extensions and packages.
- Basic usage of the tools

## Basics

Jupyter notebook describing the basic knowledge regarding the library.

- Installation of latest version or specific versions

- Using the library
  -  starting E3.series safely
  -  starting E3.dbe
  -  working with COM objects
  -  using enums provided in e3series.types
 
## Connection List

  - Prints a list of all connections in the open project to the E3.series messages window
    - From/To Device and pin
    - Jumpable link to the connection

## PartsWithPandas

  - Writing a partlist to a xlsx-file using pandas and opnpyxl
    - Once as a jupyter notebook for seperated execution and in file visualization
    - Once as py-file to add it to the tools-menu as described within the file

## PrintToE3

  - Redirect all print commands to E3.series

## Simple BOM

  - Uses a dictionary to order all parts by component name and print a sorted BOM

## ToolsMenu

  - Simple "Hello World" project with introductions how to add it to the tools menu