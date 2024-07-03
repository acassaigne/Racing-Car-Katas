import unittest

from telemetry import *

class StubAlwaysOfflineClient:
    def __init__(self):
        self.online_status = False

    def disconnect(self):
        pass

    def connect(self, channel):
        pass


class StubReceivingClient:
    def __init__(self):
        self.online_status = True
        self.message_receive = ""

    def disconnect(self):
        pass

    def connect(self, channel):
        pass

    def send(self, message):
        self.message_receive = message

    def receive(self):
        return self.message_receive

class TelemetryDiagnosticControlsTest(unittest.TestCase):
    def test_never_able_to_connect(self):
        diagnostics = TelemetryDiagnostics(StubAlwaysOfflineClient())
        with self.assertRaisesRegex(Exception, "^Unable to connect\.$"):
            diagnostics.check_transmission()

    def test__bb(self):
        stub = StubReceivingClient()
        diagnostics = TelemetryDiagnostics(stub)
        diagnostics.check_transmission()
        self.assertEqual("AT#UD", diagnostics.diagnostic_info)

#TODO: stub plus compliqué pour le retry