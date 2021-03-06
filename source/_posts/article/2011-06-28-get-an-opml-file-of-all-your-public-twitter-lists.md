---
layout: post_article
category: article
date: 2011-06-28T12:31:00
title: Get an OPML File of All Your Public Twitter Lists
tags: [twitter, feed, python, programming]
---

I made this simple python script today to get an OPML file so I can import all my Twitter lists.

```python
#!/usr/bin/env python

__version__ = '0.1'
__project_name__ = 'TwitterListOPML'
__project_link__ = 'https://gist.github.com/1051517'

TWITTER_LISTS_URL = "http://api.twitter.com/1/%(username)s/lists.json"
TWITTER_LIST_FEED_URL = "http://api.twitter.com/1/%(username)s/lists/%(list)s/statuses.atom"
TWITTER_LIST_HTML_URL = "http://twitter.com/%(username)s/%(list)s"

OPML_START = """<?xml version="1.0" encoding="UTF-8"?>
<!-- OPML generated by TwitterListOPML -->
<opml version="1.1">
    <head>
        <title>Twitter Lists</title>
    </head>
    <body>
        <outline text="Twitter Lists" title="Twitter Lists">"""
OPML_END = """      </outline>
    </body>
</opml>"""

OPML_OUTLINE_FEED = '<outline text="%(title)s" title="%(title)s" type="rss" version="RSS" htmlUrl="%(html_url)s" xmlUrl="%(xml_url)s" />'

import sys
import urllib2

try:
    import json
except ImportError:
    import simplejson as json

def get_lists(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent', '%s/%s +%s' % (
        __project_name__, __version__, __project_link__
    ))
    opener = urllib2.build_opener()
    data = opener.open(request).read()
    return json.loads(data)

def main(username):
    t_lists = get_lists(TWITTER_LISTS_URL % {'username': username})

    print OPML_START

    for t_list in t_lists['lists']:
        list_title = t_list['name']
        list_html_url = TWITTER_LIST_HTML_URL % {'username': username, 'list': t_list['slug']}
        list_xml_url = TWITTER_LIST_FEED_URL % {'username': username, 'list': t_list['slug']}
        print OPML_OUTLINE_FEED % {'title': list_title, 'html_url': list_html_url, 'xml_url': list_xml_url}

    print OPML_END

if __name__ == "__main__":
    username = sys.argv[-1]
    main(username)
```

You can download the Python script, [twitter_list_to_opml.py.gz]({{ '/2011/179/get-an-opml-file-of-all-your-public-twitter-lists/twitter_list_to_opml.py.gz' | prepend: upload_url }}).
