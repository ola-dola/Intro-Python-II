# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, *args):
        self.name = name
        self.description = description
        self.items = [*args]

    def __str__(self):
        return f"name: {self.name}, description: {self.description}"
