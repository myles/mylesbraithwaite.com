# -*- coding: utf-8 -*-
from fabric.api import task

from . import config
from . import jekyll
from . import posts
from . import rsync
from . import s3
from . import sort_yaml
from . import tags


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
