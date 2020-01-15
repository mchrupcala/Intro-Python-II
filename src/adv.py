from room import Room
from player import Player 
import sys
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# print(str(room['outside'].n_to))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
play_name = str(input("What do you want to name your character: "))
player = Player(play_name, 'outside')
cur_room = room[player.current_room]
new_direction = ""

# Write a loop that:
while cur_room != "treasure":
# * Prints the current room name
    print(f"{player.name} is currently in: {cur_room}")

# * Prints the current description (the textwrap module might be useful here).
    print((cur_room.description))

# * Waits for user input and decides what to do.
#


# what's going on here...how do I write a user_direction + method into line 62?
    new_direction = str(input("Please choose a direction (n/s/e/w/ or 'q' to quit): "))

    # new_direction = global()[new_direction]
    if new_direction == 'n' and cur_room.n_to != '':
        cur_room = cur_room.n_to
    elif new_direction == 's' and cur_room.s_to != '':
        cur_room = cur_room.s_to
    elif new_direction == 'e' and cur_room.e_to != '':
        cur_room = cur_room.e_to
    elif new_direction == 'w' and cur_room.w_to != '':
        cur_room = cur_room.w_to
    elif new_direction == 'q':
        sys.exit()
    else:
        print("Sorry but that movement isn't allowed.")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
