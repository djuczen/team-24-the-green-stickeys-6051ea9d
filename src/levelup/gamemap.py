from dataclasses import dataclass
from levelup import Position

@dataclass
class GameMap:
    num_positions: int = 100
    position: list[list[Position]]