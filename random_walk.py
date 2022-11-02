# Req #1 Import choice from random library
from random import choice

class RandomWalk:
    """A class to generate random walks."""
    # Req 2.1 Initialize class with default value of 5000
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        # All walks start at (0, 0).
        # Req 2.2 Initialize x_values and y_values to zero
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
    
        # Keep taking steps until the walk reaches the desired length.
        #Req 3.1 While loop that will loop as long as num_points is greater
        while len(self.x_values) < self.num_points:
        
            # Decide which direction to go and how far to go in that direction.
            # Req 3.2 Decide direction and distance of x_direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
        
            # Req 3.3 Decide direction and distance of y_direction
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
        
            # Req.3.4 Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
        
            # Req 3.5Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            # Req 3.6 Append the values to both x_values and y_values        
            self.x_values.append(x)
            self.y_values.append(y)
