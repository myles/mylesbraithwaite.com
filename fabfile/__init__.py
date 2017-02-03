# -*- coding: utf-8 -*-
"""Fabfile."""
from fabric.api import task

from . import config  # noqa: F401
from . import jekyll
from . import posts  # noqa: F401
from . import rsync
from . import s3  # noqa: F401
from . import sort_yaml  # noqa: F401
from . import shorturls  # noqa: F401
from . import tags  # noqa: F401


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
