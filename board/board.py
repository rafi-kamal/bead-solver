from abc import ABC, abstractmethod
import random

class Board(ABC):
  """
  Attributes:
    board_structure   A 2D list representing the structure of the board. Each
                      (row, col) position contains either `None`, indicating
                      that there can't be any bead in that position, or a list
                      of :class:`Direction`s representing all possible steps
                      you can take from that position (subject to the position
                      of other beads).
    board_state       A 2D list of players indicating which bead in the
                      board belongs to which player.
                      `0` indicates that there is no bead on that position.
                      `1` indicates the first player.
                      `2` indicates the second player.
    current_player    Player whose move is next.
  """
  board_structure = None
  board_state = None
  current_player = 1

  def __init__(self):
    self.__calculate_move_classes()

  @abstractmethod
  def winner(self):
    """
    :return: int  the winner of the game, if the game is finished. Returns 0
    otherwise."""
    pass

  def number_of_move_classes(self):
    """
    :return: int  number of possible moves (e.g. from (0, 0) to (0, 1))
    """
    return len(self.moves)

  def move_to_move_class(self, prev_pos_row, prev_pos_col, next_pos_row,
      next_pos_col):
    """
    :return: int  an integer representation of the move, the value should be
                  within [0, number_of_move_classes).
    """
    return self.move_to_move_class_map[
      (prev_pos_row, prev_pos_col, next_pos_row, next_pos_col)]

  def move_class_to_move(self, move_class):
    """

    :param move_class: int  the integer representation of the move, the value
                            should be within [0, number_of_move_classes)
    :return: tuple          A tuple of (prev_pos_row, prev_pos_col, next_pos_row, next_pos_col), representing the move
    """
    return self.moves[move_class]

  def other_player(self):
    """ Returns the opponent of the current player """
    return 3 - self.current_player

  def move(self, pos_row, pos_col, next_pos_row, next_pos_col):
    self.board_state[next_pos_row][next_pos_col] = self.current_player
    self.board_state[pos_row][pos_col] = 0
    self.current_player = self.other_player()

  def move_random(self):
    bead_positions = self.__get_bead_positions_for_current_player()
    while True:
      prev_pos_row, prev_pos_col = random.choice(bead_positions)
      potential_next_positions = self.get_potential_next_positions(prev_pos_row,
                                                                   prev_pos_col)
      if potential_next_positions:
        next_pos_row, next_pos_col = random.choice(potential_next_positions)
        self.move(prev_pos_row, prev_pos_col, next_pos_row,
                  next_pos_col)
        return

  def get_potential_next_positions(self, row_pos, col_pos):
    potential_next_positions = []
    for move_direction in self.board_structure[row_pos][col_pos]:
      row_delta, col_delta = move_direction.get_direction_delta()
      row = row_pos + row_delta
      col = col_pos + col_delta
      if 0 <= row < len(self.board_state) and 0 <= col < len(
          self.board_state[row]) and self.board_state[row][col] == 0:
        potential_next_positions.append((row, col))
    return potential_next_positions

  def __get_bead_positions_for_current_player(self):
    assert len(self.board_state) > 0 and len(self.board_state[0]) > 0

    bead_positions = []
    for row_pos, row in enumerate(self.board_state):
      for col_pos, col in enumerate(row):
        if col == self.current_player:
          bead_positions.append((row_pos, col_pos))
    return bead_positions

  def __calculate_move_classes(self):
    self.moves = []
    self.move_to_move_class_map = {}
    for row_pos, row in enumerate(self.board_structure):
      for col_pos, directions in enumerate(row):
        for delta_row, delta_col in directions:
          move = (row_pos, col_pos, row_pos + delta_row, col_pos + delta_col)
          self.move_to_move_class_map[move] = len(self.moves)
          self.moves.append(move)

  def __str__(self):
    spacing = 1
    str = '=' * (len(self.board_state) + (len(self.board_state) - 1) * spacing)
    str += '\nNext move: Player {}\n'.format(self.current_player)
    for row in self.board_state:
      for bead in row:
        str += '{}{}'.format(bead, ' ' * spacing)
      str += '\n' * spacing
    return str
