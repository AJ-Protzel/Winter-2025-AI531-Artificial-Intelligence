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
        return (f"Turn {t} P: {percept}")

    def make_action_query(self, t):
        return ("?")

    def make_action_sentence(self, action, t):
        return (f"Turn {t} A: {action}")

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
