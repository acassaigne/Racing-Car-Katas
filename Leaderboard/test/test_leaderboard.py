import unittest

from leaderboard import *

# # Test Data found via http://en.wikipedia.org/wiki/2015_Formula_One_season
# driver1 = Driver(name="Nico Rosberg", country="DE")
# driver2 = Driver(name="Lewis Hamilton", country="UK")
# driver3 = Driver(name="Sebastian Vettel", country="DE")
# driver4 = SelfDrivingCar(algorithm_version = "1.2", company="Acme")
#
# race1 = Race("Australian Grand Prix", [driver1, driver2, driver3])
# race2 = Race("Malaysian Grand Prix", [driver3, driver2, driver1])
# race3 = Race("Chinese Grand Prix", [driver2, driver1, driver3])
# race4 = Race("Fictional Grand Prix", [driver1, driver2, driver4])
# race5 = Race("Fictional Grand Prix", [driver4, driver2, driver1])
# driver4.algorithm_version = "1.3"
# race6 = Race("Fictional Grand Prix", [driver2, driver1, driver4])
#
# sample_leaderboard1 = Leaderboard(races=[race1, race2, race3])
# sample_leaderboard2 = Leaderboard(races=[race4, race5, race6])

## TODO: Ensure we are not breaking the behavior with changing the self driving car algorithm
## TODO: Add tests on race
## TODO: Add tests on Leadearboard to allow for refacto (test paramétrés ?)
## TODO: Refacto

class LeaderboardTest(unittest.TestCase):

    def test_winner(self):
        driver1 = HumanDriver(name="Nico Rosberg", country="DE")
        driver2 = HumanDriver(name="Lewis Hamilton", country="UK")
        driver3 = HumanDriver(name="Sebastian Vettel", country="DE")
        driver4 = SelfDrivingCar(algorithm_version="1.2", company="Acme")

        race1 = Race([driver1, driver2, driver3])
        race2 = Race([driver3, driver2, driver1])
        race3 = Race([driver2, driver1, driver3])
        driver4.algorithm_version = "1.3"

        sample_leaderboard1 = Leaderboard(races=[race1, race2, race3])

        self.assertEqual("Lewis Hamilton", sample_leaderboard1.driver_rankings()[0])

    def test_driver_points(self):
        driver1 = HumanDriver(name="Nico Rosberg", country="DE")
        driver2 = HumanDriver(name="Lewis Hamilton", country="UK")
        driver3 = HumanDriver(name="Sebastian Vettel", country="DE")
        driver4 = SelfDrivingCar(algorithm_version="1.2", company="Acme")

        race1 = Race([driver1, driver2, driver3])
        race2 = Race([driver3, driver2, driver1])
        race3 = Race([driver2, driver1, driver3])
        driver4.algorithm_version = "1.3"

        sample_leaderboard1 = Leaderboard(races=[race1, race2, race3])

        self.assertEqual(18+18+25, sample_leaderboard1.driver_points()["Lewis Hamilton"])

    def test_winner_self_driving_car(self):
        driver4 = SelfDrivingCar(algorithm_version="1.2", company="Acme")

        race3 = Race([driver4])

        sample_leaderboard1 = Leaderboard(races=[race3])

        self.assertEqual("Self Driving Car - Acme (1.2)", sample_leaderboard1.driver_rankings()[0])



    @unittest.skip("will be back, maybe")
    def test_AA(self):
        driver1 = HumanDriver(name="A", country="DE")
        driver2 = HumanDriver(name="A", country="DE")

        d = {}
        d[driver1] = driver1.name

        d[driver2] = driver2.name

        self.assertEqual({driver1:"A"}, d)

class RaceTest(unittest.TestCase):

    def test_driver_points(self):
        driver1 = HumanDriver(name="Nico Rosberg", country="DE")
        driver2 = HumanDriver(name="Lewis Hamilton", country="UK")
        driver3 = HumanDriver(name="Sebastian Vettel", country="DE")
        driver4 = SelfDrivingCar(algorithm_version="1.2", company="Acme")

        race1 = Race([driver1, driver2, driver3])
        driver4.algorithm_version = "1.3"

        self.assertEqual(25, race1.points(driver1))
        self.assertEqual(18, race1.points(driver2))
        self.assertEqual(15, race1.points(driver3))

if __name__ == "__main__":
    unittest.main()