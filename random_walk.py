from random import choice


class Randomwalk:
    """A class to create random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_value = [0]
        self.y_value = [0]

    @staticmethod
    def get_step():
        """Calculate the number of steps taken for each instance"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5])
        return distance * direction

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_value) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # Reject zero movements in both directions
            if y_step == 0 and x_step == 0:
                continue
            # Calculate the new position.
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)
