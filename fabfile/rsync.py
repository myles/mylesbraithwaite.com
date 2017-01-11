# -*- coding: utf-8 -*-
"""Fabric rsync Tasks."""
from os.path import join

from fabric.api import env, local, task


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

    local('rsync -pthrvz {local_dir} {remote_dir}'.format(**args))
