# PySweeper

MineSweeper made in Python using PyGame.

## Run

Prerequisite: PyGame is installed. You may get it from the official website.

### Using command-line interface:

Run the following command at the root of the repository:
```
python3 PySweeper.py
```
This command will create a board with 10 rows, 10 columns and 10 mines.

### Using GUI:

Run the following command at the root of the repository:
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

### Themes

Themes allow for the cosmetics of the game to be changed. 

Example:
```
python3 PySweeper.py 12 10 15 Dark
```
This command will produce a board with 12 rows and 10 columns with 15 mines using the "Dark" theme.

Themes may also be selected from the GUI.

## Controls

Game can be reset by pressing the 'R' key.
* Flags can be placed by right-clicking.
* Tiles with no flags can be removed by left-clicking.
* Left clicking while holding down right click will remove all non-flagged tiles surrounding the currently selected tile. The number of surrounding mines must equal the number of surrounding flags for this to work.

## Libraries used

* Pygame
* PySimpleGui
