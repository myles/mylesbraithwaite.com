#!/usr/bin/env python3

from glob import glob
from itertools import groupby
from os.path import dirname, realpath, join

import yaml
import click
import frontmatter


def tag_meta(tag_name):
    with open(join(dirname(realpath(__file__)),
                   '../source/_data/tags.yml'), 'r') as fobj:
        meta = yaml.load(fobj.read())

    return meta.get(tag_name, {'name': tag_name})


def post_list():
    posts_dir = join(dirname(realpath(__file__)), '../source/_posts')

    post_files = glob(join(posts_dir, '**', '*'))

    post_list = []

    for post_file in post_files:
        post = frontmatter.load(post_file)
        post['file_path'] = post_file.replace(posts_dir, './source/_posts')
        post_list.append(post)

    return post_list


@click.group()
def cli():
    pass


@cli.command('list')
def tag_list():
    """List all the tags."""

    tag_list = []

    for post in post_list():
        tag_list = tag_list + post['tags']

    tag_list.sort()

    resutls = []

    for tag, group in groupby(tag_list):
        count = len(list(group))
        resutls.append('{tag} ({count})'.format(tag=tag, count=count))

    click.echo_via_pager('\n'.join(resutls))


@cli.command('get')
@click.argument('name', metavar='<name>')
def tag_get(name):
    """Get information about a tag."""

    tag_info = tag_meta(name)
    tag_info['posts'] = []

    for post in post_list():
        if any(tag == name for tag in post['tags']):
            tag_info['posts'].append(post)

    click.secho('{name}'.format(**tag_info), fg='green')

    for post in tag_info['posts']:
        click.echo('{title} - {file_path}'.format(**post))


if __name__ == '__main__':
    cli()
