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

    'secret': Room("Secret Annex", "What's this? You found a hidden room!\n\n You walk down a winding staircase into a cramped, musty room. Your eyes dart to a shiny glint of metal in the center of the room....the hidden treasure, full to the brim with gold!!")
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
    
    'treasure': Item("treasure", "A large oak chest filled to the brim with gold coins. It looks heavy!"),

    'statue': Item("statue", "Creepy! This neck-high marble statue sits on an old bookshelf...you could swear that its eyes are looking straight at you.")
}
room['foyer'].items = [items['candlestick'], items["goldcoin"]]
room['overlook'].items = [items['whip']]
room['secret'].items = [items['treasure']]
room['treasure'].items = [items['statue']]

# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = str(input("What do you want to name your character: "))
player = Player(player_name, room['outside'])
print(player.current_room)
game_won = False
directions = ["n", "s", "e", "w"]

# Write a loop that:
while game_won == False :

    if len(player.current_room.items) > 0:
        print(f"\nYou notice the following items: {player.current_room.items}")

    new_direction = str(input("\nPlease choose a direction (n/s/e/w/ or 'q' to quit): ")).split(" ")
    direction = new_direction[0]
    user_action = new_direction[1] if len(new_direction) > 1 else None
    selected_item = new_direction[2] if len(new_direction) > 2 else None

    # If the user enters a cardinal direction, attempt to move to the room there. # If the user enters "q", quit the game. Print an error message if the movement isn't allowed.
    if direction in directions:
        player.travel(direction)
    elif direction == 'q':
        sys.exit()
    elif direction in ['i', 'inventory']:
        player.check_inventory()
    else:
        print("Sorry but that movement isn't allowed.")

    #Second IF, which handles the item situation.
    if len(new_direction) == 3:

        if user_action in ["get", "take"] and selected_item.lower() in str(player.last_room.items):
            player.items.append(items[selected_item])
            player.last_room.items.remove(items[selected_item])
            items[selected_item].on_take()

        elif user_action in ["drop", "leave"] and selected_item.lower() in str(player.items):
            player.last_room.items.append(items[selected_item])
            player.items.remove(items[selected_item])
            items[selected_item].on_drop()
        else:
            print("The item you selected is not in this room.")

    #Unlock the secret room
    if items['statue'] in room['foyer'].items and room['foyer'].w_to == None:
        room['foyer'].w_to = room['secret']
        room['secret'].e_to = room['foyer']
        print("\nYou hear a sudden, grinding noise coming from a latch somewhere in the west-facing wall. It comes to a stop, followed by a soft 'click'")

    #Winner!
    if items['treasure'] in player.items:
        game_won = True
        print('''
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝
                                                      
''')
# http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=YOU%20WIN!%0A
        print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')