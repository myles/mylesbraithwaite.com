"""Short URLs"""
import codecs
from datetime import datetime
from netrc import netrc
from os.path import basename, join


import frontmatter
import requests

from fabric.api import abort, env, task
from fabric.utils import puts


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

    with codecs.open(join(env.root_dir, post_path), 'r', 'utf-8') as fobj:
        post = frontmatter.loads(fobj.read())

    if post.get('shorturl'):
        abort('Post already has a short url: {shorturl}.'.format(**post))

    meta = post.to_dict()
    content = meta['content']
    del(meta['content'])

    meta['shorturl'] = shorturl(post_url)

    with codecs.open(join(env.root_dir, post_path), 'w', 'utf-8') as fobj:
        new_post = frontmatter.Post(content, **meta)
        frontmatter.dump(new_post, fobj)

    puts('Added the short url: {shorturl}.'.format(**meta))
