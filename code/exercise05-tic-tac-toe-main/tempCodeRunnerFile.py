from tic_tac_toe_game import TicTacToeGame
from tic_tac_toe_board_renderer import TicTacToeBoardRenderer
from minimax_tic_tac_toe_agent import MinimaxTicTacToeAgent
from human_tic_tac_toe_agent import HumanTicTacToeAgent
from random_tic_tac_toe_agent import RandomTicTacToeAgent

renderer = TicTacToeBoardRenderer()
game = TicTacToeGame((None, None, None, None, None, None, None, None, None), renderer)
# human_agent = HumanTicTacToeAgent(game, TicTacToeGame.P1_SYMBOL)
# human_agent = RandomTicTacToeAgent(game, TicTacToeGame.P1_SYMBOL)
# ai_agent = MinimaxTicTacToeAgent(game, TicTacToeGame.P2_SYMBOL)

# game = TicTacToeGame((None, None, None, None, None, None, None, None, None), None)
ai_agent = MinimaxTicTacToeAgent(game, 'X')
human_agent = RandomTicTacToeAgent(game, TicTacToeGame.P1_SYMBOL)

state = ('X', None, None, None, None, None, None, None, None)
move = ai_agent.action(state)
print(f"Chosen move: {move}")