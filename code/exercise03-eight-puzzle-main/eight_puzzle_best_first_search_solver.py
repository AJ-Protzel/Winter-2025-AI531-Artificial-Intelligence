# EightPuzzleBestFirstSearchSolver: A problem solver for the eight-puzzle problem
# that can apply best-first search to find a solution node. This class encapsulates
# a best-first search algorithm and an evaluation function. It encapsulates the
# application of the algorithm to the problem, and in the end can produce a
# solution, which is a list of actions.
# Adrien Protzel

from queue import PriorityQueue
from eight_puzzle_node import EightPuzzleNode

class EightPuzzleBestFirstSearchSolver:

    def solution(self, problem):
        """
        Return a list of EightPuzzleAgent actuator methods. If the problem
        initial state is the same as the goal state, return an empty list.
        """
        solution_node = self.best_first_search(problem, self.cost_so_far_plus_estimated_cost_remaining)
        if solution_node:
            return self.actions_to_reach_solution_node(solution_node)
        else:
            return None

    def best_first_search(self, problem, evaluation_function):
        """
        Return a solution EightPuzzleNode, or None to indicate failure.
        """
        node = EightPuzzleNode(problem.initial_state, None, None, 0)
        frontier = PriorityQueue()
        frontier.put((evaluation_function(node), node))
        reached = {problem.initial_state: node}

        while not frontier.empty():
            _, node = frontier.get()
            if problem.is_goal(node.state):
                return node
            for child in self.expand(problem, node):
                s = child.state
                if s not in reached or child.path_cost < reached[s].path_cost:
                    reached[s] = child
                    frontier.put((evaluation_function(child), child))
        return None

    def expand(self, problem, node):
        """
        Return a list of EightPuzzleNodes that are reachable from `node`.
        """
        s = node.state
        for action in problem.actions(s):
            s_prime = problem.result(s, action)
            cost = node.path_cost + problem.action_cost(s, action, s_prime)
            yield EightPuzzleNode(state=s_prime, parent=node, action=action, path_cost=cost)

    def cost_so_far_plus_estimated_cost_remaining(self, node):
        """
        The evaluation function, f(n) = g(n) + h(n).
        """
        g = node.path_cost
        h = self.heuristic(node.state)
        return g + h
    
    def heuristic(self, state):
        """
        Heuristic function to estimate the cost from the current state to the goal state.
        """
        return 0

    def actions_to_reach_solution_node(self, solution_node):
        """
        Given an EightPuzzleNode goal node, produce a list of in-order actions
        that lead from the initial state to the goal state.
        """
        actions = []
        node = solution_node
        while node.parent is not None:
            actions.append(node.action)
            node = node.parent
        actions.reverse() 
        return actions