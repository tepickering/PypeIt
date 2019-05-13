"""
Module to run tests on arcoadd
"""
import os

import pytest
import numpy as np

from pypeit import msgs
from pypeit.tests.tstutils import cooked_required


@cooked_required
def test_cooked_version():
    return

    # TODO: Use pygit2 to both add the branch name when constructing
    # Cooked and here to check that the branch is correct?

    # Load up the version
    v_file = os.path.join(os.getenv('PYPEIT_DEV'), 'Cooked', 'version')
    with open(v_file) as f:
        tmp = f.readlines()
    value = float(tmp[-1].strip())
    # Test
    # TODO: Shouldn't this be an exact version?
    assert value >= 1.0
