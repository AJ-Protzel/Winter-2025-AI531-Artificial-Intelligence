# SimpleReflexVacuum: A robot vacuum cleaner modeled as a simple reflex agent.
# Your implementation should pass the tests in test_simple_reflex_vacuum.py.
# YOUR NAME

class SimpleReflexVacuum:

    def __init__(self):
        pass

    """
    Actuators
    """

    def suck(self):
        print("Sucked")
        pass

    def move_left(self):
        print("Moved Left")
        pass

    def move_right(self):
        print("Moved Right")
        pass
    
    """
    Agent function
    """

    def action(self, location, dirt):
        if(dirt):
            return self.suck
        # was not sure if the vacuum should still turn after sucking
        elif(location == 'A'):
            return self.move_right
        elif(location == 'B'):
            return self.move_left
