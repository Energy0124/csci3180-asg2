class Attendant:
    def __init__(self, name, weight, wealth, position):
        self._position = position
        self._wealth = wealth
        self._weight = weight
        self._name = name

    # def move_to(self, destination):
    #     distance = abs(self._position - destination.position
    #     calories_consumed = distance * self._weight
    #     self._position = destination.position
    #     print self._name + " moved to " + destination.name + "."
    #     return calories_consumed

    def move_to(self, destination, obj=None):
        if obj is None:
            distance = abs(self._position - destination.position)
            calories_consumed = distance * self._weight
            self._position = destination.position
            print self._name + " moved to " + destination.name + "."
            return calories_consumed
        else:
            distance = abs(obj.position - destination.position)
            calories_consumed = distance * obj.weight
            obj.position = destination.position
            print obj.name + " was moved to " + destination.name + "."
            return calories_consumed

    def carry_to(self, obj, destination):
        calories_consumed = 0
        calories_consumed += self.move_to(obj)
        calories_consumed += self.move_to(destination)
        calories_consumed += self.move_to(destination, obj)
        print self._name + " consumed " + "%.1f" % calories_consumed + " calories."

    @property
    def position(self):
        return self._position

    @property
    def wealth(self):
        return self._wealth

    @property
    def weight(self):
        return self._weight

    @property
    def name(self):
        return self._name

    def pay(self, amount):
        if amount <= self._wealth:
            self._wealth -= amount
            print self._name + " paid " + "%.1f" % amount + " dollars."
            return amount
        else:
            return -1
