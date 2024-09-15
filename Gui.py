import os
import PySimpleGUI as sg
import subprocess
import threading

def start_game(rows, columns, mines, theme):
    if (rows=='' or columns=='' or mines=='' or theme==''):
        print("Warning: Invalid value given for one or more inputs! Using default settings.")
        subprocess.run(['python', 'Pysweeper.py'])
        return
    subprocess.run(['python', 'Pysweeper.py', rows, columns, mines, theme])

def main():
    theme_list = next(os.walk('Themes/'))[1]
    sg.theme('DarkAmber')
    layout = [  [sg.Text('Rows'), sg.InputText()],
            [sg.Text('Columns'), sg.InputText()],
            [sg.Text('Mines'), sg.InputText()],
            [sg.Text('Theme'), sg.Combo(theme_list, default_value=theme_list[0], readonly=True)],
            [sg.Button('Ok'), sg.Button('Quit')] ]

    window = sg.Window('PySweeper GUI', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
            break
        x = threading.Thread(target=start_game, args=[values[0], values[1], values[2], values[3]])
        x.start()

    window.close()

if __name__ == "__main__" :
    main()