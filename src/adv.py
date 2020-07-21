from room import Room
from player import Player
from item import Item

# Declare all the items

item = {
    'sword': Item("Sword of Intimidation",
                  "weild this long, bladed weapon to intimidate other"),
    'sheild': Item("Shield of Safety",
                   "equip this shield in order to protect yourself from attacks"),
    'helmet': Item("Helmet of Honor", 
                   "equip this helmet to better protect your noggin"),
    'bag': Item("Bag of Wonders", "use this to carry any items you may come across"),
    'chest': Item("Chest of treasures", "where is the treasure?")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item['bag']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item["sheild"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['sword']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['helmet']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['chest']),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input("What is your name?\n")
active_player = Player(player_name, room['outside'], [])

# print(active_player.name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

def player_location():
    global current_location
    current_location = active_player.current_room
    print(f'{active_player.name}, You are in the {active_player.current_room.name}\n', current_location.description, f"Look! You've come across a {current_location.items}")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    player_location()
    add_item = input("Enter 'take' to pickup found item(s)\n")

    if add_item == 'take':
        active_player = Player(player_name, current_location, current_location.items)
        print(f"{active_player.name}, you've grabbed {active_player.inventory}")
        
    user_input = input("Where would you like to go? n, e, s, w, or q to quit.\n")

    # North
    if user_input == 'n':
        print(f'Onward north!\n')

        if current_location == room['outside']:
            active_player = Player(player_name, room['outside'].n_to, [])

        elif current_location == room['foyer']:
            active_player = Player(player_name, room['foyer'].n_to, [])

        elif current_location == room['overlook']:
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location == room['narrow']:
            active_player = Player(player_name, room['narrow'].n_to, [])

        elif current_location == room['treasure']:
            print(f'{active_player.name}, there is no path this way!\n')
    
    # South
    elif user_input == 's':
        print('Onward south!')

        if current_location == room['outside']:
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location == room['foyer']:
            active_player = Player(player_name, room['foyer'].s_to, [])

        elif current_location == room['overlook']:
            active_player = Player(player_name, room['overlook'].s_to, [])

        elif current_location == room['narrow']:
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location == room['treasure']:
            active_player = Player(player_name, room['treasure'].s_to, [])

    # # East
    elif user_input == 'e':
        print('Onward east!')

        if current_location == room['outside']:
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location == room['foyer']:
            active_player = Player(player_name, room['foyer'].e_to, [])
        
        elif current_location == room['overlook']:
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location == room['narrow']:
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location == room['treasure']:
            print(f'{active_player.name}, there is no path this way!\n')

    # # West    
    elif user_input == 'w':
        print('Onward west!') 

        if current_location == room['outside']:
            print(f'{active_player.name}, there is no path this way!\n')
        
        elif current_location == room['foyer']:
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location == room['overlook']:
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location == room['narrow']:
            active_player = Player(player_name, room['narrow'].w_to, [])

        elif current_location == room['treasure']:
            print(f'{active_player.name}, there is no path this way!\n')

    elif user_input == 'q':
        exit()