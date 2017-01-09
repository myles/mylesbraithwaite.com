# -*- coding: utf-8 -*-

from ordereddict import OrderedDict
from os.path import dirname, realpath, join

import yaml
from fabric.api import env, task


def sort_yaml_file(yaml_file):
    with open(yaml_file, 'r') as fobj:
        raw = fobj.read()
        data = yaml.load(raw)

    return yaml.dump(data, default_flow_style=False, explicit_start=True)


@task(default=True)
def sort_yaml():
    data_dir = join(env.root_dir, 'source/_data')

    # chdir(data_dir)
    # yaml_files = iglob('*.yml')

    yaml_files = [join(data_dir, 'tags.yml'), join(data_dir, 'navigation.yml'),
                  join(data_dir, 'categories.yml')]

    for yaml_file in yaml_files:
        raw = sort_yaml_file(yaml_file)

        with open(yaml_file, 'w') as fobj:
            fobj.write(raw.replace('\n-', '\n\n-'))
