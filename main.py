from tkinter import Tk, messagebox

from ui.layout import create_main_layout
from ui.update_display import update_display
from ui.theme import BG_COLOR
from logic.add_handlers import bind_add_buttons
from logic.file_loaders import bind_file_buttons
from logic.combat import bind_combat_toggle

# Initialize main window
root = Tk()
root.title("Valkyrie - D&D 5e Tracker")
root.geometry("1024x768")
root.configure(bg=BG_COLOR)

# Create UI layout and widgets
widgets = create_main_layout(root)

# Bind functional logic
bind_add_buttons(widgets)
bind_file_buttons(widgets)
bind_combat_toggle(widgets)

# Graceful exit
def confirm_exit():
    if messagebox.askokcancel("Exit Valkyrie", "Are you sure you want to exit?"):
        root.destroy()

widgets["exit_btn"].config(command=confirm_exit)

# Initial visual update
update_display(widgets["display_box"])

# Run the app
root.mainloop()
