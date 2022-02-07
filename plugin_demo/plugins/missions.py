from .base import Plugin

from .api import Api

class Missions(Plugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('init missions')

    def do_stuff(self):
        Api.do_things(self)
        print('doin stuff with state:', self.state)
