import PySimpleGUI as sg
import subprocess
import threading

def start_game(rows, columns, mines):
    subprocess.run(['python3', 'Pysweeper.py', rows, columns, mines])

def main():
    sg.theme('DarkAmber')
    layout = [  [sg.Text('Rows'), sg.InputText()],
            [sg.Text('Columns'), sg.InputText()],
            [sg.Text('Mines'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Quit')] ]

    window = sg.Window('PySweeper GUI', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
            break
        x = threading.Thread(target=start_game, args=[values[0], values[1], values[2]])
        x.start()

    window.close()

if __name__ == "__main__" :
    main()