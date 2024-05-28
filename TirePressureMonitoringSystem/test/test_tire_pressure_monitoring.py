import unittest

from tire_pressure_monitoring import Alarm


class TestableAlarm(Alarm):

    def __init__(self, sensor):
        super().__init__()
        self._sensor = sensor


class SensorStub:
    def __init__(self, value: int) -> None:
        self._value = value

    def pop_next_pressure_psi_value(self) -> int:
        return self._value


class AlarmTest(unittest.TestCase):

    def test__alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def test__alarm_is_off_when_pressure_between_high_and_low_threshold(self):
        sensor = SensorStub(value=18)
        alarm_test = TestableAlarm(sensor)
        alarm_test.check()
        self.assertFalse(alarm_test.is_alarm_on)

    def test__alarm_is_on_when_pressure_is_lower_than_low_threshold(self):
        sensor = SensorStub(value=16)
        alarm_test = TestableAlarm(sensor)
        alarm_test.check()
        self.assertTrue(alarm_test.is_alarm_on)
