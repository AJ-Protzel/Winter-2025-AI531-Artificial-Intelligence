# EightPuzzleAgent: A goal-based agent that emits the actions from a solution to
# an "eight puzzle" problem.
# Your implementation should pass the tests in test_eight_puzzle_agent.py.
# YOUR NAME


class EightPuzzleAgent:

    def __init__(self, initial_state, transition_model, actions):
        self.current_state = initial_state
        self.transition_model = transition_model
        self.actions = actions

    def has_actions(self):
        """ Return `True` when `self.actions` is not empty """
        pass

    def action(self):
        """ Return the next action in `self.actions` """
        pass

    def move_left(self):
        """
        Print "Left" as a side effect, and update `self.current_state`. Use the
        EightPuzzleTransitionModel stored in `self.transition_model` to obtain
        the new state to assign to `self.current_state`.
        """
        pass

    def move_right(self):
        """
        Print "Right" as a side effect, and update `self.current_state`. Use the
        EightPuzzleTransitionModel stored in `self.transition_model` to obtain
        the new state to assign to `self.current_state`.
        """
        pass

    def move_up(self):
        """
        Print "Up" as a side effect, and update `self.current_state`. Use the
        EightPuzzleTransitionModel stored in `self.transition_model` to obtain
        the new state to assign to `self.current_state`.
        """
        pass

    def move_down(self):
        """
        Print "Down" as a side effect, and update `self.current_state`. Use the
        EightPuzzleTransitionModel stored in `self.transition_model` to obtain
        the new state to assign to `self.current_state`.
        """
        pass
