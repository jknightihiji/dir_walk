"""
test_walk module for dir_walk
"""

# Standard library imports
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from logging import getLogger


import pytest
from pprint import pformat
from dir_walk.walk import list_contents

log = getLogger(__name__)


def test_empty_dir(tmpdir):
    """
    Test the case where directory is empty
    """
    root = tmpdir.mkdir('root')
    structure = dict()
    result = list_contents(structure, root.strpath)

    print(pformat(result))

    assert root in structure
    assert structure[str(root)] == []


def test_file_list(tmpdir):
    """
    Test case  for single level directory structure
    """
    root = tmpdir.mkdir('root')
    file1 = root.join('file1')
    file2 = root.join('file2')
    file1.write('')
    file2.write('')
    structure = dict()
    result = list_contents(structure, root.strpath)

    print(pformat(result))

    assert root in structure
    assert structure[ root.strpath ] == [ file1.strpath, file2.strpath ]


def test_2_deep_list(tmpdir):
    """
    Test the case 2 level directory structure
    """
    root = tmpdir.mkdir('root')
    file1 = root.join('file1')
    file2 = root.join('file2')
    file1.write('')
    file2.write('')

    sub_dir = root.mkdir('sub1')
    file3 = sub_dir.join('file3')
    file3.write('')
    file4 = sub_dir.join('file4')
    file4.write('')
    structure = dict()
    result = list_contents(structure, root.strpath)

    print(pformat(result))

    assert root in structure
    assert file1.strpath in structure[root.strpath]
    assert file2.strpath in structure[root.strpath]
    assert file3.strpath in structure[sub_dir.strpath]
    assert file4.strpath in structure[sub_dir.strpath]


