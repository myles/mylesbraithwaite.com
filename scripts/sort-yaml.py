#!/usr/bin/env python3

from os import chdir
from glob import iglob
from os.path import dirname, realpath, join

import yaml


def sort_yaml_file(yaml_file):
    with open(yaml_file, 'r') as fobj:
        raw = fobj.read()
        data = yaml.load(raw)

    data.sort()

    return yaml.dump(data)


def main():
    data_dir = join(dirname(realpath(__file__)), '../source/_data')

    chdir(data_dir)
    yaml_files = iglob('*.yml')

    for yaml_file in yaml_files:
        raw = sort_yaml_file(yaml_file)

        with open(yaml_file, 'w') as fobj:
            fobj.write(raw)


if __name__ == '__main__':
    main()
