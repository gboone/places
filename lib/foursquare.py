import requests
class Foursquare():
    """docstring for Foursquare"""
    def __init__(self, token):
        self.token = token
        self.path = "_data"
        self.version = 20150907
        self.mode = "swarm"
        self.limit = 250

    def checkins(self):
        url = "https://api.foursquare.com/v2/users/self/checkins"
        params = {"oauth_token":self.token, "v":self.version, "m":self.mode, "limit":self.limit}
        response = requests.get(url, params=params)
        if response.ok:
            json = response.json()
            return json['response']['checkins']['items']
        else:
            import pdb; pdb.set_trace()

    def save_as_json(data, filename):
        pass
