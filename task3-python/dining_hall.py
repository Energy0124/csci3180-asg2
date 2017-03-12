from room import Room


class DiningHall(Room):
    def __init__(self, name, postion, dinner_price):
        Room.__init__(self, name, postion)
        self._dinner_price = dinner_price

    @property
    def dinner_price(self):
        return self._dinner_price

    def serve_dinner_to(self, obj):
        if obj.position == self.position:
            if obj.pay(self._dinner_price) > 0:
                print obj.name + " finished the dinner."
            else:
                print obj.name + " didn't have enough money."
        else:
            print obj.name + " was too far away to be served."
