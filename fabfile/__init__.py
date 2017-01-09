# -*- coding: utf-8 -*-
from os.path import join

import yaml
from fabric.api import env, task

from . import config
from . import jekyll
from . import rsync


@task
def build(environment='local'):
    """Build the website."""
    jekyll.build(environment)


@task
def deploy(environment='stag'):
    """Deploy the website."""
    jekyll.build(environment)
    rsync.push(environment)


@task
def develop():
    """Run a test web server locally."""
    jekyll.serve()
