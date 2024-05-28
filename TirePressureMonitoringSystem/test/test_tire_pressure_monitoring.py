import unittest

from sensor import Sensor
from tire_pressure_monitoring import Alarm

class TestableAlarm(Alarm):

    def __init__(self, sensor):
        super().__init__()
        self._sensor = sensor


class SensorStub:
    pass


class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        assert not alarm.is_alarm_on

    def test__yyy(self):
        sensor = SensorStub()
        alarm_test = TestableAlarm(sensor)
        alarm_test.check()
        assert not alarm_test.is_alarm_on



