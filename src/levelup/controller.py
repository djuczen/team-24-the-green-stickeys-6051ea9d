import logging
from dataclasses import dataclass
from enum import Enum

from levelup.character import Character
from levelup.gamemap import GameMap
from levelup.position import Position

DEFAULT_CHARACTER_NAME = "Cowboy Hank"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: Position = None
    move_count: int = 0

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:


    status: GameStatus

    def __init__(self):
        self.character: Character = None
        self.game_map: GameMap = None
        self.status = GameStatus()

    def start_game(self):
        self.game_map = GameMap()
        self.status.current_position = self.game_map.start_position()
        self.set_character_position(self.status.current_position)
        self.character.enter_map(self.game_map)

    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.status.character_name = character_name
        else:
            self.status.character_name = DEFAULT_CHARACTER_NAME
        self.character = Character(self.status.character_name)


    def move(self, direction: Direction) -> None:
        self.character.move(direction)
        # TODO: Implement move - should call something on another class
        # TODO: Should probably also update the game results
        pass

    def set_character_position(self, position: Position) -> None:
        self.character.position = position

    def set_current_move_count(self, move_count: int) -> None:
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        pass

    def get_total_positions(self) -> int:
        return self.game_map.num_positions


    
