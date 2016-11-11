from unicurses import *

stdscr = initscr() # initializes the standard screen

####### GAME FUNCTIONS #######

points = int(20)


##### MAIN FUNCTION ######

print "Welcome! I hear you're looking for a spaceship. "
print "Well you've come to the right place, let's build you a ship!"
name = raw_input("What do you want to name your ship? ")
print "Ok, now on to upgrading "+ name +"."
print "You have 20 points to spend on the strength, tech, and speed of this ship."
strength = int(raw_input("How strong do you want your ship to be? STRENGTH: "))
technology = int(raw_input("And how much high-end technology would you like? TECH: "))
speed = int(raw_input("Lastly, how fast do you want this baby? SPEED: "))


class character:
    def __init__(self, name, strength, technology, speed):
        self.name = name
        self.strength = strength
        self.knowledge = technology
        self.dexterity = speed




#Questions... What is unicode? Global variables? How do you test the code?#
getch()