#!/usr/bin/env python3
"""
# New Post

Create a new post.

## Requires

* click
* awesome-slugify
* python-frontmatter
"""

from datetime import datetime
from urlparse import urlparse, parse_qs
from os.path import dirname, realpath, join

import click
from slugify import Slugify
from frontmatter import Post, dump

slugify = Slugify(to_lower=True)

TEMP_FILEPATH = './source/_posts/{type}/{date}-{slug}.markdown'


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
    filepath = TEMP_FILEPATH.format(date=date.strftime('%Y-%m-%d'),
                                    type=post_type, slug=slug)

    with open(join(dirname(realpath(__file__)), filepath), 'w') as fobj:
        dump(post, fobj)


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
                url={'url': url})

    write_post('bookmark', ctx.obj['NOW'], ctx.obj['SLUG'], post)


if __name__ == '__main__':
    cli(obj={})
