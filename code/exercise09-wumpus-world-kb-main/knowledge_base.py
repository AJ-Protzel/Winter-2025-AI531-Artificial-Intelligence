# KnowledgeBase
# A knowledge base for a knowledge-based agent.

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:

    def __init__(self, agent_location, agent_direction):
        """Initialize the agent with its location and direction."""
        self.agent_location = agent_location  # Set the agent's current location
        self.agent_direction = agent_direction  # Set the agent's current direction
        self.cells = {}  # Initialize an empty dictionary to store cell information
        self.actions = []  # Initialize an empty list to store actions
        self.path = []  # Initialize an empty list to store the path
        self.found_gold = False  # Flag to indicate if gold is found
        self.grabbed_gold = False  # Flag to indicate if gold is grabbed
        self.found_cave = False  # Flag to indicate if cave is found
        self.at_cave = False  # Flag to indicate if agent is at the cave
        self.found_wumpus = False  # Flag to indicate if Wumpus is found
        self.dead_wumpus = False  # Flag to indicate if Wumpus is dead

    def tell(self, info):
        """Process the information received by the agent."""
        if isinstance(info, str):
            self.actions.append(info)  # Add the action to the actions list
        else:
            x, y = self.agent_location  # Get the current location coordinates
            locations = {
                "Current": (x, y),  # Current location
                "North": (x, y + 1),  # Location to the north
                "South": (x, y - 1),  # Location to the south
                "East": (x + 1, y),  # Location to the east
                "West": (x - 1, y)  # Location to the west
            }
            for location in locations.values():
                if location not in self.cells:
                    self.cells[location] = {"Rev": False, "Env": 'empty'}  # Initialize cell information
            self.cells[self.agent_location].update({"Rev": True, "Env": 'empty'})  # Update current cell information
            if self.agent_location == (1, 1):
                self.cells[self.agent_location]["Env"] = 'cave'  # Mark the cell as cave
                self.found_cave = True  # Set found_cave flag to True
                self.at_cave = True  # Set at_cave flag to True
            else:
                self.at_cave = False  # Set at_cave flag to False
            for percept in reversed(info):
                if percept == 'Stench':
                    self.found_wumpus = True  # Set found_wumpus flag to True
                    if not self.dead_wumpus:
                        for location in locations.values():
                            if not self.cells[location]["Rev"] and self.cells[location]["Env"] != 'wall':
                                self.cells[location]["Env"] = 'wumpus'  # Mark the cell as wumpus
                elif percept == 'Breeze':
                    for location in locations.values():
                        if not self.cells[location]["Rev"] and self.cells[location]["Env"] != 'wall':
                            self.cells[location]["Env"] = 'pit'  # Mark the cell as pit
                elif percept == 'Glitter':
                    self.cells[self.agent_location]["Env"] = 'gold'  # Mark the cell as gold
                    self.found_gold = True  # Set found_gold flag to True
                elif percept == 'Bump':
                    self.cells[locations[self.agent_direction]]["Env"] = 'wall'  # Mark the cell as wall
                elif percept == 'Scream':
                    if not self.dead_wumpus:
                        for location, cell in self.cells.items():
                            if cell["Env"] == 'wumpus':
                                cell["Env"] = 'empty'  # Mark the cell as empty
                                self.dead_wumpus = True  # Set dead_wumpus flag to True

    def ask(self, t):
        """Determine the next action based on the current state."""
        if self.found_wumpus and not self.dead_wumpus:
            return self.hunt()  # Hunt the Wumpus
        if self.found_gold:
            if self.grabbed_gold:
                if self.found_cave:
                    if self.at_cave:
                        return WumpusWorldAgent.climb  # Climb out of the cave
                    else:
                        if not self.path:
                            self.find_path()  # Find the path to the cave
                        return self.follow_path()  # Follow the path to the cave
                else:
                    return self.explore(t)  # Explore the environment
            elif self.cells[self.agent_location]["Env"] == 'gold':
                self.grabbed_gold = True  # Set grabbed_gold flag to True
                return WumpusWorldAgent.grab  # Grab the gold
        return self.explore(t)  # Explore the environment

    def move(self, action):
        """Move the agent based on the given action."""
        x, y = self.agent_location  # Get the current location coordinates
        locations = {
            "North": ((x, y + 1), {"West": 'left', "East": 'right', "South": 'back'}),  # Location and turns for North
            "South": ((x, y - 1), {"East": 'left', "West": 'right', "North": 'back'}),  # Location and turns for South
            "East": ((x + 1, y), {"North": 'left', "South": 'right', "West": 'back'}),  # Location and turns for East
            "West": ((x - 1, y), {"South": 'left', "North": 'right', "East": 'back'})  # Location and turns for West
        }
        if action == 'get_locations':
            return locations  # Return the locations dictionary
        if action == 'get_turn':
            if self.agent_direction in locations:
                location, turns = locations[self.agent_direction]
                return turns  # Return the turns dictionary for the current direction
        if action == 'forward':
            new_location, _ = locations[self.agent_direction]
            self.agent_location = new_location  # Update the agent's location
            return WumpusWorldAgent.move_forward  # Move the agent forward
        if action == 'left':
            turns = self.move('get_turn')
            new_direction = [dir for dir, turn in turns.items() if turn == 'left'][0]
            self.agent_direction = new_direction  # Update the agent's direction
            return WumpusWorldAgent.turn_left  # Turn the agent left
        if action == 'right' or action == 'back':
            turns = self.move('get_turn')
            new_direction = [dir for dir, turn in turns.items() if turn == 'right'][0]
            self.agent_direction = new_direction  # Update the agent's direction
            return WumpusWorldAgent.turn_right  # Turn the agent right

    def hunt(self):
        """Hunt the Wumpus based on the current state."""
        for direction, (location, turns) in self.move('get_locations').items():
            if self.cells[location]["Env"] == 'wumpus':
                if self.agent_direction == direction:
                    return WumpusWorldAgent.shoot  # Shoot the Wumpus
                elif direction in turns:
                    action = turns[direction]
                    return self.move(action)  # Move the agent based on the action

    def find_path(self):
        """Find the path to the cave using depth-first search."""
        start, goal = self.agent_location, (1, 1)  # Set the start and goal locations
        rev_cells = {k: v for k, v in self.cells.items() if v["Rev"]}  # Get the cells that have been visited
        visited = set()  # Initialize a set to store visited locations
        def dfs(current):
            if current == goal:
                self.path.append(current)  # Add the current location to the path
                return True
            visited.add(current)  # Add the current location to visited
            x, y = current
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]  # Get the neighboring locations
            for neighbor in neighbors:
                if neighbor in rev_cells and neighbor not in visited:
                    if dfs(neighbor):
                        if current != start:
                            self.path.append(current)  # Add the current location to the path
                        return True
            return False
        dfs(start)  # Start the depth-first search from the start location

    def follow_path(self):
        """Follow the path to the goal."""
        goal = self.path[-1]  # Get the goal location
        locations = self.move('get_locations')
        for direction, (location, turns) in locations.items():
            if location == goal:
                if direction == self.agent_direction:
                    self.path.pop()  # Remove the goal from the path
                    return self.move('forward')  # Move the agent forward
                else:
                    turns = self.move('get_turn')
                    if direction in turns:
                        action = turns[direction]
                        return self.move(action)  # Move the agent based on the action
    
    def explore(self, t):
        """
        Function to explore the environment based on the agent's heuristics.
        """
        locations = self.move('get_locations')  # Get the current locations of the agent
        turns = self.move('get_turn')  # Get the possible turns the agent can make

        directions = {
            'forward': self.agent_direction,  # Direction the agent is currently facing
            'left': next(dir for dir, turn in turns.items() if turn == 'left'),  # Direction to the left of the agent
            'right': next(dir for dir, turn in turns.items() if turn == 'right'),  # Direction to the right of the agent
            'back': next(dir for dir, turn in turns.items() if turn == 'back')  # Direction behind the agent
        }

        env = {dir: self.cells[locations[directions[dir]][0]]["Env"] for dir in directions}  # Get the environment status for each direction

        if t == 0:
            return self.move('forward')  # Move forward if it's the first time step

        # if facing wall, turn right
        if env['forward'] == 'wall':
            return self.move('right')  # Turn right if there's a wall ahead

        # if percept 'Breeze' but 3/4 cells are known not pit, real pit == wall
        for direction in ['forward', 'left', 'right']:
            if env[direction] == 'pit' and all(env[dir] != 'pit' for dir in ['forward', 'left', 'right'] if dir != direction) and env['back'] != 'pit':
                self.cells[locations[directions[direction]][0]]["Env"] = 'wall'  # Mark the pit as a wall if certain conditions are met
                env[direction] = 'wall'  # Update the environment status

        # Check adjacent cells for 'Rev' == False and 'Env' == 'empty'
        for direction in ['forward', 'left', 'right', 'back']:
            if self.cells[locations[directions[direction]][0]]["Rev"] == False and env[direction] == 'empty':
                return self.move(direction)  # Move to the direction if the cell is not revisited and is empty

        return self.move('forward')  # Default move forward if no other conditions are met
    