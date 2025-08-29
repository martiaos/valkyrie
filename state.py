# Shared global state

players = []
enemies = []
initiative_order = []

in_combat = False
current_turn_index = 0
round_number = 1

# Hit! targeting support
line_to_creature_map = []
selected_creature = None
