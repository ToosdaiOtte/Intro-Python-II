# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__ (self, name, description, items):
        self.name = name
        self.description = description
        self.items = items # list of items available in room


    def __str__ (self):
        return f"{self.name}: {self.description}. You've come across a {self.items}"