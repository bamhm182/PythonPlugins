from .base import Plugin

class Api(Plugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('init api')

    def request(self, method, url):
        url = f"http://somesite.com/{url}"
        headers = {
            'Authorization': f'Bearer {self.state.api_token}'
        }
        print(f"Mocked a request to {url} with {headers}")
