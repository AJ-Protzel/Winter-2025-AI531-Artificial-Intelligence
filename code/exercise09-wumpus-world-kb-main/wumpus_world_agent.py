# WumpusWorldAgent
# An agent designed to perform in the wumpus world environment.

class WumpusWorldAgent:

    def __init__(self, kb):
        self.kb = kb
        self.time = 0

    def action(self, percept):
        self.kb.tell(self.make_percept_sentence(percept, self.time))
        action = self.kb.ask(self.make_action_query(self.time))
        self.kb.tell(self.make_action_sentence(action, self.time))
        self.time += 1
        return action

    def make_percept_sentence(self, percept, t):
        return percept

    def make_action_query(self, t):
        return t

    def make_action_sentence(self, action, t):
        return action.__name__

    def turn_left(self, world):
        world.turned_left()

    def turn_right(self, world):
        world.turned_right()

    def move_forward(self, world):
        world.moved_forward()

    def grab(self, world):
        world.grabbed()

    def climb(self, world):
        world.climbed()

    def shoot(self, world):
        world.shot()
    
    def sit(self, world):
        world.sat()
