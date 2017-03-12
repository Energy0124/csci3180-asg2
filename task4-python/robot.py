class Robot:
    def __init__(self, name, weight, position, battery_capacity):
        self._position = position
        self._battery_capacity = battery_capacity
        self._battery_remaining = battery_capacity
        self._weight = weight
        self._name = name

    def move_to(self, destination, obj=None):
        if obj is None:
            distance = abs(self._position - destination.position)
            battery_consumed = distance * self._weight
            if self.consume_battery(battery_consumed) > 0:
                self._position = destination.position
                print self.name + " moved to " + destination.name + "."
            else:
                print "Not enough battery to move!"
            return battery_consumed
        else:
            distance = abs(obj.position - destination.position)
            battery_consumed = distance * obj.weight
            if self.consume_battery(battery_consumed) > 0:
                obj.position = destination.position
                print obj.name + " was moved to " + destination.name + "."
            else:
                print "Not enough battery to move!"
            return battery_consumed

    def carry_to(self, obj, destination):
        battery_consumed = 0
        robot_distance = abs(self.position - obj.position) + abs(obj.position - destination.position)
        battery_consumed += robot_distance * self.weight
        obj_distance = abs(obj.position - destination.position)
        battery_consumed += obj_distance * obj.weight
        if battery_consumed >= self._battery_remaining:
            print "Not enough battery to move!"
        else:
            battery_consumed = 0
            battery_consumed += self.move_to(obj)
            battery_consumed += self.move_to(destination)
            battery_consumed += self.move_to(destination, obj)
            print self._name + " consumed " + "%.1f" % battery_consumed + " units of battery."

    @property
    def position(self):
        return self._position

    @property
    def weight(self):
        return self._weight

    @property
    def name(self):
        return self._name

    def charge_battery(self, amount):
        self._battery_remaining += amount
        if self._battery_remaining > self._battery_capacity:
            self._battery_remaining = self._battery_capacity
        print self.name + " charged " + "%.1f" % amount + " units of battery."

    def consume_battery(self, amount):
        if amount >= self._battery_remaining:
            return -1
        else:
            self._battery_remaining -= amount
            return self._battery_remaining
