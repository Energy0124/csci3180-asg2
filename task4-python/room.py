class Room:

    def __init__(self, name, postion):
        self._name=name
        self._position= postion

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position
