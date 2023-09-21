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
#test for 100 positions
#calculate position based on direction entered
#valid position?
