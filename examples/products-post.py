"""Example POST requests to the OnSite Products API."""
import lsonsite
import xmltodict


def main():
    # Read app configuration from config.xml
    with open('config.xml') as f:
        config = xmltodict.parse(f.read())['appconfig']
    host = config['host']
    pappid = config['pappid']
    user_agent = config['user_agent']
    user = config['user']
    pw = config['password']

    # Open a Session
    with lsonsite.OnSiteSession(host, pappid, user_agent, user, pw) as s:
        print('Create a Product:')
        payload = lsonsite.XMLDict(
            {
                'product': {
                    'code': 'MAXCRAX',
                    'description': 'Cracks for Max',
                    'sells': {
                        'sell': 1
                    }
                }
            })
        print(payload)
        r = s.post('products', data=str(payload))
        print(r.xml)

if __name__ == '__main__':
    main()
