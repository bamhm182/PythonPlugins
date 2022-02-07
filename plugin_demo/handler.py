from plugins.base import Plugin
from state import State

class Handler:
    def __init__(self, state=None):
        if state == None:
            state = State()
        self.state = state

        for name, subclass in Plugin.registry.items():
            instance = subclass(self.state)
            setattr(self, name.lower(), instance)
