import unittest

import pytest

from leaderboard import Leaderboard, Driver, Race, SelfDrivingCar


@pytest.mark.parametrize("a,b", [("hello", "salut"),
                                 ("foo", "bar")])
def test_u(a, b):
    assert a == b


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

    def test_self_driving_car_name_is_display_whit_prefix_company_name_and_version(self):
        driver1 = SelfDrivingCar(algorithm_version="1.2",company="acme")
        race1 = Race("Australian Grand Prix", [driver1])

        l = Leaderboard(races=[race1])

        self.assertEqual({'Self Driving Car - acme (1.2)': 25}, l.driver_points())