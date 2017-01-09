# -*- coding: utf-8 -*-
from fabric.api import env, local, task


def jekyll(command, *args, **kwargs):
    opts = []

    for arg in args:
        opts.append('--{}'.format(arg))

    for key, value in kwargs.items():
        opts.append('--{0}={1}'.format(key, value))

    local('bundle exec jekyll {0} {1}'.format(command, ' '.join(opts)))


@task
def build(environment='stag'):
    config = [env.config_base_file]

    if environment == 'local':
        config.append(env.config_local_file)

    elif environment == 'prod':
        config.append(env.config_prod_file)

    else:
        config.append(env.config_stag_file)

    jekyll('build', config=','.join(config))


@task
def serve():
    jekyll('serve', 'auto', 'show_drafts', 'future', 'unpublished', config=','.join([env.config_base_file, env.config_local_file]), limit_posts=50)
