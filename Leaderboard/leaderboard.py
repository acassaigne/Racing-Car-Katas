from collections import defaultdict


class Leaderboard(object):
    
    def __init__(self, races):
        self.races = races

    def driver_points(self):
        driver_points = defaultdict(int)
        for race in self.races:
            for driver in race.results:
                name = driver.name2()
                driver_points[name] += race.points(driver)
        return driver_points

    def driver_rankings(self):
        rankings = sorted(self.driver_points().items(), key=lambda x: x[1], reverse=True)
        return [name for (name, points) in rankings]


class Driver(object):
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def name2(self):
        return self.name

class SelfDrivingCar(Driver):
    def __init__(self, algorithm_version, company):
        Driver.__init__(self, None, company)
        self.algorithm_version = algorithm_version

    def name2(self):
        return "Self Driving Car - {} ({})".format(self.country, self.algorithm_version)

# Is it actually Podium?
# When we instanciate a Race with more than 3 drivers, the points method fails
class Race(object):

    _points = [25, 18, 15]

    def __init__(self, results):
        self.results = results

    def points(self, driver):
        return Race._points[self.results.index(driver)]
