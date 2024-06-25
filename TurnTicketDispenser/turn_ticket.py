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

    def __init__(self):
        self._turnNumber = -1

    def next_turn_number2(self):
        self._turnNumber += 1
        return self._turnNumber




class TicketDispenser(object):
    def __init__(self, turn_number_sequence=TurnNumberSequence()):
        self.turn_number_sequence = turn_number_sequence


    def getTurnTicket(self) -> TurnTicket:
        newTurnNumber = self.turn_number_sequence.next_turn_number2()
        newTurnTicket = TurnTicket(newTurnNumber)
        return newTurnTicket
