<p align="center">
  <img src="demo.gif" width=600 height=400>
</p>

# PySweeper

[MineSweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) made in Python using the PyGame library.

## Installation

**You must have Python 3 installed before proceeding.**

PySweeper relies on the external libraries [PyGame](https://www.pygame.org) and [PySimpleGUI](https://www.pysimplegui.org). If you don't already have them, they can be installed by running this command:

```
pip install -r requirements.txt
```

## Usage

PySweeper can be executed using a few different options.

### Using the Command Line

At the root of the repository, run the following command:

```
python PySweeper.py
```

This will create a window with 10 rows, 10 columns and 10 mines, using the default theme.
You may also change various game settings by passing arguments to the run command.

```
python PySweeper.py 12 10 15 Dark
```

This will create a window with 12 rows, 10 columns, and 15 mines, using the "Dark" theme.

### Using the GUI

The various game settings can be adjusted using a graphical menu by using the following command at root:

```
python Gui.py
```

## Controls

- Flags can be placed by right-clicking.
- Tiles with no flags can be removed by left-clicking.
- Left clicking while holding down right click will remove all non-flagged tiles surrounding the currently selected tile. The number of surrounding mines must equal the number of surrounding flags for this to work.
- Pressing the 'R' key will reset the game.
- Use the '-' and '+' keys to adjust the window size.
