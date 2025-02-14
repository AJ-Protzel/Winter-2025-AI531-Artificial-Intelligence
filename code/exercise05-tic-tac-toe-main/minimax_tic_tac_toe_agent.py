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
        # valid_moves = [i for i in range(len(state)) if state[i] is None]
        # if valid_moves:
        #     if self.game is None:
        #         return valid_moves[0]
        #     move = self.minimax(self.game, state)
        #     return move
        # else:
        #     return None
        # # invodce minimax and return moves
        move = self.minimax(self.game, state)
        return move

    def minimax(self, game, state):
    #     player = game.to_move(state)
    #     if player == self.symbol:
    #         _, move = self.max_value(game, state)
    #     else:
    #         _, move = self.min_value(game, state)
    #     return move
    # # always start on max
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
    