from tkinter import simpledialog, messagebox
import state
from logic.creature import Creature
from ui.update_display import update_display
from log import logger

def bind_add_buttons(widgets):
    widgets["add_player_btn"].config(command=lambda: add_player(widgets["display_box"]))
    widgets["add_enemy_btn"].config(command=lambda: add_enemy(widgets["display_box"]))

def add_player(widgets):
    if state.in_combat:
        messagebox.showwarning("Combat Mode", "Can't add players during combat.")
        logger.warning("Attempted to add player during combat.")
        return
    name = simpledialog.askstring("Add Player", "Enter player name:")
    if name:
        hp = simpledialog.askinteger("Player HP", f"{name}'s HP:", minvalue=1, maxvalue=999)
        ac = simpledialog.askinteger("Player AC", f"{name}'s AC:", minvalue=1, maxvalue=30)
        if hp is not None and ac is not None:
            state.players.append(Creature(name, "Player", hp=hp, ac=ac))
            logger.info(f"Added player: {name}, HP: {hp}, AC: {ac}")
            update_display(widgets["display_box"])

def add_enemy(widgets):
    if state.in_combat:
        messagebox.showwarning("Combat Mode", "Can't add enemies during combat.")
        logger.warning("Attempted to add enemy during combat.")
        return
    name = simpledialog.askstring("Add Enemy", "Enter enemy name:")
    if name:
        hp = simpledialog.askinteger("Enemy HP", f"{name}'s HP:", minvalue=1, maxvalue=999)
        ac = simpledialog.askinteger("Enemy AC", f"{name}'s AC:", minvalue=1, maxvalue=30)
        mod = simpledialog.askinteger("Initiative Modifier", f"{name}'s initiative mod:", minvalue=-10, maxvalue=10)
        if hp is not None and ac is not None and mod is not None:
            state.enemies.append(Creature(name, "Enemy", hp=hp, ac=ac, initiative_mod=mod))
            logger.info(f"Added enemy: {name}, HP: {hp}, AC: {ac}, Mod: {mod}")
            update_display(widgets["display_box"])

def bind_add_buttons(widgets):
    widgets["add_player_btn"].config(command=lambda: add_player(widgets))
    widgets["add_enemy_btn"].config(command=lambda: add_enemy(widgets))
    widgets["clear_btn"].config(command=lambda: clear_all(widgets))  # ✅ This line

def clear_all(widgets):
    if state.in_combat:
        messagebox.showwarning("In Combat", "Can't clear while combat is active.")
        return

    state.players.clear()
    state.enemies.clear()
    state.selected_creature = None
    logger.info("Cleared all players and enemies.")
    update_display(widgets["display_box"])
    
