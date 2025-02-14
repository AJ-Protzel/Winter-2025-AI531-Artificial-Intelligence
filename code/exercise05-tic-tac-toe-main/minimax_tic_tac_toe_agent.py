# MinimaxTicTacToeAgent
# A game-playing tic tac toe agent that uses the minimax algorithm to produce
# a rational action.
# Adrien Protzel


class MinimaxTicTacToeAgent:

    def __init__(self, game, symbol):
        self.game = game
        self.symbol = symbol

    def action(self, state):
        print("Minimax turn!")
        move = self.minimax(self.game, state)
        return move

    def minimax(self, game, state):
        _, move = self.max_value(game, state)
        return move

    def max_value(self, game, state):
        if game.is_terminal(state):
            return game.utility(state, self.symbol), None
        v = float('-inf')
        move = None
        for a in game.actions(state):
            v2, _ = self.min_value(game, game.result(state, a))
            if v2 > v:
                v, move = v2, a
        return v, move

    def min_value(self, game, state):
        if game.is_terminal(state):
            return game.utility(state, self.symbol), None
        v = float('inf')
        move = None
        for a in game.actions(state):
            v2, _ = self.max_value(game, game.result(state, a))
            if v2 < v:
                v, move = v2, a
        return v, move
    