

class State:
    def __init__(self):
        self._something = None

    @property
    def something(self):
        return self._something

    @something.setter
    def something(self, value):
        self._something = value
