import math
from dataclasses import dataclass
from levelup.position import Position
from typing import List

@dataclass
class GameMap:
    num_positions: int = 100
    positions: List[List[Position]] = None

    def __post_init__(self):
        grid_size = int(math.sqrt(self.num_positions))
        self.positions = [[Position(x,y) for x in range(grid_size)] for y in range(grid_size)]

    def calculate_position(self, startpos, movement):
        grid_size = int(math.sqrt(self.num_positions))
        if movement == 'n':
            return self.positions[startpos.y + 1 if startpos.y < grid_size else startpos.y][startpos.x]
        elif movement == 's':
            return self.positions[startpos.y - 1 if startpos.y > 0 else startpos.y][startpos.x]
        elif movement == 'e':
            return self.positions[startpos.y][startpos.x + 1 if startpos.x < grid_size else startpos.x]
        elif movement == 'w':
            return self.positions[startpos.y][startpos.x - 1 if startpos.x > 0 else startpos.x]
        else :
            return self.positions[startpos.y][startpos.x]