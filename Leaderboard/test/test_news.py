import unittest

from leaderboard import Leaderboard, Driver, Race


# Axes: more drivers / more races / more races and drivers / driver ranking / change driver type
class TestCaracterisation(unittest.TestCase):

    def test_when_no_races_no_driver_points(self):
        l = Leaderboard(races=[])

        self.assertEqual({}, l.driver_points())

    def test_when_winner_of_one_race_gets_25_points(self):
        driver1 = Driver(name="Nico Rosberg", country="DE")
        race1 = Race("Australian Grand Prix", [driver1])

        l = Leaderboard(races=[race1])

        self.assertEqual({'Nico Rosberg': 25}, l.driver_points())

    def test_when_winner_of_one_race_gets_25_points_with_a_self_driving_car(self):
        driver1 = Driver(name="Nico Rosberg", country="DE")
        race1 = Race("Australian Grand Prix", [driver1])

        l = Leaderboard(races=[race1])

        self.assertEqual({'Nico Rosberg': 25}, l.driver_points())