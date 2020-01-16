import textwrap
from player import Player

# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __repr__(self):
        display_string = ""
        display_string = f"\n----------------\nPlayer is currently in: {self.name}"

        if self.name != "Outside Cave Entrance":
            display_string += "\n\nThe sound of your shuffling footsteps echoes off the walls..."
        
        display_string += "\n\n" + textwrap.fill(self.description, width=100)

        return display_string


    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None