# -*- coding: utf-8 -*-
"""Fabric Posts Tasks."""
from datetime import datetime
from os import makedirs
from os.path import basename, exists, join

from fabric.api import env, task
from fabric.operations import prompt
from fabric.utils import error, puts
from slugify import Slugify

from frontmatter import Post, dump

slugify = Slugify(to_lower=True)


@task
def new(post_type='simple', timestamp=datetime.now()):
    """Create a new Jekyll post."""
    if post_type not in ['simple', 'list', 'bookmark', 'article',
                         'quote']:
        raise error("The post type, '{0}', "
                    "isn't supported.".format(post_type))

    meta = {}
    meta['title'] = prompt('Title')
    meta['tags'] = prompt('Tags').split(',')
    meta['slug'] = prompt('Slug')
    meta['layout'] = 'post_{0}'.format(post_type)
    meta['category'] = post_type
    meta['date'] = timestamp.isoformat()

    if meta['slug']:
        meta['slug'] = slugify(meta['slug'])
    else:
        meta['slug'] = slugify(meta['title'])

    content = '<!-- TODO: Write something here. -->\n'

    if post_type == 'bookmark':
        meta['bookmark'] = {}

        meta['bookmark']['url'] = prompt('URL')

    post = Post(content, **meta)

    post_path = env.tpl_post_path.format(date=timestamp.strftime('%Y-%m-%d'),
                                         type=post_type,
                                         slug=meta['slug'])

    upload_path = env.tpl_upload_path.format(date=timestamp.strftime('%Y/%j'),
                                             slug=meta['slug'])

    if exists(join(env.root_dir, post_path)):
        msg = 'A post with the slug, {0}, already exists on this day.'
        raise error(msg.format(meta['slug']))

    with open(join(env.root_dir, post_path), 'w') as fobj:
        dump(post, fobj)

    if not exists(join(env.root_dir, upload_path)):
        makedirs(join(env.root_dir, upload_path))

    puts('Post: {0}\nUpload: {1}'.format(post_path, upload_path))


@task
def upload_path(name):
    """Find the upload path for a post."""
    filename = basename(name)
    m = env.re_file_foramt.match(filename)

    date_obj = datetime.strptime('{0}-{1}-{2}'.format(m.group('year'),
                                                      m.group('month'),
                                                      m.group('day')),
                                 '%Y-%m-%d')

    upload_path_date_str = date_obj.strftime('%Y/%j')
    upload_path = env.tpl_upload_path.format(date=upload_path_date_str,
                                             slug=m.group('slug'))

    if not exists(join(env.root_dir, upload_path)):
        makedirs(join(env.root_dir, upload_path))

    puts('Upload Path: {0}'.format(upload_path))
