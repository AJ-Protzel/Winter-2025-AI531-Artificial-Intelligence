# WumpusWorldAgent
# An agent designed to perform in the wumpus world environment.


class WumpusWorldAgent:

    def __init__(self, kb, time=0):
        self.kb = kb
        self.time = time

    def action(self, kb):
        self.kb.tell(kb)
        action = self.kb.ask()
        self.kb.tell(action)
        self.time += 1
        return action

    def make_percept_sentence(self, percept):
        # call world percept to get tuple
        # make string from tuple and world variables like agent location
        # send string to knowledgebase tell
        pass

    def make_action_query(self):
        # call knowledgebase ask based on world agent location
        # call make action sentance with return from ask()
        pass

    def make_action_sentence(self, query):
        pass

    def turn_left(self, world):
        print("Turning Left")
        world.turned_left()

    def turn_right(self, world):
        print("Turning Right")
        world.turned_right()

    def move_forward(self, world):
        print("Moving Forward")
        world.moved_forward()

    def grab(self, world):
        print("Grabbing")
        world.grabbed()

    def climb(self, world):
        print("Climbing")
        world.climbed()

    def shoot(self, world):
        print("Shooting")
        world.shot()
