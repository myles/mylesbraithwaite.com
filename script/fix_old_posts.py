import re
from glob import glob
from os.path import dirname, realpath, join

import frontmatter
from dateutil.parser import parse as dateutil_parse

posts_dir = join(dirname(realpath(__file__)), '../source/_posts')

post_filenames = glob(join(posts_dir, '**', '2*'))

date_regex = re.compile(r'date: (?P<date>[-\w]+) (?P<time>[:\d+]+)')
layout_regex = re.compile(r'layout: (?P<layout>[_\w]+)')
category_regex = re.compile(r'category: (?P<category>[\w]+)')

for post_filename in post_filenames:
    print(post_filename)

    with open(post_filename, 'r') as fobj:
        content = fobj.read()

    date_match = date_regex.search(content)
    layout_match = layout_regex.search(content)
    category_match = category_regex.search(content)

    if date_match:
        date_obj = dateutil_parse("{0} {1}".format(date_match.group('date'),
                                                   date_match.group('time')))

        date_tpl = 'date: {:%Y-%m-%d}T{:%H:%M:%S}'

        content = content.replace(date_match.group(),
                                  date_tpl.format(date_obj, date_obj))

    if layout_match.group('layout') == 'post':
        layout_tpl = 'layout: post_{}'
        category = category_match.group('category')
        content = content.replace(layout_match.group(),
                                  layout_tpl.format(category))

    with open(post_filename, 'w') as fobj:
        fobj.write(content)
