# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.last_room = None

    def check_inventory(self):
        print(f"\nYou're holding the following items: {self.items}")

    def travel(self, direction):
        # Player should be able to move in a direction
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.last_room = self.current_room
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction.")

    def __repr__(self):
        return self.name