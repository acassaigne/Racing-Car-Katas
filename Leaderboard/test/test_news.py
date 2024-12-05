import unittest

from leaderboard import Leaderboard, HumanDriver, Race, SelfDrivingCar

# Axes: more drivers / more races / more races and drivers / driver ranking / change driver type
class TestCaracterisation(unittest.TestCase):

    def test_when_no_races_no_driver_points(self):
        l = Leaderboard(races=[])

        self.assertEqual({}, l.driver_points())

    def test_when_winner_of_one_race_gets_25_points(self):
        driver1 = HumanDriver(name="Nico Rosberg", country="DE")
        race1 = Race([driver1])

        l = Leaderboard(races=[race1])

        self.assertEqual({'Nico Rosberg': 25}, l.driver_points())


    def test_displays_driver_points_for_one_race(self):
        driver1 = HumanDriver(name="Driver 1", country="DE")
        driver2 = HumanDriver(name="Driver 2", country="DE")
        driver3 = HumanDriver(name="Driver 3", country="DE")

        race1 = Race([driver1, driver2, driver3])

        l = Leaderboard(races=[race1])

        self.assertEqual({'Driver 1': 25,
                          'Driver 2': 18,
                          'Driver 3': 15}, l.driver_points())


    def test_displays_driver_points_for_multiples_races(self):
        driver1 = HumanDriver(name="Driver 1", country="DE")
        driver2 = HumanDriver(name="Driver 2", country="DE")
        driver3 = HumanDriver(name="Driver 3", country="DE")
        driver4 = HumanDriver(name="Driver 4", country="DE")

        race1 = Race([driver1, driver2, driver3])
        race2 = Race([driver4, driver3, driver1])

        l = Leaderboard(races=[race1, race2])

        self.assertEqual({'Driver 1': 40,
                          'Driver 2': 18,
                          'Driver 3': 33,
                          'Driver 4': 25,
                          }, l.driver_points())

    def test_displays_driver_rankings_for_one_race(self):
        driver1 = HumanDriver(name="Driver 1", country="DE")
        driver2 = HumanDriver(name="Driver 2", country="DE")
        driver3 = HumanDriver(name="Driver 3", country="DE")

        race1 = Race([driver1, driver2, driver3])

        l = Leaderboard(races=[race1])

        self.assertEqual(['Driver 1', 'Driver 2', 'Driver 3'], l.driver_rankings())

    def test_displays_driver_rankings_for_multiples_races(self):
        driver1 = HumanDriver(name="Driver 1", country="DE")
        driver2 = HumanDriver(name="Driver 2", country="DE")
        driver3 = HumanDriver(name="Driver 3", country="DE")
        driver4 = HumanDriver(name="Driver 4", country="DE")

        race1 = Race([driver1, driver2, driver3])
        race2 = Race([driver4, driver3, driver1])

        l = Leaderboard(races=[race1, race2])

        self.assertEqual(['Driver 1', 'Driver 3', 'Driver 4', 'Driver 2'], l.driver_rankings())


    def test_self_driving_car_name_is_display_whit_prefix_company_name_and_version(self):
        driver1 = SelfDrivingCar(algorithm_version="1.2",company="acme")
        race1 = Race([driver1])

        l = Leaderboard(races=[race1])

        self.assertEqual({'Self Driving Car - acme (1.2)': 25}, l.driver_points())