# LSOnSite

This package provides an OnSiteSession class—an extension of the [Session](http://docs.python-requests.org/en/master/user/advanced/#session-objects) class from [Reqests](http://docs.python-requests.org/en/master/)—to connect to a Lightspeed OnSite Server and make requests.


## OnSiteSession

The OnSiteSession keeps track of the hostname (with port) Private App ID and User Agent, as well as the username and password for the Lightspeed OnSite User your application will connect as.

The OnSiteSession automatically takes care of cookies (this is inherited from Requests' Session class), and will send a logout request when closing the Session.


## Example

```python
with lsonsite.OnSiteSession(HOST, PAPPID, USER_AGENT, USER, PW) as s:
    r = s.get('products/147')
    print(r.text)
```

## XMLDict

This package also provides the XMLDict class. This takes a string of XML and converts it to a dictionary using [xmltodict](https://github.com/martinblech/xmltodict).

It will act like a Python dictionary, but print as indented XML:

```python
with lsonsite.OnSiteSession(HOST, PAPPID, USER_AGENT, USER, PW) as s:
    r = s.get('products/147')
    print(r.xml)
```
