import roll as Roll
import unittest

class TestDie(unittest.TestCase):
    def setUp(self):
        self.die = Roll.RollableDie()

    def test_upper(self):
        self.assertEqual(self.die.sides, 6)