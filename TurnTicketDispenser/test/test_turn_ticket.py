import unittest

from turn_ticket import TicketDispenser, TurnTicket, TurnNumberSequence


class TicketDispenserTest(unittest.TestCase):

    def test_do_something(self):
        dispenser = TicketDispenser()
        ticket = dispenser.getTurnTicket()
        self.assertEqual(TurnTicket(0), ticket)

    def test_do_somethingAA(self):
        turn_number_sequence = TurnNumberSequence()
        dispenser1 = TicketDispenser(turn_number_sequence=turn_number_sequence)
        dispenser2 = TicketDispenser(turn_number_sequence=turn_number_sequence)
        ticket0 = dispenser1.getTurnTicket()
        ticket1 = dispenser1.getTurnTicket()
        ticket2 = dispenser2.getTurnTicket()
        self.assertEqual(TurnTicket(0), ticket0)
        self.assertEqual(TurnTicket(1), ticket1)
        self.assertEqual(TurnTicket(2), ticket2)

    def test_equal(self):
        self.assertEqual(TurnTicket(1), TurnTicket(1))
