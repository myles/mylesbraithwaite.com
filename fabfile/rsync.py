# -*- coding: utf-8 -*-
from os.path import join

from fabric.api import env, task
from fabric.contrib.project import rsync_project


@task
def push(environment='stag'):
    """Push website though rsync."""
    args = {}

    if environment == 'local':
        args['local_dir'] = join(env.root_dir, env.config_local['destination'])
        args['remote_dir'] = env.config_local['rsync']

    elif environment == 'prod':
        args['local_dir'] = join(env.root_dir, env.config_prod['destination'])
        args['remote_dir'] = env.config_prod['rsync']

    else:
        args['local_dir'] = join(env.root_dir, env.config_stag['destination'])
        args['remote_dir'] = env.config_stag['rsync']

    rsync_project(**args)
