import unittest

from tire_pressure_monitoring import Alarm

class AlarmTest(Alarm):

    def __init__(self):
        super().__init__()

class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        assert not alarm.is_alarm_on

    def test__yyy(self):
        alarm_test = AlarmTest()
        assert not alarm_test.is_alarm_on



