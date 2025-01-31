# EightPuzzleBestFirstSearchSolver: A problem solver for the eight-puzzle problem
# that can apply best-first search to find a solution node. This class encapsulates
# a best-first search algorithm and an evaluation function. It encapsulates the
# application of the algorithm to the problem, and in the end can produce a
# solution, which is a list of actions.
# YOUR NAME


from queue import PriorityQueue
from eight_puzzle_node import EightPuzzleNode

class EightPuzzleBestFirstSearchSolver:

    def solution(self, problem):
        """
        Return a list of EightPuzzleAgent actuator methods. If the problem
        initial state is the same as the goal state, return an empty list.
        """
        solution_node = self.best_first_search(problem,
            self.cost_so_far_plus_estimated_cost_remaining)
        if solution_node:
            return actions_to_reach_solution_node(solution_node)
        else:
            return None

    def best_first_search(self, problem, evaluation_function):
        """
        Return a solution EightPuzzleNode, or None to indicate failure.
        """
        pass

    def expand(self, problem, node):
        """
        Return a list of EightPuzzleNodes that are reachable from `node`.
        """
        return []

    def cost_so_far_plus_estimated_cost_remaining(self, node):
        """
        The evaluation function, f(n) = g(n) + h(n).
        """
        pass

    def actions_to_reach_solution_node(self, solution_node):
        """
        Given an EightPuzzleNode goal node, produce a list of in-order actions
        that lead from the initial state to the goal state.
        """
        return []
