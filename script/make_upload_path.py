#!/usr/bin/env python3

import re
from os import makedirs
from datetime import datetime
from os.path import basename, exists, join, dirname, realpath

import click


@click.command()
@click.argument('name')
def cli(name):
    file_format_re = re.compile(r'^(?P<year>\d{4})-(?P<month>\d{2})-'
                                r'(?P<day>\d{2})-(?P<slug>[-\w]+)\.'
                                r'(?P<format>\w+)$')

    file_name = basename(name)
    m = file_format_re.match(file_name)

    date_obj = datetime.strptime('{year}-{month}-{day}'.format(year=m.group('year'),
                                                    month=m.group('month'),
                                                    day=m.group('day')),
                                 '%Y-%m-%d')

    upload_path_tpl = '../source/uploads/{year}/{day}/{slug}'

    upload_path = upload_path_tpl.format(year=m.group('year'),
                                         day=date_obj.strftime('%j'),
                                         slug=m.group('slug'))

    full_upload_path = join(dirname(realpath(__file__)), upload_path)

    makedirs(full_upload_path, exist_ok=True)

    click.echo(upload_path)


if __name__ == '__main__':
    cli()
