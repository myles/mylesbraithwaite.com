# -*- coding: utf-8 -*-
import os
import re
from os.path import abspath, dirname, realpath, join

import yaml

from fabric.api import env

from .utils import merge_dicts

env.root_dir = abspath(join(dirname(realpath(__file__)), os.pardir))

# Config Files
env.config_base_file = abspath(join(env.root_dir, 'config/base.yml'))
env.config_local_file = abspath(join(env.root_dir, 'config/local.yml'))
env.config_prod_file = abspath(join(env.root_dir, 'config/prod.yml'))
env.config_stag_file = abspath(join(env.root_dir, 'config/stag.yml'))

# File Templates
env.tpl_post_path = 'source/_posts/{type}/{date}-{slug}.markdown'
env.tpl_upload_path = 'source/uploads/{date}/{slug}'

# Prase Jekyll Config
with open(env.config_base_file, 'r') as fobj:
    env.config = yaml.load(fobj.read())

with open(env.config_local_file, 'r') as fobj:
    env.config_local = merge_dicts(env.config, yaml.load(fobj.read()))

with open(env.config_prod_file, 'r') as fobj:
    env.config_prod = merge_dicts(env.config, yaml.load(fobj.read()))

with open(env.config_stag_file, 'r') as fobj:
    env.config_stag = merge_dicts(env.config, yaml.load(fobj.read()))

# Regular Expresions
env.re_file_foramt = re.compile(r'^(?P<year>\d{4})-(?P<month>\d{2})-'
                                r'(?P<day>\d{2})-(?P<slug>[-\w]+)\.'
                                r'(?P<format>\w+)$')
