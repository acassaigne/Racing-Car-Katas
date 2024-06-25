import unittest

from turn_ticket import TicketDispenser, TurnTicket


class TicketDispenserTest(unittest.TestCase):

    def test_do_something(self):
        dispenser = TicketDispenser()
        ticket = dispenser.getTurnTicket()
        self.assertEqual(TurnTicket(0), ticket)

    def test_equal(self):
        self.assertEqual(TurnTicket(1), TurnTicket(1))

    def test_str(self):
        self.assertEqual("a", str(TurnTicket(0)))
