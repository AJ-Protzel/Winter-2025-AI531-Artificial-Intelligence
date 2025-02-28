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
        if location is None:
            return (None, None, None, None, None)

        if location == self.gold_location:
            return (None, None, 'Glitter', None, None)

        if self.wumpus_location is not None:
            if location == self.wumpus_location or self.adjacent(location, self.wumpus_location):
                return ('Stench', None, None, None, None)
        
        for pit_location in self.pit_locations:
            if self.adjacent(location, pit_location):
                return (None, 'Breeze', None, None, None)
        
        if(self.agent_bumped_wall):
            return 'Bump'

        return (None, None, None, None, None)  # default catch on fail
        # fail: gold = none, wumpus lcoatin = none, pit adjacent = none
        

    """
    Physical side effects of agent actions
    """

    def turned_left(self):
        """
        Turn the agent counter-clockwise, to the left, resulting in a new
        `agent_direction`.
        """
        pass

    def turned_right(self):
        """
        Turn the agent clockwise, to the right, resulting in a new `agent_direction`.
        """
        pass

    def moved_forward(self):
        """
        Attempt to move forward. When successful, update the agent location.
        Moving into a pit location kills the agent.
        Moving into a living wumpus location kills the agent.
        """
        pass

    def grabbed(self):
        """
        Attempt to grab the gold. Successful when executed in `gold_location`, in
        which case the gold location should be set to None.
        """
        pass

    def climbed(self):
        """
        Attempt to climb out of the cave. Successful when executed in location
        (1, 1), in which case the agent location should be set to None.
        """
        pass

    def shot(self):
        """
        Shoot the arrow. If the arrow strikes the wumpus, then the wumpus should
        no longer be alive.
        """
        pass

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
        return self.adjacent((x1, y1 + 1), (x2, y2))

    def wumpus_south_of_agent(self):
        """
        Is the wumpus somewhere to the south of the agent?
        """
        x1, y1 = self.agent_location
        x2, y2 = self.wumpus_location
        return self.adjacent((x1, y1 - 1), (x2, y2))

    def wumpus_east_of_agent(self):
        """
        Is the wumpus somewhere to the east of the agent?
        """
        x1, y1 = self.agent_location
        x2, y2 = self.wumpus_location
        return self.adjacent((x1 + 1, y1), (x2, y2))

    def wumpus_west_of_agent(self):
        """
        Is the wumpus somewhere to the west of the agent?
        """
        x1, y1 = self.agent_location
        x2, y2 = self.wumpus_location
        return self.adjacent((x1 - 1, y1), (x2, y2))

    def agent_bumped_wall(self):
        """
        Did the agent bump into a wall? (Or, is the agent facing a wall?)
        """
        x, y = self.agent_location
        if(self.agent_direction == 'North'):
            return y == 4 or not self.adjacent((x, y + 1), (x, y))
        elif(self.agent_direction == 'South'):
            return y == 1 or not self.adjacent((x, y - 1), (x, y))
        elif(self.agent_direction == 'East'):
            return x == 4 or not self.adjacent((x + 1, y), (x, y))
        elif(self.agent_direction == 'West'):
            return x == 1 or not self.adjacent((x - 1, y), (x, y))
        else:
            return False

