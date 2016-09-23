"""Example GET requests to the OnSite Products API."""
import lsonsite
import xmltodict
import os
from PIL import Image
import io


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
        print('# Add a photo to a Product:\n')
        endpoint = 'products/2'
        photo_name = 'logo.png'
        headers = s.headers.update({"Content-Location": photo_name})
        s.lock(endpoint)
        with open(photo_name, mode='r+b') as f:
            upload_r = s.post(
                endpoint + "/add_product_photo",
                headers=headers,
                data=f)
        s.unlock(endpoint)
        print(upload_r.xml)

        print('# Download the photo:')
        photo_uri = upload_r.xml['product_photo']['@uri']
        print(photo_uri + 'image/')
        download_photo_name = upload_r.xml['product_photo']['scales']['scale'][2]['filename']
        print(download_photo_name)
        dest_path = os.path.expanduser('~/Desktop/' + download_photo_name)
        download_r = s.get(photo_uri + 'image/')
        download_photo = Image.open(io.BytesIO(download_r.content))
        download_photo.save(dest_path)


if __name__ == '__main__':
    main()
