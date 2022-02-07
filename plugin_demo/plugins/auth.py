from .base import Plugin

class Auth(Plugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('init auth')

    def get_api_token(self):
        self.state.api_token = '12345'
