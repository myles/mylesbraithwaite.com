#!/usr/bin/env python3
"""
# New Post

Create a new post.

## Requires

* click
* awesome-slugify
* python-frontmatter
"""

from os import makedirs
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from os.path import dirname, realpath, join, exists

import click
from slugify import Slugify
from frontmatter import Post, dump

slugify = Slugify(to_lower=True)

TEMP_FILE_PATH = '../source/_posts/{type}/{date}-{slug}.markdown'
TEMP_UPLOAD_PATH = '../source/uploads/{date}/{slug}'


@click.group()
@click.option('--title', prompt=True)
@click.option('--tags')
@click.option('--slug')
@click.pass_context
def cli(ctx, title, tags, slug):
    ctx.obj['TITLE'] = title
    ctx.obj['NOW'] = datetime.now()
    ctx.obj['CONTENT'] = '<!-- TODO: Write something here. -->\n'

    if tags:
        ctx.obj['TAGS'] = tags.split(',')

    if slug:
        ctx.obj['SLUG'] = slugify(slug)
    else:
        ctx.obj['SLUG'] = slugify(title)


def write_post(post_type, date, slug, post):
    file_path = TEMP_FILE_PATH.format(date=date.strftime('%Y-%m-%d'),
                                      type=post_type, slug=slug)
    upload_path = TEMP_UPLOAD_PATH.format(date=date.strftime('%Y/%j'),
                                          slug=slug)

    with open(join(dirname(realpath(__file__)), file_path), 'w') as fobj:
        dump(post, fobj)

    if not exists(upload_path):
        makedirs(upload_path)


@cli.command()
@click.pass_context
def article(ctx):
    post = Post(ctx.obj['CONTENT'], title=ctx.obj['TITLE'],
                layout='post_article', category='article',
                date=ctx.obj['NOW'].isoformat(), tags=ctx.obj.get('TAGS'))

    write_post('article', ctx.obj['NOW'], ctx.obj['SLUG'], post)


@cli.command()
@click.option('--url', prompt=True)
@click.pass_context
def bookmark(ctx, url):
    if 'youtube.com' in url:
        youtube_id = parse_qs(urlparse(url).query)['v'][0]

        ctx.obj['CONTENT'] = '{% c_responsive_video iframe_url=https://www.youtube-nocookie.com/embed/{} %}'.format(youtube_id)
    elif 'vimeo.com' in url:
        ctx.obj['CONTENT'] = '{% c_responsive_vidoe iframe_url=https://player.vimeo.com/video/TODO %}'

    post = Post(ctx.obj['CONTENT'], title=ctx.obj['TITLE'],
                layout='post_bookmark', category='bookmark',
                date=ctx.obj['NOW'].isoformat(), tags=ctx.obj.get('TAGS'),
                bookmark={'url': url})

    write_post('bookmark', ctx.obj['NOW'], ctx.obj['SLUG'], post)


if __name__ == '__main__':
    cli(obj={})
