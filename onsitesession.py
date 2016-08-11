import requests


class OnSiteSession(requests.Session):
    """Creates a Session to send requests to the OnSite public API.

    Stores private App ID, user agent, username and password."""
    def __init__(self, pappid, user_agent, username, password):
        super(OnSiteSession, self).__init__()
        self.headers = {'X_PAPPID': pappid,
                        'User-Agent': user_agent}
        self.auth = (username, password)
        self.verify = False
