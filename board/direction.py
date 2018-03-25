from enum import Enum, unique


@unique
class Direction(Enum):
  LEFT = 0
  RIGHT = 1
  TOP = 2
  BOTTOM = 3
  TOP_LEFT = 4
  TOP_RIGHT = 5
  BOTTOM_LEFT = 6
  BOTTOM_RIGHT = 7
  LEFT_2 = 8
  RIGHT_2 = 9


  def get_direction_delta(self):
    if self is Direction.LEFT:
      return 0, -1
    elif self is Direction.RIGHT:
      return 0, 1
    elif self is Direction.TOP:
      return -1, 0
    elif self is Direction.BOTTOM:
      return 1, 0
    elif self is Direction.TOP_LEFT:
      return -1, -1
    elif self is Direction.TOP_RIGHT:
      return -1, 1
    elif self is Direction.BOTTOM_LEFT:
      return 1, -1
    elif self is Direction.BOTTOM_RIGHT:
      return 1, 1
    elif self is Direction.LEFT_2:
      return 0, -2
    elif self is Direction.RIGHT_2:
      return 0, 2
