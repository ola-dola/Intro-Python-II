from room import Room
from player import Player
from item import Item
# Declare all the rooms

water = Item("water", "good for the journey")
coins = Item("coins", "shines bright like a diamond")
sword = Item("sword", "cuts you, saves you")
chain = Item("chain", "can tie you down, you can tie your enemy")
naira = Item("naira", "some say it is worthless. I will take 382mil anyday tho (o__0)")
guitar = Item("naira", "who is the best to do it? KSA or Fatai Rolling Dollar?")
sanitizer = Item("sanitizer", "wash off all the virus, before they mess you up")
chloro = Item("chloroquine", "Some say do not believe trump. Do you think it is fair to drag drugs into politics?")
gloves = Item("gloves", "Do you have what it takes to beat Wilder?")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", water, sanitizer),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", chain, naira, chloro),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", sword, chloro, gloves),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", coins, sword, gloves),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", water, coins, sanitizer, naira, guitar, chloro),
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

player = Player("Ola", room["outside"])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print("You are currently in " + player.current_room.name)
    print(player.current_room.description + "\n")

    print("Items available to you in this room are:")
    for item in player.current_room.items:
        print("\t" + item.name)
    
    dir = input("Pick a direction to change room:  ")

    if dir == "n":
        try:
            player.current_room = player.current_room.n_to
        except AttributeError:
            print("Aww schmucks! No way there. Pick another direction \n")
    elif dir == "s":
        try:
            player.current_room = player.current_room.s_to
        except AttributeError:
            print("Aww schmucks! No way there. Pick another direction \n")
    elif dir == "e":
        try:
            player.current_room = player.current_room.e_to
        except AttributeError:
            print("Aww schmucks! No way there. Pick another direction \n")
    elif dir == "w":
        try:
            player.current_room = player.current_room.w_to
        except AttributeError:
            print("Aww schmucks! No way there. Pick another direction \n")
    elif dir == "q":
        print(f"It's been nice playing with you {player.name}. I hope you come back, and become addicted to my game \n")
        break
    else:
        print("You can only move in n-s-e-w directions")