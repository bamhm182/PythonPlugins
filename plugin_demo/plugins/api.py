from .base import Plugin


class Api(Plugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('init api')

    def do_things(self):
        print('doin things with state:', self.state)
