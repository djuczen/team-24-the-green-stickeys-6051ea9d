import math
from dataclasses import dataclass
from random import random

from levelup.position import Position
from typing import List

@dataclass
class GameMap:
    num_positions: int = 100
    positions: List[List[Position]] = None

    def __post_init__(self):
        self.grid_size = int(math.sqrt(self.num_positions))
        self.positions = [[Position(x,y) for x in range(0, self.grid_size)] for y in range(0, self.grid_size)]
        print(self.grid_size)

    def calculate_position(self, startpos, movement):
        if movement == 'n':
            return self.positions[startpos.y + 1 if startpos.y < (self.grid_size - 1) else startpos.y][startpos.x]
        elif movement == 's':
            return self.positions[startpos.y - 1 if startpos.y > 0 else startpos.y][startpos.x]
        elif movement == 'e':
            return self.positions[startpos.y][startpos.x + 1 if startpos.x < (self.grid_size - 1) else startpos.x]
        elif movement == 'w':
            return self.positions[startpos.y][startpos.x - 1 if startpos.x > 0 else startpos.x]
        else :
            return self.positions[startpos.y][startpos.x]

    def start_position(self):
        startposy = (int(random() * (self.grid_size - 1)))
        startposx = (int(random() * (self.grid_size - 1)))
        return self.positions[startposy][startposx]