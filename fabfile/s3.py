# -*- coding: utf-8 -*-
from os.path import join

from fabric.api import env, task, local


@task
def sync():
    """Sync the uploads directory."""
    config = {
        'local': join(env.root_dir, 'source/uploads'),
        'remote': 's3://assets.mylesbraithwaite.com/uploads/',
        'exclude': '".DS_Store"'
    }

    local('aws s3 sync {local} {remote} --exclude {exclude}'.format(**config))
