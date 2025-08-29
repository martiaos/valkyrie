from log import logger  # ← Add this import at the top

class Creature:
    def __init__(self, name, type_, hp=None, ac=None, initiative=None, initiative_mod=0):
        self.name = name
        self.type = type_
        self.hp = int(hp) if hp is not None else None
        self.ac = int(ac) if ac is not None else None
        self.initiative = initiative
        self.initiative_mod = int(initiative_mod)

        logger.info(f"Created {self}")

    def __str__(self):
        parts = [f"{self.name} ({self.type})"]
        if self.hp is not None:
            parts.append(f"HP: {self.hp}")
        if self.ac is not None:
            parts.append(f"AC: {self.ac}")
        if self.initiative is not None:
            parts.append(f"Init: {self.initiative}")
        return " | ".join(parts)
