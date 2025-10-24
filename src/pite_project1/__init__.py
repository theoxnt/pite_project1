"""
pite_project1 package
=====================

Modules :
- core: main logic for filtering and computing
- data_generator: generate data

Shortcut :
- main: shortcut for core.main()

"""

from . import core, io_

__version__ = "1.0.0"
__author__ = "Théo Nouet"
__license__ = "MIT"

#Shortcut 
main = core.main

__all__ = ["core", "io_", "main"]

