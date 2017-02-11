# -*- coding: utf-8 -*-
"""Fabric S3 Tasks."""
from os.path import join

from fabric.api import env, local, task


@task
def push():
    """Push all uploads to S3."""
    config = {
        'local': join(env.root_dir, 'source/uploads'),
        'remote': 's3://assets.mylesbraithwaite.com/uploads/',
        'exclude': '".DS_Store"'
    }

    local('aws s3 sync {local} {remote} --exclude {exclude}'.format(**config))


@task
def pull():
    """Pull all uploads to S3."""
    config = {
        'local': 's3://assets.mylesbraithwaite.com/uploads/',
        'remote': join(env.root_dir, 'source/uploads'),
        'exclude': '".DS_Store"'
    }

    local('aws s3 sync {local} {remote} --exclude {exclude}'.format(**config))
