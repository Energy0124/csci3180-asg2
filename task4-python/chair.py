from dumb_fixture import DumbFixture


class Chair(DumbFixture):
    def __init__(self, name, weight, position, person_in_charge, seat_back):
        DumbFixture.__init__(self, name, weight, position, person_in_charge)
        self._seat_back = seat_back

    @property
    def seat_back(self):
        return self._seat_back
