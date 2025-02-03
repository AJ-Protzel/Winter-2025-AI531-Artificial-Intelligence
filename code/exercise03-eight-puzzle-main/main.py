# Main
# Adrien Protzel
# Demonstrate the use of your EightPuzzleAgent.

import random
import time
import inspect
import heuristics
from eight_puzzle_agent import EightPuzzleAgent
from eight_puzzle_transition_model import EightPuzzleTransitionModel
from eight_puzzle_problem import EightPuzzleProblem
from eight_puzzle_best_first_search_solver import EightPuzzleBestFirstSearchSolver

random.seed(9)
# Dynamically load all heuristic functions from heuristics.py
heuristics_list = [func for _, func in inspect.getmembers(heuristics, inspect.isfunction)]

def generate_states(x):
    """
    Generates states for easier initial and goal state change.
    """
    states_list = list(range(9))  # Generate a list from 0 to 8
    states_list[x] = None  # Replace the element at index x with None
    states = tuple(states_list)  # Convert the list to a tuple
    return states

# Generate initial and goal states for test (uniform states for each heuristic)
initial_states = [generate_states(random.randint(0, 8)) for _ in range(4)]
goal_states = [generate_states(random.randint(0, 8)) for _ in range(4)]

for h in heuristics_list:
    print(f"Using heuristic: {h.__name__}")
    
    total_time = 0
    
    for i in range(4):
        initial_state = initial_states[i]
        goal_state = goal_states[i]

        print(f"Test {i+1}")
        print(f"initial_state = {initial_state}")
        print(f"goal_state = {goal_state}")

        transition_model = EightPuzzleTransitionModel()
        problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
        solver = EightPuzzleBestFirstSearchSolver(heuristic = h)
        
        start_time = time.time()
        
        agent = EightPuzzleAgent(initial_state, transition_model, solver.solution(problem))
        
        while agent.has_actions():
            action = agent.action()
            action(agent)
        
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        total_time += elapsed_time
        
        print(f"Time to finish: {elapsed_time} seconds")
    
    average_time = total_time / 4
    print(f"Average time to finish for {h.__name__}: {average_time} seconds\n")
