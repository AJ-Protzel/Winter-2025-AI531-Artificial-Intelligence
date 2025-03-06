# WumpusWorldAgent
# An agent designed to perform in the wumpus world environment.


class WumpusWorldAgent:

    def __init__(self, kb):
        self.kb = kb
        self.time = 0

    def action(self, percept):
        # get percepts of current world
        # ask what to do about the current percepts
        # return action
        print("++++++++++++++++++++++++++++")
        print(percept)
        # percept = make_percept_sentence(percept)

        self.kb.tell(percept)
        action = self.kb.ask()
        self.kb.tell(action)
        self.time += 1
        return action
    
    # def action(self, kb):
    #     percept_sentence = self.make_percept_sentence(kb)
    #     self.kb.tell(percept_sentence)
    #     action_query = self.make_action_query()
    #     action_sentence = self.make_action_sentence(action_query)
    #     self.kb.tell(action_sentence)
    #     action = self.kb.ask()
    #     self.time += 1
    #     return action

    # def action(self, percept):
    #     # Increment time
    #     self.time += 1
    #     # Tell the KB the current percept
    #     percept_sentence = self.make_percept_sentence(percept)
    #     self.kb.tell(percept_sentence)
    #     # Ask the KB for the next action
    #     action_query = self.make_action_query()
    #     action = self.kb.ask(action_query)
    #     # Tell the KB the chosen action
    #     action_sentence = self.make_action_sentence(action)
    #     self.kb.tell(action_sentence)
    #     return action

    def make_percept_sentence(self, world):
        # make a string from world.percept
        # pass
        location = world.agent_location
        percept = world.percept(location)
        percept_sentence = f"Cell {location}: {percept}"
        return percept_sentence

    # def make_percept_sentence(self, percept):
    #     # Create a percept sentence based on the percept
    #     return f"Percept: {percept}"

    def make_action_query(self):
        return '?'

    # def make_action_query(self):
    #     # Create an action query
    #     return "What should I do next?"

    def make_action_sentence(self, query):
        # pass
        action = self.kb.ask(query)
        action_sentence = f"Response: {action}"
        return action_sentence

    # def make_action_sentence(self, action):
    #     # Create an action sentence based on the action
    #     return f"Action: {action}"

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
