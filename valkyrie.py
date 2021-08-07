# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# logging
import logging
# check platform
import platform
# pretty iters
from tqdm import tqdm
# sys flow
import sys
# Loading env
from dotenv import load_dotenv
# Reading env
import os
# Reading paths
from pathlib import Path
# Interactive debug
from IPython import embed

#Check platform; rich not handled on raspi
if platform.uname().node != 'raspberrypi':
	from rich.logging import RichHandler
	logging.basicConfig(
    		level="INFO",
    		format="%(message)s",
    		datefmt="[%X]",
    		handlers=[RichHandler()]
		)
else:
	logging.basicConfig(
		level="INFO",
		format="%(message)s",
		datefmt="[%X]",
		handlers=[logging.StreamHandler()]
		)

log = logging.getLogger("Valkyrie")
log.setLevel(logging.INFO)
log.info("Logger initialized")

# Get .env
# load_dotenv()

#Importing package
import PySimpleGUI as sg

# Define the base window's contents
top_menu = [ [sg.Text("Valkyrie has awakened! What happens below?")],
            [sg.Button(key='addPlayers', button_text='Add player character', size=(20,5)),
             sg.Button(key='listChars', button_text='List characters', size=(20,5)),
             sg.Button(key='loadPartyFromFile', button_text='Load party from file', size=(20,5))],
            [sg.Button(key='addEnemies', button_text='Add enemies', size=(20,5)),
			sg.Button(key='listEnemies', button_text='List enemies', size=(20,5)),
            sg.Button(key='loadEnemiesFromFile', button_text="Load enemies from file", size=(20,5))
            ],
            [sg.Button(key='startBattle', button_text='Start Battle', size=(32,5)),
            sg.Button("Exit", size=(32,5))]
         ]
# Create the base window
main_window = sg.Window("Valhalla responds!", top_menu, grab_anywhere=True)

# Defines addPlayers menu 
def addPlayers(players):
    player_menu = [[sg.Text("What is the character name?")],
               [sg.InputText(key='--IN--')],
               [sg.Submit(key='addPlayerName', button_text="Submit player name", size=(10,2)), sg.Button("Exit", size=(10,2))],
               [sg.Text(size=(15,1), key='-OUTPUT-')]]
    player_window = sg.Window("Adding player character...", player_menu, grab_anywhere=True)
    while True:
        p_event, p_values = player_window.read()
        log.info(p_event)
        if p_event == sg.WIN_CLOSED or p_event == 'Exit':
            log.info("Closing window")
            break
        if p_event == 'addPlayerName':
            players.append(p_values['--IN--'])
            player_window['-OUTPUT-'].update(p_values['--IN--'])
            break
    player_window.close()
    return players

# Defines listChars menu
def listChars(players):
    msg = ", ".join(players)
    player_menu = [[sg.Text("Current characters: ")],
                  [sg.Text(msg)],
                  [sg.Button(key="Exit", button_text="Ok", size=(10,2))]]
    player_window = sg.Window("Current characters", player_menu, grab_anywhere=True)
    while True: 
        p_event, p_values = player_window.read()
        log.info(p_event)
        if p_event == sg.WIN_CLOSED or p_event == 'Exit':
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
            break
    window.close()

def loadPartyFromFile(players):
    ''' Allows loading/viewing of .txt files defining character names '''
    player_menu = [[sg.Input(key='-INPUT-')],
                  [sg.FileBrowse(key='Browse', file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*")), target='-INPUT-')],
                  [sg.Button("Load file", size=(10,2)), sg.Button("View file", size=(10,2)), sg.Button("Exit", size=(10,2))]]
    player_window = sg.Window("Load party from file", player_menu, grab_anywhere=True)
  
    while True:
        p_event, p_values = player_window.read()
        log.info(p_event)
        if p_event == sg.WINDOW_CLOSED or p_event == 'Exit':
            break
        elif p_event == 'View file':
            filename = p_values['-INPUT-']
            if Path(filename).is_file():
                try:
                    with open(filename, "rt", encoding='utf-8') as f:
                        text = f.read()
                        log.info(text)
                    openFile(filename, text)
                except Exception as e:
                    print("Error: ", e)
        elif p_event == 'Load file':
            filename = p_values['-INPUT-']
            if Path(filename).is_file():
                try:
                    with open(filename, "rt", encoding='utf-8') as f:
                        lines = [line.rstrip('\n') for line in f]
                        for line in lines:
                            log.info(line)
                            players.append(line)
                except Exception as e:
                    print("Error: ", e)
    player_window.close()   
    return players

# Display, and interact with the main window 
def Main(): 
    ''' The main window, used to call all sub-methods'''
    players = []
    while True:
        m_event, m_values = main_window.read()
        log.info(m_event)
        if m_event == sg.WIN_CLOSED or m_event == 'Exit':
            break
        if m_event == 'addPlayers':
            players = addPlayers(players)
        if m_event == 'listChars':
            players = listChars(players)
        if m_event == 'loadPartyFromFile':
            players = loadPartyFromFile(players)
    main_window.close()

if __name__ == '__main__':
    Main()