# -*- coding: utf-8 -*-
import netrc
import os
import time
from os.path import join
from stat import *


from boto.s3.connection import S3Connection
from boto.s3.key import Key
from fabric.api import env, task


def client():
    login, account, password = netrc.netrc().authenticators('aws')
    
    conn = S3Connection(login, password)
    return conn.get_bucket('assets.mylesbraithwaite.com')


@task
def push():
    """Push uploads to AWS S3."""
    bucket = client()
    
    # Upload Files
    for root, dirs, files in os.walk(join(env.root_dir, 'source/uploads')):
        for f in files:
            if f.endswith('.swp') or f.startswith('.'):
                continue

            filename = join('uploads', root, f)
            modify_time = os.stat(filename)[ST_MTIME]

            key = bucket.get_key(filename)

            if key is None:
                key = Key(bucket)
                key.key = filename

            if key.last_modified is None or time.localtime(modify_time) > time.strptime(key.last_modified, '%a, %d %b %Y %H:%M:%S %Z'):
                fid = file(filename, 'r')
                key.set_contents_from_file(fd)
                key.set_acl('public-read')


@task
def pull():
    """Pull uploads from AWS S3."""
    bucket = client()
