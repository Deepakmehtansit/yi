#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from lk.skeleton import fib

__author__ = "Deepakmehtansit"
__copyright__ = "Deepakmehtansit"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
