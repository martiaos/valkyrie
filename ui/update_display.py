import state

def update_selected_creature(display_box):
    index = display_box.index("insert")
    line = int(index.split(".")[0])

    for line_num, creature in state.line_to_creature_map:
        if line == line_num:
            state.selected_creature = creature
            break
    else:
        state.selected_creature = None

    update_display(display_box)

def update_display(display_box):
    display_box.delete("1.0", "end")
    state.line_to_creature_map = []

    # Clear highlights
    display_box.tag_remove("selected", "1.0", "end")
    display_box.tag_remove("sel", "1.0", "end")

    # Tag configs
    display_box.tag_configure("unconscious", overstrike=True, font="Courier 14")
    display_box.tag_configure("normal", font="Courier 14")
    display_box.tag_configure("selected", background="#333366")

    if state.in_combat and state.initiative_order:
        display_box.insert("end", f"{'':3}{'Name':20} {'Type':8} {'Init':5} {'HP':4} {'AC':3}\n")
        display_box.insert("end", "-" * 70 + "\n")

        for i, c in enumerate(state.initiative_order):
            # Line tracking for click-to-select
            line_num = int(display_box.index("end-1c").split(".")[0])
            state.line_to_creature_map.append((line_num, c))

            prefix = "→ " if i == state.current_turn_index else "   "
            name = c.name if len(c.name) <= 20 else c.name[:17] + "..."
            line = f"{prefix}{name:<20} {c.type[:8]:<8} {c.initiative:<5} {c.hp:<4} {c.ac:<3}\n"

            tags = ["normal"]
            if c.hp is not None and c.hp <= 0:
                tags.append("unconscious")
            if c == state.selected_creature:
                tags.append("selected")

            display_box.insert("end", line, tuple(tags))

    else:
        display_box.insert("end", f"{'Name':20} {'Type':8} {'HP':4} {'AC':4} {'InitMod':7}\n")
        display_box.insert("end", "-" * 70 + "\n")

        for p in state.players:
            name = p.name if len(p.name) <= 20 else p.name[:17] + "..."
            line = f"{name:<20} {p.type:<8} {p.hp:<4} {p.ac:<4} {'-':<7}\n"
            display_box.insert("end", line)

        for e in state.enemies:
            name = e.name if len(e.name) <= 20 else e.name[:17] + "..."
            mod = e.initiative_mod if hasattr(e, "initiative_mod") else "-"
            line = f"{name:<20} {e.type:<8} {e.hp:<4} {e.ac:<4} {mod:<7}\n"
            display_box.insert("end", line)
