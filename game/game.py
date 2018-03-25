from board.board import Board


class Game(object):
  def run(self, board):
    """
    :param board: Board   The board where the game will run
    """
    print('Starting game...\n')
    print(board)
    while board.winner() == 0:
      board.move_random()
      print(board)

    print('Player {} wins!'.format(board.winner()))