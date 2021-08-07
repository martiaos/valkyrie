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
# Interactive debug
from IPython import embed

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

# Define the window's contents
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
# Create the window
main_window = sg.Window("Valhalla responds!", top_menu, grab_anywhere=True)

def addPlayers(players):
    player_menu = [[sg.Text("What is the character name?")],
               [sg.InputText(key='--IN--')],
<<<<<<< HEAD
               [sg.Submit(key='addPlayerName', button_text="Submit player name", size=(10,2)), sg.Button("Exit", size=(10,2))],
=======
               [sg.Submit(key='addPlayerName', button_text="Submit player name"), sg.Button("Exit")],
>>>>>>> 74cbe97ae260d9f527eb6e10a44c6c046f7e734d
               [sg.Text(size=(15,1), key='-OUTPUT-')]]
    player_window = sg.Window("Adding player character...", player_menu, grab_anywhere=True)
    while True:
        p_event, p_values = player_window.read()
        log.info(m_event)
        if p_event == sg.WIN_CLOSED or p_event == 'Exit':
            break
        if p_event == 'addPlayerName':
            players.append(p_values['--IN--'])
            player_window['-OUTPUT-'].update(p_values['--IN--'])
            break
    player_window.close()
    return players

def loadParty():
    file_menu = [[sg.Text("What is")],
               [sg.InputText(key='--IN--')],
               [sg.Submit(key='addPlayerName', button_text="Submit player name"), sg.Button("Exit")],
               [sg.Text(size=(15,1), key='-OUTPUT-')]]

# Display, and interact with the window
players = []
while True:
    m_event, m_values = main_window.read()
    log.info(m_event)
    if m_event == sg.WIN_CLOSED or m_event == 'Exit':
        break
    if m_event == 'addPlayers':
        players = addPlayers(players)
    if m_event == 'listChars':
        log.info("Current chars are:")
        for char in players:
            log.info(f"{char}")
    if m_event == 'loadPartyFromFile':
        players = loadParty()
main_window.close()
