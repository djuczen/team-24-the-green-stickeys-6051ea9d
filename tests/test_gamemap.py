from unittest import TestCase
from levelup.position import Position
from levelup.gamemap import GameMap


class TestTotalPositions(TestCase):
    def test_init(self):
        num_positions = 100
        testobj = GameMap(num_positions)
        self.assertEqual(num_positions, testobj.num_positions)

#test for 100 positions
#calculate position based on direction entered
#valid position?
