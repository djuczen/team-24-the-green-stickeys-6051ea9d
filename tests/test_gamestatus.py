from unittest import TestCase
from levelup.character import Character
from levelup.controller import GameStatus
from levelup.position import Position

class TestCharacterNamein(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = GameStatus(character_name=ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.character_name)
        self.assertEqual((None), testobj.current_position)
        self.assertEqual(0,testobj.move_count)


