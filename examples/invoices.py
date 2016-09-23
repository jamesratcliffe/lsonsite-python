"""Example GET requests to the OnSite Products API."""
import lsonsite
import xmltodict
import pprint
import collections


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
        print('# Create a blank Invoice and get its URI:\n')
        create_payload = lsonsite.XMLDict({
            'invoice': {
                'invoice_customer': {
                    'customer': {'@id': 6}
                },
                'station': 'API',
                'c_discount_percentage': 10
            }})
        print(create_payload)
        r = s.post('invoices', data=str(create_payload))
        # print(r.xml)
        invoice_uri = r.xml['invoice']['@uri']
        print("\n" + invoice_uri)
        print('-----------------------------------------------------\n')

        print('# Add a Product to the Invoice:\n')
        add_payload = lsonsite.XMLDict({
            'lineitem': {
                'quantity': 1,
                'lineitem_product': {
                    'product': {'@id': 3}
                }
            }})

        # We have to lock the Invoice, add the Product, then unlock.
        s.lock(invoice_uri)
        s.post(invoice_uri + 'lineitems/', data=str(add_payload))
        s.unlock(invoice_uri)

        # r = s.get(invoice_uri)
        r = s.get('invoices/55')
        print_invoice(r)


def print_invoice(response):
    print("""Invoice ID: {0}
Customer: {1}
Subtotal: {2}
Tax: {3}
Total: {4}""".format(
        response.xml['invoice']['invoice_id'],
        response.xml['invoice']['invoice_customer']['mainname'],
        response.xml['invoice']['totals']['subtotal'],
        response.xml['invoice']['totals']['tax'],
        response.xml['invoice']['totals']['total']
    ))
    lineitems = response.xml['invoice']['lineitems']['lineitem']
    if not isinstance(lineitems, list):
        lineitems = [lineitems]
    print('Line Items:')
    for i, line in enumerate(lineitems):
        print("""    Code: {0}
    Description: {1}
    Quantity: {2}
    Sell Regular: {3}
    Sell: {4}""".format(
            line['lineitem_product']['code'],
            line['lineitem_product']['description'],
            line['quantity'],
            line['sells']['base'],
            line['sell_price']
        ))
        if i != len(lineitems) - 1:
            print("    ----")


if __name__ == '__main__':
    main()
