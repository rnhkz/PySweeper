<img src="demo.gif" alt="PySweeper Demo">

# PySweeper

MineSweeper made in Python using the PyGame library.

## Run

* Prerequisite: You must have Python 3 installed.

PySweeper relies on the external libraries PyGame and PySimpleGUI. If you don't already have them, they can be installed by running this command:
```
pip install -r requirements.txt
```

### Using the Command Line:

At the root of the repository, run the following command:
```
python3 src/PySweeper.py
```
This command will create a board with 10 rows, 10 columns and 10 mines, using the default theme.

### Modifying Game Settings

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

Game can be reset by pressing the 'R' key.
* Flags can be placed by right-clicking.
* Tiles with no flags can be removed by left-clicking.
* Left clicking while holding down right click will remove all non-flagged tiles surrounding the currently selected tile. The number of surrounding mines must equal the number of surrounding flags for this to work.
