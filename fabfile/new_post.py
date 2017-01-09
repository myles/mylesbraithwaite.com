#!/usr/bin/env python3

from os import makedirs
from datetime import datetime
from os.path import dirname, realpath, join, exists

import click
import micawber
from slugify import Slugify
from bs4 import BeautifulSoup
from frontmatter import Post, dump

slugify = Slugify(to_lower=True)

TEMP_FILE_PATH = '../source/_posts/{type}/{date}-{slug}.markdown'
TEMP_UPLOAD_PATH = '../source/uploads/{date}/{slug}'


@click.group()
@click.option('--title', prompt=True)
@click.option('--tags', prompt=True)
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
    providers = micawber.bootstrap_basic()

    bookmark = {
        'url': url
    }

    try:
        oembed = providers.request(url)
        soup = BeautifulSoup(oembed['html'], 'html.parser')
    except:
        oembed = {}
        content = '<!-- TODO Write something here. -->'

    if oembed.get('type') == 'video':
        iframe_src = soup.iframe.get('src')
        content = ' include c_video.html iframe_url="{0}" '.format(iframe_src)
        bookmark = oembed

    if oembed.get('type') == 'photo':
        oembed['image_src'] = soup.img.get('src')
        content = (' include c_image.html src="{image_src}" '
                   'alt="{title}" ')

    post = Post(content, title=ctx.obj['TITLE'], layout='post_bookmark',
                category='bookmark', date=ctx.obj['NOW'].isoformat(),
                tags=ctx.obj.get('TAGS'), bookmark=bookmark)

    write_post('bookmark', ctx.obj['NOW'], ctx.obj['SLUG'], post)


@cli.command()
@click.pass_context
def list(ctx):
    post = Post(ctx.obj['CONTENT'], title=ctx.obj['TITLE'],
                layout='post_list', category='list',
                date=ctx.obj['NOW'].isoformat(), tags=ctx.obj.get('TAGS'))

    write_post('list', ctx.obj['NOW'], ctx.obj['SLUG'], post)


@cli.command()
@click.pass_context
def quote(ctx):
    post = Post(ctx.obj['CONTENT'], title=ctx.obj['TITLE'],
                layout='post_quote', category='quote',
                date=ctx.obj['NOW'].isoformat(), tags=ctx.obj.get('TAGS'))

    write_post('quote', ctx.obj['NOW'], ctx.obj['SLUG'], post)


@cli.command()
@click.pass_context
def simple(ctx):
    post = Post(ctx.obj['CONTENT'], title=ctx.obj['TITLE'],
                layout='post_simple', category='simple',
                date=ctx.obj['NOW'].isoformat(), tags=ctx.obj.get('TAGS'))

    write_post('simple', ctx.obj['NOW'], ctx.obj['SLUG'], post)


if __name__ == '__main__':
    cli(obj={})
