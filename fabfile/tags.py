# -*- coding: utf-8 -*-
from glob import glob
from itertools import groupby
from os.path import dirname, realpath, join

import yaml
import frontmatter
from fabric.api import env, task
from fabric.utils import puts


def post_list():
    """
    A list of the Jekyll posts.

    Returns
    -------
    list
        A list of frontmatter.Post objects.
    """

    posts_dir = join(env.root_dir, 'source/_posts')

    post_files = glob(join(posts_dir, '**', '*'))

    post_list = []

    for post_file in post_files:
        post = frontmatter.load(post_file)
        post['file_path'] = post_file.replace(posts_dir, './source/_posts')
        post_list.append(post)

    return post_list


def tag_yml():
    """
    Converts the `./source/_data/tags.yml` file to a Python dict.

    Returns
    -------
    dict
        The contents of the `./source/_data/tags.yml` file convert to a dict.
    """
    with open(join(env.root_dir, 'source/_data/tags.yml'), 'r') as fobj:
        return yaml.load(fobj.read())


def tag_meta(slug):
    """
    Get the meta information of a specific tag.

    Paramerters
    -----------
    slug : str
        The slug of the tag.

    Returns
    -------
    dict
        The meta data of the tag.
    """
    meta = tag_yml()

    return meta.get(slug, {'name': slug})


def tag_list():
    """
    Get all the tags that are currently used in posts.

    Returns
    -------
    list
        A list of dict with tag meta data.
    """
    tag_list = []

    for post in post_list():
        tag_list = tag_list + post['tags']

    tag_list.sort()

    resp = []

    for tag, group in groupby(tag_list):
        resp.append({
            'name': tag,
            'count': len(list(group)),
            # 'posts': posts
        })

    return resp


def tag_get(slug):
    """
    Get information about an individual tag.

    Paramerters
    -----------
    slug : str
        The slug of the tag.

    Returns
    -------
    list
        A list of dict with the tag meta data.
    """
    tag_info = tag_meta(slug)
    tag_info['posts'] = []

    for post in post_list():
        if any(tag == slug for tag in post['tags']):
            tag_info['posts'].append(post)

    return tag_info


@task
def all():
    """List all the tags."""

    resp = []

    for tag in tag_list():
        resp.append('{name} ({count})'.format(**tag))

    puts('\n'.join(resp))


@task
def get(slug):
    """Get information about a tag."""
    tag = tag_get(slug)

    puts('{name}'.format(**tag))

    for post in tag['posts']:
        puts('{title} - {file_path}'.format(**post))
