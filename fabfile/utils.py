# -*- coding: utf-8 -*-
"""Fabic Utilities."""

from glob import glob
from itertools import groupby
from os.path import join

import yaml
from fabric.api import env

import frontmatter


def merge_dicts(*dict_args):
    """
    Merge multiple Dictonaries.

    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


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
        post['file_path'] = post_file.replace(posts_dir,
                                              './source/_posts')
        post_list.append(post)

    return post_list


def data_get(filename):
    """
    Convert the `./source/_data/*.{yml,json}` file to a Python dict.

    Paramerters
    -----------
    filename : str
        The name of the data file you want to load.

    Returns
    -------
    dict
        The contents of the data file convert to a dict.
    """
    filename = 'source/_data/{0}'.format(filename)

    with open(join(env.root_dir, filename), 'r') as fobj:
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
    meta = data_get('tags.yml')

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
