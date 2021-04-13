# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# logging
import logging
# rich logging
from rich.logging import RichHandler
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

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
)

log = logging.getLogger("Valkyrie")
log.setLevel(logging.INFO)
log.info("Logger initialized")

# Get .env
# load_dotenv()

#Importing package
import PySimpleGUI as sg

# Define the window's contents
layout = [ [sg.Text("Set values")],
            [sg.Input()],
            [sg.Button('Enter'), sg.Button("Exit")]
         ]

# Create the window
window = sg.Window("This is a textbox", layout, grab_anywhere=True)

# Display, and interact with the window
while True:
    event, values = window.read()
    log.info(event)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Enter':
        log.info("Button pressed")
        log.info(f"Entered value {values[0]}")
window.close()

# Finish up by removing the screen
window.close()
