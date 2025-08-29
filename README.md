# Valkyrie

**Valkyrie** is a touchscreen-friendly combat tracker for Dungeons & Dragons 5e, designed for use on a Raspberry Pi with a 7" display. It provides a fast and intuitive interface for tracking initiative, managing characters, and running combat at the table.

---

## Features

- Add/remove players and enemies
- Load characters from files
- Auto-roll initiative for enemies with modifiers
- Manual initiative input for players
- Toggle between Setup and Combat mode
- Styled for clarity and large-touch interface

---

## Project Structure

```
valkyrie/
├── main.py
├── state.py
├── logic/
│   ├── creature.py
│   ├── add_handlers.py
│   ├── file_loaders.py
│   └── combat.py
├── ui/
│   ├── layout.py
│   ├── theme.py
│   └── update_display.py
├── assets/
│   ├── example_party.txt
│   └── example_enemies.txt
```

---

## File Format

### Party File (example_party.txt)
Each line: `name,hp,ac`
```
Heidi,38,17
Hilda,26,13
Theren,22,15
```

### Enemy File (example_enemies.txt)
Each line: `name,hp,ac,initiative_mod`
```
Goblin,7,15,2
Orc,15,13,1
Kobold,5,12,3
```

---

## Running the App

Ensure you have Python 3 installed. No external libraries are required (Tkinter is included by default).

```bash
python3 main.py
```

For fullscreen on Raspberry Pi:
```python
root.attributes('-fullscreen', True)
```

To exit fullscreen, bind the Escape key:
```python
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))
```

---

## Roadmap

- [ ] Turn counter & next-turn highlight
- [ ] HP tracking with buttons
- [ ] Status effect tagging
- [ ] Save/load current encounters

---

## License
MIT License