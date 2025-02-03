# Main
# Adrien Protzel
# Demonstrate the use of your EightPuzzleAgent.

import random
import time
from eight_puzzle_agent import EightPuzzleAgent
from eight_puzzle_transition_model import EightPuzzleTransitionModel
from eight_puzzle_problem import EightPuzzleProblem
from eight_puzzle_best_first_search_solver import EightPuzzleBestFirstSearchSolver

random.seed(9)

def rand_state():
    elements = [1, 2, 3, 4, 5, 6, 7, 8, None]
    random.shuffle(elements)
    return tuple(elements)

initial_states = [
    (7, 2, 4, 5, None, 6, 8, 3, 1),
    (8, None, 6, 5, 4, 7, 2, 3, 1),
    (8, 6, 7, 2, 5, 4, 3, None, 1),
    (6, 4, 7, 8, 5, None, 3, 2, 1),
    rand_state(),
    rand_state(),
    rand_state(),
    rand_state(),
]

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, None)
total_time = 0

for initial_state in initial_states:
    print(f"Test {initial_states.index(initial_state) + 1} = {initial_state}")
    # print(f"initial_state = {initial_state}")

    start_time = time.time()
    transition_model = EightPuzzleTransitionModel()
    problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
    solver = EightPuzzleBestFirstSearchSolver(goal_state)
    agent = EightPuzzleAgent(initial_state, transition_model, solver.solution(problem))
    
    while agent.has_actions():
        action = agent.action()
        action(agent)
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    total_time += elapsed_time
    
    print(f"Finish: {elapsed_time} seconds")

average_time = total_time / len(initial_states)
print(f"\nAverage time to finish: {average_time} seconds\n")
