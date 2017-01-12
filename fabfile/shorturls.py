"""Short URLs"""
import json
from netrc import netrc

import requests


def shorturl(url):
    endpoint = 'https://myl.be/yourls-api.php'

    login, account, password = netrc().authenticators('myl.be')

    data = {
        'signature': account,
        'format': 'json',
        'action': 'shorturl',
        'url': url
    }

    resp = requests.post(endpoint, data=data)

    return resp.json()['shorturl']


@task
def add(name):
    """Add shorturl to a post."""
    filename = basename(name)
    m = env.re_file_foramt.match(filename)

    date_obj = datetime.strptime('{0}-{1}-{2}'.format(m.group('year'),
                                                      m.group('month'),
                                                      m.group('day')),
                                 '%Y-%m-%d')

    post_url = env.tpl_post_url.format(date=date_obj.strftime('%Y/%j'),
                                       slug=m.group('slug'))
