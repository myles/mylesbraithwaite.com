"""Short URLs"""
import json
from datetime import datetime
from os.path import basename, join
from netrc import netrc

import requests
import frontmatter

from fabric.api import env, task


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


@task(default=True)
def add(post_path):
    """Add shorturl to a post."""
    filename = basename(post_path)
    m = env.re_file_foramt.match(filename)

    date_obj = datetime.strptime('{0}-{1}-{2}'.format(m.group('year'),
                                                      m.group('month'),
                                                      m.group('day')),
                                 '%Y-%m-%d')

    post_url = env.tpl_post_url.format(date=date_obj.strftime('%Y/%j'),
                                       slug=m.group('slug'))

    with open(join(env.root_dir, post_path), 'r') as fobj:
        post = frontmatter.loads(fobj.read())

    post.shorturl = shorturl(post_url)

    with open(join(env.root_dir, post_path), 'w') as fobj:
        frontmatter.dump(post, fobj)
