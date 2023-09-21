import math
from dataclasses import dataclass
from levelup.position import Position

@dataclass
class GameMap:
    num_positions: int = 100
    positions: list[list[Position]] = None

    def __post_init__(self):
        grid_size = int(math.sqrt(self.num_positions))
        self.positions = [[Position(x,y) for x in range(grid_size)] for y in range(grid_size)]
