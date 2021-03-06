from board.board import Board
from board.direction import Direction


class Bead3(Board):
  def __init__(self):
    self.structure = [
      [
        [Direction.RIGHT, Direction.BOTTOM_RIGHT, Direction.BOTTOM],
        [Direction.RIGHT, Direction.BOTTOM, Direction.LEFT],
        [Direction.BOTTOM, Direction.BOTTOM_LEFT, Direction.LEFT]
      ],
      [
        [Direction.RIGHT, Direction.BOTTOM, Direction.TOP],
        [Direction.RIGHT, Direction.BOTTOM_RIGHT, Direction.BOTTOM,
         Direction.BOTTOM_LEFT, Direction.LEFT, Direction.TOP_LEFT,
         Direction.TOP, Direction.TOP_RIGHT],
        [Direction.BOTTOM, Direction.LEFT, Direction.TOP]
      ],
      [
        [Direction.RIGHT, Direction.TOP, Direction.TOP_RIGHT],
        [Direction.RIGHT, Direction.LEFT, Direction.TOP],
        [Direction.LEFT, Direction.TOP_LEFT, Direction.TOP]
      ],
    ]
    self.state = [
      [2, 2, 2],
      [0, 0, 0],
      [1, 1, 1],
    ]
    super(Bead3, self).__init__()

  def winner(self):
    for i in range(3):
      # i == 0 and self.board_state[i][0] == 2: Player 2 initial state
      # i == 2 and self.board_state[i][0] == 1: Player 1 initial state
      if not (i == 0 and self.state[i][0] == 2) \
          and not (i == 2 and self.state[i][0] == 1) \
          and self.state[i][0] == self.state[i][1] == \
              self.state[i][2]:
        return self.state[i][0]

      if self.state[0][i] == self.state[1][i] == \
          self.state[2][i]:
        return self.state[0][i]

    if self.state[0][0] == self.state[1][1] == self.state[2][2]:
      return self.state[0][0]

    if self.state[0][2] == self.state[1][1] == self.state[2][0]:
      return self.state[0][2]

    return 0
