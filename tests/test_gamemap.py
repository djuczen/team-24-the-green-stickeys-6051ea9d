from unittest import TestCase
from levelup.character import Character
from levelup.gamemap import GameMap


class TestGetPositions(TestCase):
    def test_init(self):
        num_positions = 100
        testobj = Position(num_positions)
        self.assertNotEqual(None, testobj.map)

#test for 100 positions
#calculate position based on direction entered
#valid position?

class TestCharacterInitWithoutName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = Character(ARBITRARY_NAME)
        self.assertNotEqual(ARBITRARY_NAME, testobj.name)


class TestCharacterEnterMap(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = Character(ARBITRARY_NAME)
        testobj.enter_map(GameMap())
        self.assertNotEqual(None, testobj.map)
