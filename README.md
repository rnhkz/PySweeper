<p align="center">
  <img src="demo.gif" width=600 height=400>
</p>

# PySweeper

[MineSweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) made in Python using the PyGame library.

## Run

* **You must have Python 3 installed.**

PySweeper relies on the external libraries [PyGame](https://www.pygame.org) and [PySimpleGUI](https://www.pysimplegui.org). If you don't already have them, they can be installed by running this command:

```
pip install -r requirements.txt
```

### Using the Command Line:

At the root of the repository, run the following command:
```
python3 src/PySweeper.py
```
This command will create a board with 10 rows, 10 columns and 10 mines, using the default theme.

#### Modifying Game Settings:

You may change various game settings by passing arguments to the run command:
```
python3 src/PySweeper.py 12 10 15 Dark
```
This command will produce a board with 12 rows, 10 columns, and 15 mines, using the "Dark" theme.

### Using the GUI:

Run the following command at the root of the repository:
```
python3 src/Gui.py
```
With this, the rows, columns, mines, and themes can be adjusted using a graphical menu.

## Controls

* Flags can be placed by right-clicking.
* Tiles with no flags can be removed by left-clicking.
* Left clicking while holding down right click will remove all non-flagged tiles surrounding the currently selected tile. The number of surrounding mines must equal the number of surrounding flags for this to work.

* Pressing the 'R' key will reset the game.
* Use the '-' and '+' keys to adjust the window size.
