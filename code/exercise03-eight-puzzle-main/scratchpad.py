# Eight Puzzle Agent Scratchpad
# Adrien Protzel
# Use this as a "scratchpad" to tinker with your code.
# There are no rules here, and this code will not be evaluated. This file is a
# place for you to experiment.

from eight_puzzle_agent import EightPuzzleAgent
from eight_puzzle_transition_model import EightPuzzleTransitionModel
from eight_puzzle_problem import EightPuzzleProblem
from eight_puzzle_best_first_search_solver import EightPuzzleBestFirstSearchSolver
from heuristics import (
    heuristic_default,
    heuristic_manhattan,
    heuristic_euclidean,
    heuristic_chebyshev,
    heuristic_octile,
    heuristic_hamming,
    heuristic_misplaced_tiles,
    heuristic_linear_conflict
)

def generate_states(x):
    """
    Generates states for easier inital and goal state change
    """
    states_list = list(range(9)) # Generate a list from 0 to 8
    states_list[x] = None # Replace the element at index x with None
    states = tuple(states_list) # Convert the list to a tuple
    return states


# index for initial, goal, heuristic 
s = 8
g = 0
h = heuristic_default

initial_state = generate_states(s)
goal_state = generate_states(g)
transition_model = EightPuzzleTransitionModel()

problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
solver = EightPuzzleBestFirstSearchSolver(heuristic=h)
agent = EightPuzzleAgent(initial_state, transition_model, solver.solution(problem))

while agent.has_actions():
    action = agent.action()
    action(agent)
