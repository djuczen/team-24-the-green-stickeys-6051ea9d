from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.position import Position


class TestTotalPositions(TestCase):
    def test_init(self):
        num_positions = 100
        testobj = GameMap(num_positions)
        self.assertEqual(num_positions, testobj.num_positions)

class TestPositions(TestCase):
    def test_init(self):
        testobj = GameMap(100)
        self.assertNotEqual(None, testobj.positions)

class TestCalculatePositionBasedOnDirection(TestCase):
    def test_init(self):
        testobj = GameMap(100)
        direction = 'n'
        startpos = testobj.positions[4][5]
        endpos = testobj.calculate_position(startpos, direction)
        self.assertEquals(endpos.x , 5)
        self.assertEquals(endpos.y , 5)

class TestWalls(TestCase):
    def test_init(self):
        testobj = GameMap(100)
        direction = 'e'
        startpos = testobj.positions[4][9]
        endpos = testobj.calculate_position(startpos, direction)
        self.assertEquals(endpos.y, 4)
        self.assertEquals(endpos.x , 9)
