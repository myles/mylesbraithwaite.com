# -*- coding: utf-8 -*-
"""Fabic Tags Tasks."""

from fabric.api import task
from fabric.utils import puts

from .utils import tag_get, tag_list


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
