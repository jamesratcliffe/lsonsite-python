import requests


class OnSiteSession(requests.Session):
    """Creates a Session to send requests to the OnSite public API.

    Stores private App ID, user agent, username and password."""
    def __init__(self, host, pappid, user_agent, username, password):
        super(OnSiteSession, self).__init__()
        self.host = host
        self.headers = {'X_PAPPID': pappid,
                        'User-Agent': user_agent}
        self.auth = (username, password)
        self.verify = False

    def request(self, method, endpoint, **kwargs):
        endpoint = endpoint.lstrip('/')
        if endpoint[-1] != '/':
            endpoint += '/'
        url = "https://{0}/api/{1}".format(self.host, endpoint)
        r = super(OnSiteSession, self).request(method, url, **kwargs)
        return r

    def lock(self, endpoint):
        self.request('LOCK', endpoint)

    def unlock(self, endpoint):
        self.request('UNLOCK', endpoint)

    def logout(self):
        self.post('sessions/current/logout/')

    def close(self):
        self.logout()
        super(OnSiteSession, self).close()
