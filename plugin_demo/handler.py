from plugins.base import Plugin


class Handler:
    def __init__(self, state):
        self.state = state

        for name, subclass in Plugin.registry.items():
            instance = subclass(self.state)
            setattr(self, name.lower(), instance)
