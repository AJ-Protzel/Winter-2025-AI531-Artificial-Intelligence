# KnowledgeBase
# A knowledge base for a knowledge-based agent.

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:

    def __init__(self, agent_location, agent_direction):
        self.facts = []
        self.rules = {}
        self.agent_location = agent_location
        self.agent_direction = agent_direction


#  need to change facts to just array appending action
    def tell(self, info):
        if isinstance(info, str):
            self.facts.append(info)
        else:


            x, y = self.agent_location
            directions = {
                "North": (x, y + 1),
                "South": (x, y - 1),
                "East": (x + 1, y),
                "West": (x - 1, y)
            }

            # if self.agent_location not in self.facts:
            #     self.facts[self.agent_location] = 0

            # if self.agent_location == (1,1):
            #     self.facts[self.agent_location] = 0.1

            # for direction in directions.values():
            #     if direction not in self.rules and direction not in self.facts:
            #         self.rules[direction] = 0
            
            # for i in info:
            #     if i == 'Stench':
            #         for direction in directions.values():
            #             if direction not in self.facts:
            #                 self.rules[direction] = -1.1

            #     elif i == 'Breeze':
            #         for direction in directions.values():
            #             if direction not in self.facts:
            #                 self.rules[direction] = self.rules.get(direction, 0) - 10

            #     elif i == 'Glitter':
            #         self.facts[self.agent_location] = 10

            #     elif i == 'Bump':
            #         self.rules[directions[self.agent_direction]] = -100
               
    def ask(self, query):
        if query is None:
            return WumpusWorldAgent.turn_left
        else:
            return self.find_action()
    
    def find_action(self):
        score = self.facts[self.agent_location]
        room = "Room"
        
        x, y = self.agent_location
        rooms = {
            "Room": (x, y),
            "North": (x, y + 1),
            "South": (x, y - 1),
            "East": (x + 1, y),
            "West": (x - 1, y)
        }

        for direction, coord in rooms:
            if coord in self.rules:
                if self.rules[coord] > score:
                    score = self.rules[coord]
                    room = direction

        if room == "Room":
            if score % 1 == 0.1 and any("grabbed" in fact for fact in self.facts):
                return WumpusWorldAgent.climb
            else:
                return WumpusWorldAgent.grab
        else:
            directions = ["North", "East", "South", "West"]

            current_index = directions.index(self.agent_direction)
            target_index = directions.index(room)

            if self.agent_direction != room:
                if (current_index - target_index) % 4 == 2 or (target_index - current_index) % 4 != 1:
                    return WumpusWorldAgent.turn_left
                return WumpusWorldAgent.turn_right

            if room == self.agent_direction:
                if score > 0:
                    return WumpusWorldAgent.move_forward
                elif score % 1 == 0.1:
                    return WumpusWorldAgent.shoot
