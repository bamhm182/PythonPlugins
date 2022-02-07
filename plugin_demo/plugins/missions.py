from .base import Plugin
from . import Api, Auth


class Missions(Plugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('init missions')

    def get_missions(self):
        if not self.state.api_token:
            Auth.get_api_token(self)
        return Api.request(self, 'GET', 'api/missions')
        
