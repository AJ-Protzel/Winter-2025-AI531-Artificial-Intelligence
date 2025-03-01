# WumpusWorld
# A simulated representation of a real Wumpus World, aligned with the specified
# characteristics in the AIMA text.
# Note: This is not a state model. It _is_ the real world / environment within
# which the agent operates. Think of it as actual, physical, reality.
# Note 2: This simulation will not include the modeling of time, for the sake of
# simplicity. This only affects the 'Bump' and 'Scream' percepts. In the case of
# 'Bump', we assume that when an agent is in a room facing a wall, it should receive
# the 'Bump' percept. For 'Scream', when the wumpus is killed we let the scream
# linger throughout the cave indefinitely.
# Adrien Protzel

class WumpusWorld:

    EXIT_LOCATION = (1, 1)

    def __init__(self, agent_location = (1,1), agent_direction = 'East',
                       agent_alive = True, wumpus_alive = None,
                       wumpus_location = None, gold_location = None,
                       pit_locations = []):
        self.agent_location = agent_location
        self.agent_direction = agent_direction
        self.agent_alive = agent_alive
        self.wumpus_alive = wumpus_alive
        self.wumpus_location = wumpus_location
        self.gold_location = gold_location
        self.pit_locations = pit_locations

    def percept(self, location):
        """
        The current five-element percept in the `location`. Returns a tuple in the
        form of ('Stench', 'Breeze', 'Glitter', 'Bump', 'Scream'). Any of the elements
        within the returned percept tuple can be None.
        """
        if(location is None): return (None, None, None, None, None)

        percept = [None, None, None, None, None]

        if(self.wumpus_location is not None):
            if(location == self.wumpus_location or self.adjacent(location, self.wumpus_location)):
                percept[0] = 'Stench'

        for pit_location in self.pit_locations:
            if(self.adjacent(location, pit_location)):
                percept[1] = 'Breeze'

        if(location == self.gold_location):
            percept[2] = 'Glitter'

        if(self.agent_bumped_wall()):
            percept[3] = 'Bump'

        if(self.wumpus_alive == False):
            percept[4] = 'Scream'

        return tuple(percept)

    """
    Physical side effects of agent actions
    """

    def turned_left(self):
        """
        Turn the agent counter-clockwise, to the left, resulting in a new
        `agent_direction`.
        """
        directions = ['North', 'West', 'South', 'East']
        curr_dir = directions.index(self.agent_direction)
        new_dir = (curr_dir + 1) % len(directions)
        self.agent_direction = directions[new_dir]

    def turned_right(self):
        """
        Turn the agent clockwise, to the right, resulting in a new `agent_direction`.
        """
        directions = ['North', 'West', 'South', 'East']
        curr_dir = directions.index(self.agent_direction)
        new_dir = (curr_dir - 1) % len(directions)
        self.agent_direction = directions[new_dir]

    def moved_forward(self):
        """
        Attempt to move forward. When successful, update the agent location.
        Moving into a pit location kills the agent.
        Moving into a living wumpus location kills the agent.
        """
        if(not self.agent_bumped_wall()):
            x, y = self.agent_location
            if(self.agent_direction == 'North'):
                self.agent_location = (x, y+1)
            if(self.agent_direction == 'South'):
                self.agent_location = (x, y-1)
            if(self.agent_direction == 'East'):
                self.agent_location = (x+1, y)
            if(self.agent_direction == 'West'):
                self.agent_location = (x-1, y)

        if((self.agent_location in self.pit_locations) or \
            (self.agent_location == self.wumpus_location and self.wumpus_alive == True)):
            self.agent_alive = False

    def grabbed(self):
        """
        Attempt to grab the gold. Successful when executed in `gold_location`, in
        which case the gold location should be set to None.
        """
        if(self.agent_location == self.gold_location and self.gold_location is not None):
            self.gold_location = None

    def climbed(self):
        """
        Attempt to climb out of the cave. Successful when executed in location
        (1, 1), in which case the agent location should be set to None.
        """
        if(self.agent_location == (1,1)):
            self.agent_location = None

    def shot(self):
        """
        Shoot the arrow. If the arrow strikes the wumpus, then the wumpus should
        no longer be alive.
        """
        if(self.wumpus_alive == True and \
            self.agent_direction == 'North' and self.wumpus_north_of_agent() or \
            self.agent_direction == 'South' and self.wumpus_south_of_agent() or \
            self.agent_direction == 'East' and self.wumpus_east_of_agent() or \
            self.agent_direction == 'West' and self.wumpus_west_of_agent()):
            self.wumpus_alive = False  

    """
    Helper methods
    """

    def adjacent(self, location, target):
        """
        Is `location` immediately north, south, east or west of `target`?
        """
        if location is None or target is None:
            return False
        
        x1, y1 = location
        x2, y2 = target
        return (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1)

    def agent_can_move_north(self):
        """
        Can the agent move north?
        """
        return self.agent_location[1] < 4

    def agent_can_move_south(self):
        """
        Can the agent move south?
        """
        return self.agent_location[1] > 1

    def agent_can_move_east(self):
        """
        Can the agent move east?
        """
        return self.agent_location[0] < 4

    def agent_can_move_west(self):
        """
        Can the agent move west?
        """
        return self.agent_location[0] > 1

    def wumpus_north_of_agent(self):
        """
        Is the wumpus somewhere to the north of the agent?
        """
        x1, y1 = self.agent_location
        x2, y2 = self.wumpus_location
        return x1 == x2 and y2 > y1

    def wumpus_south_of_agent(self):
        """
        Is the wumpus somewhere to the south of the agent?
        """
        x1, y1 = self.agent_location
        x2, y2 = self.wumpus_location
        return x1 == x2 and y2 < y1

    def wumpus_east_of_agent(self):
        """
        Is the wumpus somewhere to the east of the agent?
        """
        x1, y1 = self.agent_location
        x2, y2 = self.wumpus_location
        return y1 == y2 and x2 > x1

    def wumpus_west_of_agent(self):
        """
        Is the wumpus somewhere to the west of the agent?
        """
        x1, y1 = self.agent_location
        x2, y2 = self.wumpus_location
        return y1 == y2 and x2 < x1

    def agent_bumped_wall(self):
        """
        Did the agent bump into a wall? (Or, is the agent facing a wall?)
        """
        if(self.agent_location is None):
            return False
        
        x, y = self.agent_location
        return (
            (y == 4 and self.agent_direction == 'North') or
            (y == 1 and self.agent_direction == 'South') or
            (x == 4 and self.agent_direction == 'East') or
            (x == 1 and self.agent_direction == 'West')
        )
