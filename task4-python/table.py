from dumb_fixture import DumbFixture


class Table(DumbFixture):
    def __init__(self, name, weight, position, person_in_charge, extendable):
        DumbFixture.__init__(self, name, weight, position, person_in_charge)
        self._extendable = extendable

    @property
    def extendable(self):
        return self._extendable
