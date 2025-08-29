from tkinter import filedialog, messagebox
from state import players, enemies, in_combat
from log import logger
from logic.creature import Creature
from ui.update_display import update_display

def bind_file_buttons(widgets):
    widgets["load_party_btn"].config(command=lambda: load_party_from_file(widgets["display_box"]))
    widgets["load_enemy_btn"].config(command=lambda: load_enemies_from_file(widgets["display_box"]))
    widgets["export_party_btn"].config(command=lambda: export_party_to_file())
    widgets["export_enemy_btn"].config(command=lambda: export_enemies_to_file())

def load_party_from_file(display_box):
    if in_combat:
        messagebox.showwarning("Combat Mode", "Can't load party during combat.")
        return

    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not path:
        logger.info("Party file load canceled.")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                name, hp, ac = [x.strip() for x in line.split(",")]
                players.append(Creature(name, "Player", int(hp), int(ac)))
                logger.debug(f"Loaded player: {name}, HP: {hp}, AC: {ac}")
        update_display(display_box)
        logger.info("Party load complete.")
    except Exception as e:
        logger.exception("Error loading party file")
        messagebox.showerror("Error", f"Could not load party: {e}")

def load_enemies_from_file(display_box):
    if in_combat:
        messagebox.showwarning("Combat Mode", "Can't load enemies during combat.")
        return

    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not path:
        logger.info("Enemy file load canceled.")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                name, hp, ac, mod = [x.strip() for x in line.split(",")]
                enemies.append(Creature(name, "Enemy", int(hp), int(ac), None, int(mod)))
                logger.debug(f"Loaded enemy: {name}, HP: {hp}, AC: {ac}, Init Mod: {mod}")
        update_display(display_box)
        logger.info("Enemy load complete.")
    except Exception as e:
        logger.exception("Error loading enemy file")
        messagebox.showerror("Error", f"Could not load enemies: {e}")

def export_party_to_file():
    if in_combat:
        messagebox.showwarning("Combat Mode", "Can't export during combat.")
        return

    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt")],
                                        title="Save Party To File")

    if not path:
        return

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("# name,hp,ac\n")
            for p in players:
                f.write(f"{p.name},{p.hp},{p.ac}\n")
        logger.info(f"Exported party to {path}")
        messagebox.showinfo("Export Complete", "Party successfully exported!")
    except Exception as e:
        logger.exception("Failed to export party")
        messagebox.showerror("Error", f"Failed to export party: {e}")

def export_enemies_to_file():
    if in_combat:
        messagebox.showwarning("Combat Mode", "Can't export during combat.")
        return

    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt")],
                                        title="Save Enemies To File")

    if not path:
        return

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("# name,hp,ac,initiative_mod\n")
            for e in enemies:
                mod = getattr(e, "initiative_mod", 0)
                f.write(f"{e.name},{e.hp},{e.ac},{mod}\n")
        logger.info(f"Exported enemies to {path}")
        messagebox.showinfo("Export Complete", "Enemies successfully exported!")
    except Exception as e:
        logger.exception("Failed to export enemies")
        messagebox.showerror("Error", f"Failed to export enemies: {e}")
