# GUI 
import PySimpleGUI as sg
# logging
import logging
# Reading paths
from pathlib import Path

log = logging.getLogger(__name__)

# Defines addPlayers menu
def addPlayers(players):
    ''' Triggers the addPlayers window '''
    player_menu = [[sg.Text("What is the character name?")],
               [sg.InputText(key='--IN--')],
               [sg.Submit(key='addPlayerName', button_text="Submit player name", size=(10,2)), sg.Button("Exit", size=(10,2))],
               [sg.Text(size=(30,1), key='-OUTPUT-')]]
    player_window = sg.Window("Adding player character...", player_menu, grab_anywhere=True)
    while True:
        p_event, p_values = player_window.read()
        if p_event == sg.WIN_CLOSED or p_event == 'Exit':
            log.info("Closing addPlayers")
            break
        if p_event == 'addPlayerName':
            log.info("addPlayerName")
            input_value = p_values['--IN--']
            if input_value != "" and input_value not in players:
                players.append(input_value)
                player_window['-OUTPUT-'].update(input_value)
                log.info(f"Added {input_value}")
                break
            else:
                if input_value == "":
                    log.error("Tried adding blank character name")
                    player_window['-OUTPUT-'].update("Character name cannot be blank!")
                else:
                    log.error("Duplicate character entry")
                    player_window['-OUTPUT-'].update("A character with this name already exists!")
                continue
    player_window.close()
    return players

# Defines listChars menu
def listChars(players):
    ''' Lists all the current chars in a new window '''
    msg = ", ".join(players)
    player_menu = [[sg.Text("Current characters: ")],
                  [sg.Text(msg)],
                  [sg.Button(key="Exit", button_text="Ok", size=(10,2))]]
    player_window = sg.Window("Current characters", player_menu, grab_anywhere=True)
    while True:
        p_event, p_values = player_window.read()
        if p_event == sg.WIN_CLOSED or p_event == 'Exit':
            log.info("Closing listChars")
            break
    player_window.close()
    return players

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

def loadPartyFromFile(players):
    ''' Allows loading/viewing of .txt files defining character names.
        Warning!  This function overwrites the existing players list if a
        file is loaded succesfully '''
    player_menu = [[sg.Input(key='-INPUT-')],
                  [sg.FileBrowse(key='Browse', file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*")), target='-INPUT-')],
                  [sg.Button("Load file", size=(10,2)), sg.Button("View file", size=(10,2)), sg.Button("Exit", size=(10,2))],
                  [sg.Text(size=(50,1), key='-OUTPUT-')]]
    player_window = sg.Window("Load party from file", player_menu, grab_anywhere=True)
    while True:
        p_event, p_values = player_window.read()
        if p_event == sg.WINDOW_CLOSED or p_event == 'Exit':
            log.info("Closing loadPartyFromFile")
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
                        loadMsg = "Loaded characters: "
                        players = []
                        for line in lines:
                            players.append(line.strip())
                        chars = ", ".join(players)
                        loadMsg = loadMsg + chars
                        player_window['-OUTPUT-'].update(loadMsg)
                        log.info(loadMsg)
                except Exception as e:
                    print("Error: ", e)
    player_window.close()
    return players
