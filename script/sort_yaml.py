#!/usr/bin/env python3
"""
# Sort YAML

Sort the contents of some YAML files.

## Requires

* pyyaml
"""

from collections import OrderedDict
from os.path import dirname, realpath, join

import yaml


def sort_yaml_file(yaml_file):
    with open(yaml_file, 'r') as fobj:
        raw = fobj.read()
        data = yaml.load(raw)

    return yaml.dump(data, default_flow_style=False, explicit_start=True)


def main():
    data_dir = join(dirname(realpath(__file__)), '../source/_data')

    # chdir(data_dir)
    # yaml_files = iglob('*.yml')

    yaml_files = [join(data_dir, 'tags.yml'), join(data_dir, 'navigation.yml'),
                  join(data_dir, 'categories.yml')]

    for yaml_file in yaml_files:
        raw = sort_yaml_file(yaml_file)

        with open(yaml_file, 'w') as fobj:
            fobj.write(raw.replace('\n-', '\n\n-'))


if __name__ == '__main__':
    main()
