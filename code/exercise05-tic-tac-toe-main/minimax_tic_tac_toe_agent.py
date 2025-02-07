# MinimaxTicTacToeAgent
# A game-playing tic tac toe agent that uses the minimax algorithm to produce
# a rational action.
# Adrien Protzel


class MinimaxTicTacToeAgent:

    def __init__(self, game, symbol):
        self.game = game
        self.symbol = symbol

    def action(self, state):
        pass

    def minimax(self, game, state):
    #     player = game.to_move(state)
    #     value, move = self.max_value(game, state)
    #     return move
        player = game.to_move(state)
        if player == self.symbol:
            value, move = self.max_value(game, state)
        else:
            value, move = self.min_value(game, state)
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


    # def minimax(self, game, state):
    #     player = game.to_move(state)
    #     if player == self.symbol:
    #         value, move = self.max_value(game, state)
    #     else:
    #         value, move = self.min_value(game, state)
    #     return move

    # def max_value(self, game, state):
    #     if game.is_terminal(state):
    #         return game.utility(state, self.symbol), None
    #     v = float('-inf')
    #     move = None
    #     for a in game.actions(state):
    #         v2, _ = self.min_value(game, game.result(state, a))
    #         if v2 > v:
    #             v, move = v2, a
    #     return v, move

    # def min_value(self, game, state):
    #     if game.is_terminal(state):
    #         return game.utility(state, self.symbol), None
    #     v = float('inf')
    #     move = None
    #     for a in game.actions(state):
    #         v2, _ = self.max_value(game, game.result(state, a))
    #         if v2 < v:
    #             v, move = v2, a
    #     return v, move
    


    # # def minimax(self, game, state):
    # #     player = game.to-move(state)
    # #     value, move = max-value(game, state)
    # #     return move

    # # def max_value(self, game, state):
    # #     if(game.is-terminal(state)):
    # #         return game.utility(state, player), null
    # #     v = -infinity
    # #     for(a in game.actions(satte)):
    # #     v2, a2 = min-value(game, game.reasult(state, a))
    # #     if(v2 > v):
    # #         v, move = v2, a
    # #     return v, move

    # # def min_value(self, game, state):
    # #     if(game.is-terminal(state)):
    # #         return game.utility(state, player), null
    # #     v = infinity
    # #     for(a in game.actions(state));
    # #     v2, a2 = min-value(game, game.reasult(state, a))
    # #     if(v2 < v):
    # #         v, move = v2, a
    # #     return v, move