# Tkinter Bingo Board Game
## Overview

This script is a simple implementation of a Bingo board game using Python's Tkinter library. It generates a Bingo board from a text file, allows users to interact with the board, and checks for Bingo conditions.
## Requirements

    Python 3.x
    Tkinter (usually comes pre-installed with Python)

## Installation

No additional installation is required if you have Python 3.x installed. Tkinter is part of the standard Python library.
Usage

    Prepare a Bingo Chart File: Create a text file named b_chart.txt with your Bingo values. Each line should contain five values separated by commas, representing a row on the Bingo board.

    Run the Script: Execute the script in Python:

    bash

    python tkinter_bingo.py

    Interact with the Board: Click on cells to mark them. The script checks for Bingo conditions and updates the board accordingly.

## Bingo Chart File Format

The Bingo chart file (b_chart.txt) should be formatted as follows:

    Each line represents a row on the Bingo board.
    Each row should have five values separated by commas.
    Use 'X' to indicate a free space. It will be highlighted on the board.

## Example:

B1,I1,N1,G1,O1

B2,I2,X,G2,O2

B3,I3,N3,G3,O3

B4,I4,N4,G4,O4

B5,I5,N5,G5,O5

## Output Description

The script generates a graphical Bingo board. Users can click on cells to mark them. The script highlights marked cells and updates the board if a Bingo is achieved.
