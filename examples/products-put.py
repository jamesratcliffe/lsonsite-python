"""Example PUT requests to the OnSite Products API."""
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
        print('Update a Product\'s Sell price:')
        payload = lsonsite.XMLDict(
            {
                'product': {
                    'sells': {
                        'sell': 25
                        }
                    }
            })
        print(payload)
        # We must lock the Product first and unlock it afterwards.
        s.lock('products/2')
        r = s.put('products/2', data=str(payload))
        print(r.xml)
        s.unlock('products/2')

if __name__ == '__main__':
    main()
