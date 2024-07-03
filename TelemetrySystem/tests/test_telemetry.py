import unittest

from telemetry import *

class TelemetryDiagnosticControlsTest(unittest.TestCase):
    def test_foo(self):
        diagnostics = TelemetryDiagnostics()
        # diagnostics.check_transmission()
        self.assertEqual("", diagnostics.diagnostic_info)
        
