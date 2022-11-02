#Req 1 Import randint function from random library
from random import randint

#Req 2 Define the Die Class
class Die:
    """A class representing a single die."""
    # Req 2.1 Create constructor with default num_sides value of 6
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
    # Req 2.2 Create roll fumction using randint function 
    # that will roll a number from 1 to the number of sides of die    
    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
