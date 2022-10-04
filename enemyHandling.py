# GUI
import PySimpleGUI as sg
# logging
import logging
# Reading paths
from pathlib import Path

log = logging.getLogger(__name__)

# Defines addEnemies menu
def addEnemies(enemies):
    ''' Triggers the addEnemies window '''
    player_menu = [[sg.Text("What is the enemy name?")],
               [sg.InputText(key='--IN--')],
               [sg.Submit(key='addEnemyName', button_text="Submit enemy name", size=(10,2)), sg.Button("Exit", size=(10,2))],
               [sg.Text(size=(30,1), key='-OUTPUT-')]]
    player_window = sg.Window("Adding enemy character...", player_menu, grab_anywhere=True)
    while True:
        p_event, p_values = player_window.read()
        if p_event == sg.WIN_CLOSED or p_event == 'Exit':
            log.info("Closing addEnemies")
            break
        if p_event == 'addEnemyName':
            log.info("addEnemyName")
            input_value = p_values['--IN--']
            if input_value != "" and input_value not in enemies:
                enemies.append(input_value)
                player_window['-OUTPUT-'].update(input_value)
                log.info(f"Added {input_value}")
                break
            else:
                if input_value == "":
                    log.error("Tried adding blank enemy name")
                    player_window['-OUTPUT-'].update("Enemy name cannot be blank!")
                else:
                    log.error("Duplicate enemy entry")
                    player_window['-OUTPUT-'].update("An enemy with this name already exists!")
                continue
    player_window.close()
    return enemies

# Defines listEnemies menu
def listEnemies(enemies):
    ''' Lists all the current enemies in a new window '''
    msg = ", ".join(enemies)
    player_menu = [[sg.Text("Current enemies: ")],
                  [sg.Text(msg)],
                  [sg.Button(key="Exit", button_text="Ok", size=(10,2))]]
    player_window = sg.Window("Current enemies", player_menu, grab_anywhere=True)
    while True:
        p_event, p_values = player_window.read()
        if p_event == sg.WIN_CLOSED or p_event == 'Exit':
            log.info("Closing listEnemies")
            break
    player_window.close()
    return enemies

def openFile(filename, text):
    ''' Used to open a multiline window displaying the content of a file; used in loading-methods'''
    menu = [[sg.Multiline(text, size=(80, 25))],
            [sg.Button("Exit", size=(10,2))]]
    window = sg.Window(filename, menu, modal=True, finalize=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            log.info("Closing openFile")
            break
    window.close()


def loadEnemiesFromFile(enemies):
    ''' Allows loading/viewing of .txt files defining enemies.
        Warning! This function overwrites the existing enemies list if a
        file is loaded succesfully '''
    player_menu = [[sg.Input(key='-INPUT-')],
                  [sg.FileBrowse(key='Browse', file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*")), target='-INPUT-')],
                  [sg.Button("Load file", size=(10,2)), sg.Button("View file", size=(10,2)), sg.Button("Exit", size=(10,2))],
                  [sg.Text(size=(50,1), key='-OUTPUT-')]]
    player_window = sg.Window("Load enemies from file", player_menu, grab_anywhere=True)
    while True:
        p_event, p_values = player_window.read()
        if p_event == sg.WINDOW_CLOSED or p_event == 'Exit':
            log.info("Closing loadEnemiesFromFile")
            break
        elif p_event == 'View file':
            filename = p_values['-INPUT-']
            if Path(filename).is_file():
                try:
                    with open(filename, "rt", encoding='utf-8') as f:
                        text = f.read()
                    log.info(f"Viewing file {p_values['-INPUT-']}")
                    openFile(filename, text)
                except Exception as e:
                    print("Error: ", e)
        elif p_event == 'Load file':
            filename = p_values['-INPUT-']
            if Path(filename).is_file():
                try:
                    with open(filename, "rt", encoding='utf-8') as f:
                        log.info(f"Loading file {p_values['-INPUT-']}")
                        lines = [line.rstrip('\n') for line in f]
                        loadMsg = "Loaded enemies: "
                        enemies = []
                        for line in lines:
                            enemies.append(line.strip())
                        mobs = ", ".join(enemies)
                        loadMsg = loadMsg + mobs
                        player_window['-OUTPUT-'].update(loadMsg)
                        log.info(loadMsg)
                except Exception as e:
                    print("Error: ", e)
    player_window.close()
    return enemies