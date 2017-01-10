# -*- coding: utf-8 -*-
"""Fabic Utilities."""


def merge_dicts(*dict_args):
    """
    Merge multiple Dictonaries.

    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result
