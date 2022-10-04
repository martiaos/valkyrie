# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# logging
import logging
# check platform
import platform
# sys flow
import sys
# Reading env
import os

# pretty iters
from tqdm import tqdm
# Loading env
from dotenv import load_dotenv
# Reading paths
from pathlib import Path
# Interactive debug
from IPython import embed

from partyHandling import addPlayers, listChars, openFile, loadPartyFromFile
from enemyHandling import addEnemies, listEnemies, loadEnemiesFromFile

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

# GUI
import PySimpleGUI as sg

# Define the base window's contents
top_menu = [[sg.Text("Valkyrie has awakened! What happens below?")],
            [sg.Button(key='addPlayers', button_text='Add player character', size=(20,5)),
             sg.Button(key='listChars', button_text='List characters', size=(20,5)),
             sg.Button(key='loadPartyFromFile', button_text='Load party from file', size=(20,5)),
             sg.Button(key='clearParty', button_text="Clear party", size=(20,5))],
            [sg.Button(key='addEnemies', button_text='Add enemies', size=(20,5)),
            sg.Button(key='listEnemies', button_text='List enemies', size=(20,5)),
            sg.Button(key='loadEnemiesFromFile', button_text="Load enemies from file", size=(20,5)),
            sg.Button(key='clearEnemies', button_text="Clear enemies", size=(20,5))
            ],
            [sg.Button(key='startBattle', button_text='Start Battle', size=(45,5)),
            sg.Button("Exit", size=(45,5))]
         ]
# Create the base window
main_window = sg.Window("Valhalla responds!", top_menu, grab_anywhere=True)

# Display, and interact with the main window
def Main():
    ''' The main window, used to call all sub-methods'''
    players = []
    enemies = []
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
        if m_event == 'clearParty':
            players = []
        if m_event == 'addEnemies':
            enemies = addEnemies(enemies)
        if m_event == 'listEnemies':
            enemies = listEnemies(enemies)
        if m_event == 'loadEnemiesFromFile':
            enemies = loadEnemiesFromFile(enemies)
        if m_event == 'clearEnemies':
            enemies =  []
        if m_event == 'startBattle':
            log.critical("Battle commences!")
    main_window.close()


if __name__ == '__main__':
    Main()
