# -*- coding: utf-8 -*-
import os
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

# Prase Jekyll Config
with open(env.config_base_file, 'r') as fobj:
    env.config = yaml.load(fobj.read())

with open(env.config_local_file,'r') as fobj:
    env.config_local = merge_dicts(env.config, yaml.load(fobj.read()))

with open(env.config_prod_file,'r') as fobj:
    env.config_prod = merge_dicts(env.config, yaml.load(fobj.read()))

with open(env.config_stag_file,'r') as fobj:
    env.config_stag = merge_dicts(env.config, yaml.load(fobj.read()))
