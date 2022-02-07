class Plugin:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # {'Api': <class 'plugins.api.Api'>} etc...
        cls.registry[cls.__name__] = cls

    def __init__(self, state):
        # things shared between all plugins can be defined at this level, to include methods or w/e
        self.state = state
