import requests

from .xmldict import XMLDict

# Disable SSL Warnings
requests.packages.urllib3.disable_warnings()


class OnSiteSession(requests.Session):
    """Creates a Session to send requests to the OnSite public API.

    Stores private App ID, user agent, username and password."""
    def __init__(self, host, pappid, user_agent, username, password):
        super(OnSiteSession, self).__init__()
        # self.host = host
        self.base_url = 'https://' + host + '/api/'
        self.headers = {'X_PAPPID': pappid,
                        'User-Agent': user_agent}
        self.auth = (username, password)
        self.verify = False

    def request(self, method, endpoint, **kwargs):
        if endpoint[-1] != '/':
            endpoint += '/'
        if endpoint.startswith(self.base_url):
            url = endpoint
        else:
            endpoint = endpoint.lstrip('/')
            url = self.base_url + endpoint
        r = super(OnSiteSession, self).request(method, url, **kwargs)
        r.xml = XMLDict(r.text)
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
