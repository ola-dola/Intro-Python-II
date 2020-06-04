# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, *args):
        self.name = name
        self.current_room = current_room
        self.items = [*args]

    def __str__(self):
        return f"Player name: {self.name}, current room: {self.current_room}"
