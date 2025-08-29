import tkinter as tk
from ui.theme import BG_COLOR, TEXT_COLOR, BUTTON_FONT, TEXT_FONT

def create_main_layout(root):
    widgets = {}

    # Header
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(pady=5)
    tk.Label(frame, text="\u2694 VALKYRIE \u2694", font=BUTTON_FONT, fg=TEXT_COLOR, bg=BG_COLOR).pack()

    # Menus Frame
    menu_container = tk.Frame(root, bg=BG_COLOR)
    menu_container.pack(pady=10)  # 🛠️ Patched: changed from .grid(...) to .pack(...)
    widgets["menu_container"] = menu_container

    # --- Setup Menu ---
    setup_frame = tk.Frame(menu_container, bg=BG_COLOR)
    widgets["setup_frame"] = setup_frame

    widgets["add_player_btn"] = tk.Button(setup_frame, text="Add Party Member", font=BUTTON_FONT, fg="white", bg="#4A90E2", width=16)
    widgets["load_party_btn"] = tk.Button(setup_frame, text="Load Party", font=BUTTON_FONT, fg="white", bg="#357ABD", width=16)
    widgets["export_party_btn"] = tk.Button(setup_frame, text="Export Party", font=BUTTON_FONT, fg="white", bg="#255E9C", width=16)

    widgets["add_enemy_btn"] = tk.Button(setup_frame, text="Add Enemy", font=BUTTON_FONT, fg="white", bg="#D43F3A", width=16)
    widgets["load_enemy_btn"] = tk.Button(setup_frame, text="Load Enemies", font=BUTTON_FONT, fg="white", bg="#B7322F", width=16)
    widgets["export_enemy_btn"] = tk.Button(setup_frame, text="Export Enemies", font=BUTTON_FONT, fg="white", bg="#A12B29", width=16)

    widgets["clear_btn"] = tk.Button(setup_frame, text="Clear", font=BUTTON_FONT, fg="white", bg="#CC7722", width=16)
    widgets["toggle_btn"] = tk.Button(setup_frame, text="\u2694 Start Battle", font=BUTTON_FONT, fg="white", bg="#3A7F68", width=16)
    widgets["exit_btn"] = tk.Button(setup_frame, text="Exit", font=BUTTON_FONT, fg="white", bg="#444444", width=16)

    # Grid layout for setup menu
    widgets["add_player_btn"].grid(row=0, column=0, padx=5, pady=5)
    widgets["load_party_btn"].grid(row=0, column=1, padx=5, pady=5)
    widgets["export_party_btn"].grid(row=0, column=2, padx=5, pady=5)

    widgets["add_enemy_btn"].grid(row=1, column=0, padx=5, pady=5)
    widgets["load_enemy_btn"].grid(row=1, column=1, padx=5, pady=5)
    widgets["export_enemy_btn"].grid(row=1, column=2, padx=5, pady=5)

    widgets["clear_btn"].grid(row=2, column=0, padx=5, pady=(10, 5))
    widgets["toggle_btn"].grid(row=2, column=1, padx=5, pady=(10, 5))
    widgets["exit_btn"].grid(row=2, column=2, padx=5, pady=(10, 5))

    setup_frame.grid(row=0, column=0, sticky="nsew")

    # --- Combat Menu ---
    combat_frame = tk.Frame(menu_container, bg=BG_COLOR)
    widgets["combat_frame"] = combat_frame

    widgets["return_btn"] = tk.Button(combat_frame, text="Return to Setup", font=BUTTON_FONT, fg="white", bg="#3A7F68", width=50)
    widgets["hit_btn"] = tk.Button(combat_frame, text="Hit!", font=BUTTON_FONT, fg="white", bg="#8B0000", width=23)
    widgets["modify_btn"] = tk.Button(combat_frame, text="Add HP", font=BUTTON_FONT, fg="white", bg="#996600", width=23)
    widgets["next_turn_btn"] = tk.Button(combat_frame, text="Next Turn", font=BUTTON_FONT, fg="white", bg="#228B22", width=50)

    # Row 0: Return to Setup — full width across 2 columns
    widgets["return_btn"].grid(row=0, column=0, columnspan=2, pady=(5, 5), padx=5, sticky="ew")

    # Row 1: Hit and Add HP — side by side
    widgets["hit_btn"].grid(row=1, column=0, padx=(5, 2), pady=5, sticky="ew")
    widgets["modify_btn"].grid(row=1, column=1, padx=(2, 5), pady=5, sticky="ew")

    # Row 2: Next Turn — full width across 2 columns
    widgets["next_turn_btn"].grid(row=2, column=0, columnspan=2, pady=(5, 5), padx=5, sticky="ew")

    combat_frame.grid(row=0, column=0, sticky="nsew")
    combat_frame.lower()  # Hide combat menu by default

    # Round Label
    widgets["round_label"] = tk.Label(root, text="", font=BUTTON_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
    widgets["round_label"].pack()

    # Display Box
    widgets["display_box"] = tk.Text(root, wrap="none", font=TEXT_FONT,
                                     bg="#2b2b2b", fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                                     bd=2, relief="ridge")
    widgets["display_box"].pack(fill="both", expand=True, padx=10, pady=5)

    # Allow selection via click
    def on_display_click(event):
        widget = event.widget
        index = widget.index(f"@{event.x},{event.y}")
        widget.mark_set("insert", index)
        widget.focus_set()

        from ui.update_display import update_selected_creature
        update_selected_creature(widget)

    widgets["display_box"].bind("<Button-1>", on_display_click)

    return widgets
