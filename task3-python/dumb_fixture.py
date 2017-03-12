from fixture import Fixture


class DumbFixture(Fixture):
    def __init__(self, name, weight, position, person_in_charge):
        Fixture.__init__(self, name, weight, position)
        self._person_in_charge = person_in_charge

    @property
    def person_in_charge(self):
        return self._person_in_charge

    def assign_to(self, person_in_charge):
        self._person_in_charge = person_in_charge

    def move_to(self, destination):
        self._person_in_charge.carry_to(self, destination)
