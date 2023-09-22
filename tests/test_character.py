from unittest import TestCase
from levelup.character import Character
from levelup.gamemap import GameMap


class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "WhoDat"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

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
        self.assertNotEqual(None, testobj.game_map)

class TestCharacterGetPositition(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = Character(ARBITRARY_NAME)
        self.assertNotEqual(None, testobj.position)

class TestCharacterMove(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = Character(ARBITRARY_NAME)
        testobj.enter_map(GameMap())
        current_position = testobj.position
        testobj.move("n")
        self.assertNotEqual(current_position,testobj.position)
