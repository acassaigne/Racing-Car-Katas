from abc import ABC, abstractmethod
from collections import defaultdict

class Leaderboard(object):
    
    def __init__(self, races):
        self.races = races
        self._driver_points = defaultdict(int)
        for race in self.races:
            race.race_add_scores(self)


    def driver_points(self):
        return self._driver_points

    def add_points_to(self, driver, points):
        self._driver_points[driver.name()] += points


    def driver_rankings(self):
        rankings = sorted(self.driver_points().items(), key=lambda x: x[1], reverse=True)
        return [name for (name, points) in rankings]

class Driver(ABC):
    @abstractmethod
    def name(self):
        pass

class HumanDriver(Driver):
    def __init__(self, name, country):
        self._name = name
        self._country = country

    def name(self):
        return self._name

class SelfDrivingCar(Driver):
    def __init__(self, algorithm_version, company):
        self._algorithm_version = algorithm_version
        self._company = company

    def name(self):
        return "Self Driving Car - {} ({})".format(self._company, self._algorithm_version)

class Race(object):

    _reference_score = [25, 18, 15]

    def __init__(self, results):
        self.results = results
        self.driver_points = defaultdict(int)
        for idx, driver in enumerate(self.results):
            self.driver_points[driver] = Race._reference_score[idx]


    def _points(self, driver: Driver):
        return self.driver_points[driver]

    def race_add_scores(self, leaderboard: Leaderboard):
        for driver in self.results:
            leaderboard.add_points_to(driver=driver, points=self._points(driver) )
