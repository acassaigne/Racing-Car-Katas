import unittest

from leaderboard import Leaderboard


class TestCaracterisation(unittest.TestCase):

    def test_when_no_races_no_driver_points(self):
        l = Leaderboard(races=[])

        self.assertEquals({}, l.driver_points())