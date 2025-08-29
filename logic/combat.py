from tkinter import messagebox, simpledialog
from random import randint
import state
from ui.update_display import update_display
from log import logger

def bind_combat_toggle(widgets):
    widgets["toggle_btn"].config(command=lambda: toggle_mode(widgets))        # Start battle (setup mode)
    widgets["return_btn"].config(command=lambda: toggle_mode(widgets))        # Return to setup (combat mode)
    widgets["next_turn_btn"].config(command=lambda: next_turn(widgets))
    widgets["hit_btn"].config(command=lambda: hit_selected_creature(widgets))
    widgets["modify_btn"].config(command=lambda: modify_selected_creature_hp(widgets))

def toggle_mode(widgets):
    if not state.in_combat:
        logger.info("Starting combat...")

        enter_player_initiatives()

        for enemy in state.enemies:
            enemy.initiative = randint(1, 20) + enemy.initiative_mod
            logger.debug(f"{enemy.name} rolled {enemy.initiative} (mod {enemy.initiative_mod})")

        state.initiative_order[:] = sorted(
            [c for c in state.players + state.enemies if c.initiative is not None],
            key=lambda c: c.initiative,
            reverse=True
        )

        logger.info("Initiative order:")
        for c in state.initiative_order:
            logger.info(f"  {c.name} ({c.type}) - {c.initiative}")

        # Activate combat mode
        state.in_combat = True
        state.current_turn_index = 0
        state.round_number = 1
        widgets["round_label"].config(text=f"Round {state.round_number}")

        show_combat_controls(widgets)
        logger.info("Combat mode active.")

    else:
        logger.info("Exiting combat mode.")

        # Reset state
        state.initiative_order.clear()
        for c in state.players + state.enemies:
            c.initiative = None
        state.in_combat = False
        state.selected_creature = None

        widgets["round_label"].config(text="")

        hide_combat_controls(widgets)
        logger.info("Returned to setup mode.")

    update_display(widgets["display_box"])

def enter_player_initiatives():
    for p in state.players:
        while True:
            try:
                value = simpledialog.askinteger("Initiative Roll", f"{p.name}'s initiative:", minvalue=1, maxvalue=30)
                if value is not None:
                    p.initiative = value
                    logger.debug(f"{p.name} set to initiative {value}")
                    break
            except ValueError:
                logger.warning(f"Invalid initiative value entered for {p.name}")
                messagebox.showerror("Error", "Please enter a valid number")

def show_combat_controls(widgets):
    widgets["setup_frame"].grid_remove()
    widgets["combat_frame"].grid(row=0, column=0, pady=10)  # ← use .grid()

def hide_combat_controls(widgets):
    widgets["combat_frame"].grid_remove()
    widgets["setup_frame"].grid(row=0, column=0, pady=10)  # ← use .grid()
    
def next_turn(widgets):
    if not state.initiative_order:
        return

    state.current_turn_index += 1
    if state.current_turn_index >= len(state.initiative_order):
        state.current_turn_index = 0
        state.round_number += 1
        logger.info(f"Starting round {state.round_number}")

    widgets["round_label"].config(text=f"Round {state.round_number}")
    update_display(widgets["display_box"])

def hit_selected_creature(widgets):
    target = state.selected_creature

    if not target:
        messagebox.showwarning("No Target", "Please click on a creature in the list first.")
        return

    dmg = simpledialog.askinteger("Damage", f"How much damage to {target.name}?", minvalue=0)

    if dmg is None:
        return

    target.hp = max(0, target.hp - dmg)
    logger.info(f"{target.name} takes {dmg} damage → HP now {target.hp}")

    if target.hp <= 0:
        logger.info(f"{target.name} is now unconscious.")

    update_display(widgets["display_box"])

def modify_selected_creature_hp(widgets):
    target = state.selected_creature

    if not target:
        messagebox.showwarning("No Target", "Please click on a creature in the list first.")
        return

    try:
        delta = simpledialog.askinteger("Modify HP", f"Modify HP for {target.name} (use negative to deal damage):")
        if delta is None:
            return

        old_hp = target.hp
        target.hp = max(0, target.hp + delta)
        logger.info(f"{target.name}: HP {old_hp} → {target.hp}")

        if target.hp <= 0:
            logger.info(f"{target.name} is now unconscious.")

        update_display(widgets["display_box"])

    except Exception as e:
        logger.warning(f"Invalid HP adjustment for {target.name}: {e}")
        messagebox.showerror("Error", "Please enter a valid number.")
