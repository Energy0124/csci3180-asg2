from smart_fixture import SmartFixture


class Refrigerator(SmartFixture):
    def __init__(self, name, weight, position, battery_capacity, initial_temperature):
        SmartFixture.__init__(self, name, weight, position, battery_capacity)
        self._temperature = initial_temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_temperature):
        self._temperature = new_temperature
        print self.name + " was set to " + "%.1f" % new_temperature + " degrees Celsius."
