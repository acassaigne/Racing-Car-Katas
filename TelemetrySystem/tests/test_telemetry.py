import unittest

from telemetry import *

class StubAlwaysOfflineClient:
    def __init__(self):
        self.online_status = False

    def disconnect(self):
        pass

    def connect(self, channel):
        pass


class TelemetryDiagnosticControlsTest(unittest.TestCase):
    def test_foo(self):
        diagnostics = TelemetryDiagnostics(StubAlwaysOfflineClient())
        with self.assertRaisesRegex(Exception, "^Unable to connect\.$"):
            diagnostics.check_transmission()

        # self.assertEqual("", diagnostics.diagnostic_info)
        
