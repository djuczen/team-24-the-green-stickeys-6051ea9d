from levelup.position import Position
from levelup.gamemap  import GameMap

class Character:
    name = ""
    game_map = None
    position = None

    def __init__(self, character_name):
        self.name = character_name if character_name != "" else "Cowboy Hank"
        self.position = Position(0,0)

    def enter_map(self, m):
        self.game_map = m
        self.position = m.start_position()

    def move(self,direction):
        current_position = self.position
        new_position = self.game_map.calculate_position(current_position, direction)
        if new_position == current_position:
            raise InvalidMoveException
        else:
            self.position = new_position