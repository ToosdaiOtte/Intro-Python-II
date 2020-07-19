from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input("What is your name?\n")
active_player = Player(player_name, room['outside'])

# print(active_player.name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

current_location = active_player.current_room
print(f'{active_player.name}, You are in the {active_player.current_room.name}\n', current_location.description)


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    user_input = input("Where would you like to go? n, e, s, w, or q to quit.")

    # North
    if user_input == 'n':
        print(f'Onward north!\n')

        if current_location.name == 'Outside Cave Entrance':
            active_player = Player(player_name, room['outside'].n_to)
            current_location = active_player.current_room
            print(f'{active_player.name}, You are now in the {active_player.current_room.name}\n', current_location.description)

        elif current_location.name == 'Foyer':
            active_player = Player(player_name, room['overlook'])
            current_location = active_player.current_room
            print(f'{active_player.name}, You are now in the {active_player.current_room.name}\n', current_location.description)

        elif current_location.name == 'Grand Overlook':
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location.name == 'Narrow Passage':
            active_player = Player(player_name, room['treasure'])
            current_location = active_player.current_room
            print(f'{active_player.name}, You are now in the {active_player.current_room.name}\n', current_location.description)

        elif current_location.name == 'Treasure Chamber':
            print(f'{active_player.name}, there is no path this way!\n')
    
    # South
    elif user_input == 's':
        print('Onward south!')

        if current_location.name == 'Outside Cave Entrance':
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location.name == 'Foyer':
            active_player = Player(player_name, room['outside'])
            current_location = active_player.current_room
            print(f'{active_player.name}, You are back in the {active_player.current_room.name}\n', current_location.description) 

        elif current_location.name == 'Grand Overlook':
            active_player = Player(player_name, room['foyer'])
            current_location = active_player.current_room
            print(f'{active_player.name}, You are back in the {active_player.current_room.name}\n', current_location.description)

        elif current_location.name == 'Narrow Passage':
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location.name == 'Treasure Chamber':
            active_player = Player(player_name, room['narrow'])
            current_location = active_player.current_room
            print(f'{active_player.name}, You are now in the {active_player.current_room.name}\n', current_location.description)

    # East
    elif user_input == 'e':
        print('Onward east!')

        if current_location.name == 'Outside Cave Entrance':
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location.name == 'Foyer':
            active_player = Player(player_name, room['narrow'])
            current_location = active_player.current_room
            print(f'{active_player.name}, You are now in the {active_player.current_room.name}\n', current_location.description)
        
        elif current_location.name == 'Grand Overlook':
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location.name == 'Narrow Passage':
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location.name == 'Treasure Chamber':
            print(f'{active_player.name}, there is no path this way!\n')

    # West    
    elif user_input == 'w':
        print('Onward west!') 

        if current_location.name == 'Outside Cave Entrance':
            print(f'{active_player.name}, there is no path this way!\n')
        
        elif current_location.name == 'Foyer':
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location.name == 'Grand Overlook':
            print(f'{active_player.name}, there is no path this way!\n')

        elif current_location.name == 'Narrow Passage':
            active_player = Player(player_name, room['foyer'])
            current_location = active_player.current_room
            print(f'{active_player.name}, You are back in the {active_player.current_room.name}\n', current_location.description)

        elif current_location.name == 'Treasure Chamber':
            print(f'{active_player.name}, there is no path this way!\n')

    elif user_input == 'q':
        exit()
        


