#!/usr/bin/python
"""
walk module for dir_walk
"""

from logging import getLogger

from os.path import isdir, join
from os import listdir

log = getLogger(__name__)


def list_contents(structure=dict(), curr_dir=None):
    """
    :param structure:
        directory structure
        default: dict()
    :param curr_dir: (string)
        path to root of directory to search
    :returns (dict)
        dictionary containing directories as keys and lists as values.

        {root: [ file1, file2 ],
         subdir1: [file1, file2]}
    """
    structure[curr_dir] = list()
    if curr_dir is None:
        return structure
    else:
        contents = listdir(curr_dir)
        if len(contents) == 0:
            return structure
        for cont in contents:
            full_path = join(curr_dir, cont)
            if isdir(full_path):
                structure[full_path] = {}
                result = list_contents(structure, full_path)
            else:
                structure[curr_dir].append(full_path)

        return structure


