class Fixture:
    def __init__(self, name, weight, position):
        self._name = name
        self._weight = weight
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position
