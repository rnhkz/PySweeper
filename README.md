# PySweeper

MineSweeper made in Python using PyGame.

## Run

Prerequisite: PyGame is installed. You may get it from the official website.

### Using command-line interface:

Run the followinf command at the root of the repository:
```
python3 PySweeper.py
```
This command will create a board with 10 rows, 10 columns and 10 mines.

### Using GUI:

Run the followinf command at the root of the repository:
```
python3 Gui.py
```
This will display a window that allows rows, columns, and mines to be set.

## Modifying Game Settings

The dimensions and mine count can be set using arguments.

Example:
```
python3 PySweeper.py 12 10 15
```
This command will produce a board with 12 rows and 10 columns with 15 mines.

## Additional Features

Game can be reset by pressing the 'R' key.

## Libraries used

* Pygame
* PySimpleGui