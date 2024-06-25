import unittest

from turn_ticket import TicketDispenser, TurnTicket


class TicketDispenserTest(unittest.TestCase):

    def test_do_something(self):
        dispenser = TicketDispenser()
        ticket = dispenser.getTurnTicket()
        self.assertEqual(TurnTicket(0), ticket)

    @unittest.skip("Doesn't work because of static")
    def test_do_somethingAA(self):
        dispenser1 = TicketDispenser()
        dispenser2 = TicketDispenser()
        ticket0 = dispenser1.getTurnTicket()
        ticket1 = dispenser1.getTurnTicket()
        ticket2 = dispenser2.getTurnTicket()
        self.assertEqual(TurnTicket(0), ticket0)
        self.assertEqual(TurnTicket(1), ticket1)
        self.assertEqual(TurnTicket(2), ticket2)

    def test_equal(self):
        self.assertEqual(TurnTicket(1), TurnTicket(1))
