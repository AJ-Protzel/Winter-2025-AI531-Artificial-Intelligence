# Main
# Adrien Protzel
# Demonstrate the use of your EightPuzzleAgent.


# If Print statements are missing, 
# the print statements in EightPuzzleAgent were commented out for testing purposes
# and forgotten to turn back on before submitting


import time
from eight_puzzle_agent import EightPuzzleAgent
from eight_puzzle_transition_model import EightPuzzleTransitionModel
from eight_puzzle_problem import EightPuzzleProblem
from eight_puzzle_best_first_search_solver import EightPuzzleBestFirstSearchSolver

initial_state = (None, 1, 2, 3, 4, 5, 6, 7, 8)
goal_states = [
    (7, 2, 4, 5, None, 6, 8, 3, 1),
    (8, None, 6, 5, 4, 7, 2, 3, 1),
    (8, 6, 7, 2, 5, 4, 3, None, 1),
    (6, 4, 7, 8, 5, None, 3, 2, 1)
]

total_time = 0

for i in range(4):
    goal_state = goal_states[i]

    print(f"Test {i+1}")
    print(f"initial_state = {initial_state}")
    print(f"goal_state = {goal_state}")

    transition_model = EightPuzzleTransitionModel()
    problem = EightPuzzleProblem(initial_state, goal_state, transition_model)
    solver = EightPuzzleBestFirstSearchSolver()
    
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
print(f"\nAverage time to finish: {average_time} seconds\n")
