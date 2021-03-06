"""Example GET requests to the OnSite Products API."""
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
        print('# Filtering, sorting and working with the XMLDict result:\n')
        params = {
            'filter': '(code CONTAINS[cd] "Test" AND inventoried = 1 AND current = 1)',
            'order_by': 'id:asc'}
        r = s.get('products', params=params)
        print(r.url + '\n')
        # Note that r.xml['products'] is None if there are no matches,
        # so this part will raise an exception:
        try:
            r.xml['products']['product'][0]['code']
        except TypeError as e:
            if r.xml['products']:
                raise e
            else:
                print("No matching Products found.")
        else:
            for p in r.xml['products']['product']:
                print('- ID: ' + p['@id'])
                print('  Product Code: ' + p['code'])
                print('  Available Inventory: ' + p['inventory']['available'])
        print('-----------------------------------------------------\n')

        print('# Get an individual Product:\n')
        r = s.get('products/2')
        try:
            r.xml['product']
        except KeyError:
            pass
        else:
            info = lsonsite.XMLDict(r.xml['product'])
            print(info)
            print('Code: ' + info['code'])
            print('Description: ' + info['description']['#text'])
            sell_price = str(round(float(info['sell_price']),2))
            print('Sell: ' + sell_price)
        print('-----------------------------------------------------\n')

        print("# Try to get a Product that doesn't exist:\n")
        try:
            r= s.get('products/1000000')
        except lsonsite.RequestException:
            pass


if __name__ == '__main__':
    main()
