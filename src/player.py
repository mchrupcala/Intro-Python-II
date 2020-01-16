# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def check_inventory(self):
        print(f"You're holding the following items: {self.items}")

    def __repr__(self):
        return self.name