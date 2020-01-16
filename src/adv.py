from room import Room
from player import Player 
from item import Item
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

# Create all items

items = {
    'candlestick': Item("candlestick", "An old metal candlestick that hasn't been used in a long time."),

    'goldcoin': Item("goldcoin", "You inspect the coin. Though it might be dusty, you can see a Portugues cross, and the faint inscription 'IOANNES.V.D.G.PORT.ET.ALG.REX'"),
    
    'whip': Item("whip", "A tightly-wound leather bullwhip."),
    
    'treasure': Item("treasure chest", "A large oak chest filled to the brim with gold coins. It looks heavy!")
}
room['foyer'].items = [items['candlestick'], items["goldcoin"]]
room['overlook'].items = [items['whip']]
room['treasure'].items = [items['treasure']]

# print(str(room['outside'].n_to))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
play_name = str(input("What do you want to name your character: "))
player = Player(play_name, 'outside')
cur_room = room[player.current_room]
last_room = ""

new_direction = ""

# Write a loop that:
while cur_room != "treasure":
# * Prints the current room name
    print(f"{player.name} is currently in: {cur_room}")

# * Prints the current description (the textwrap module might be useful here).
    print(cur_room.description)

    print(f"You notice the following items: {cur_room.items}")

# * Waits for user input and decides what to do.
#



    new_direction = str(input("Please choose a direction (n/s/e/w/ or 'q' to quit): ")).split(" ")


    # If the user enters a cardinal direction, attempt to move to the room there.
    if new_direction[0] == 'n' and cur_room.n_to != '':
        last_room = cur_room
        cur_room = cur_room.n_to
    elif new_direction[0] == 's' and cur_room.s_to != '':
        last_room = cur_room
        cur_room = cur_room.s_to
    elif new_direction[0] == 'e' and cur_room.e_to != '':
        last_room = cur_room
        cur_room = cur_room.e_to
    elif new_direction[0] == 'w' and cur_room.w_to != '':
        last_room = cur_room
        cur_room = cur_room.w_to
    # If the user enters "q", quit the game.
    elif new_direction[0] == 'q':
        sys.exit()
    elif new_direction[0] in ['i', 'inventory']:
        player.check_inventory()
    # Print an error message if the movement isn't allowed.
    else:
        print("Sorry but that movement isn't allowed.")


    #Second IF, which handles the item situation.
    if len(new_direction) == 3:
        new_item = new_direction[2]
        if new_direction[1] in ["get", "take"] and new_item.lower() in str(last_room.items):
            player.items.append(items[new_item])
            last_room.items.remove(items[new_item])
            items[new_item].on_take()

        elif new_direction[1] in ["drop", "leave"] and new_item.lower() in str(player.items):
            cur_room.items.append(items[new_item])
            player.items.remove(items[new_item])
            items[new_item].on_drop()
        else:
            print("The item you selected is not in this room.")




