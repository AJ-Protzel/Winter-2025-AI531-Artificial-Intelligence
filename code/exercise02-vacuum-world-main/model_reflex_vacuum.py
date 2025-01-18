# ModelReflexVacuum: A robot vacuum cleaner modeled as a model-based reflex agent.
# Your implementation should pass the tests in test_model_reflex_vacuum.py.
# YOUR NAME


class ModelReflexVacuum:

    """
    Initialization
    Attributes
    """

    def __init__(self, state, transition_model, sensor_model):
        self.state = state
        self.transition_model = transition_model
        self.sensor_model = sensor_model
        self.most_recent_action = None

    """
    Actuators
    """

    def suck(self):
        self.transition_model.apply_suction()
        return None
    
    def move_left(self):
        # the README states that move_left should deligate to transition model and call movel_left, however that does not exist in the transition_model.py
        self.transition_model.move_left()
        return None

    def move_right(self):
        # the README states that move_right should deligate to transition model and call movel_right, however that does not exist in the transition_model.py
        self.transition_model.move_right()
        return None
    
    """
    Update state
    """

    def update_state(self):
        if(self.most_recent_action):
            self.most_recent_action()
    
    """
    Agent function
    """

    def action(self):
        self.update_state()

        if(self.sensor_model.sense_dirt()):
            self.most_recent_action = self.suck
        elif(self.sensor_model.sense_location_id() == 'A'):
            self.most_recent_action = self.move_right
        elif(self.sensor_model.sense_location_id() == 'B'):
            self.most_recent_action = self.move_left
        
        return self.most_recent_action
