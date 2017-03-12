from fixture import Fixture


class SmartFixture(Fixture):
    def __init__(self, name, weight, position, battery_capacity):
        Fixture.__init__(self, name, weight, position)
        self._battery_capacity = battery_capacity
        self._battery_remaining = battery_capacity

    def charge_battery(self, amount):
        self._battery_remaining += amount
        if self._battery_remaining > self._battery_capacity:
            self._battery_remaining = self._battery_capacity
        print self.name + " was charged " + "%.1f" % amount + " units of battery."

    def consume_battery(self, amount):
        if amount >= self._battery_remaining:
            return -1
        else:
            self._battery_remaining -= amount
            return self._battery_remaining

    def move_to(self, destination):
        distance = abs(self.position - destination.position)
        battery_consumed = distance * self.weight
        if self.consume_battery(battery_consumed) > 0:
            self.position = destination.position
            print self.name + " moved to " + destination.name + "."
            print self.name + " consumed " + "%.1f" % battery_consumed + " battery."
        else:
            print "Not enough battery to move!"
