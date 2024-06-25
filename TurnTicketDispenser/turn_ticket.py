class TurnTicket(object):
    def __init__(self, turnNumber):
        self.turnNumber = turnNumber

    def __eq__(self, other):
        return self.turnNumber == other.turnNumber

    def __repr__(self):
        return f"TurnTicket({self.turnNumber})"

    def __str__(self):
        return "x"

class TurnNumberSequence(object):
    _turnNumber = -1

    @staticmethod
    def next_turn_number():
        TurnNumberSequence._turnNumber += 1
        return TurnNumberSequence._turnNumber


class TicketDispenser(object):
    def getTurnTicket(self) -> TurnTicket:
        newTurnNumber = TurnNumberSequence.next_turn_number()
        newTurnTicket = TurnTicket(newTurnNumber)
        return newTurnTicket
