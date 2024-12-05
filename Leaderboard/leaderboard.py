from abc import ABC, abstractmethod
from collections import defaultdict

# re-intégrer la responsabilité d'accumuler les points pour chaque driver pour l'ensemble des courses
# ajouter une méthode (par exemple) ...
class Leaderboard(object):
    
    def __init__(self, races):
        self.races = races

    def driver_points(self):
        driver_points = defaultdict(int)
        for race in self.races:
            race.scores(driver_points)
        return driver_points

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

# Is it actually Podium?
# When we instanciate a Race with more than 3 drivers, the points method fails
class Race(object):

    _points = [25, 18, 15]

    def __init__(self, results):
        self.results = results
        self.driver_points = defaultdict(int)
        for idx, driver in enumerate(self.results):
            self.driver_points[driver] = Race._points[idx]


    def points(self, driver: Driver):
        return self.driver_points[driver]

    def scores(self, driver_points):
        for driver in self.results:
            driver_points[driver.name()] += self.points(driver)
