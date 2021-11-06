#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Alex Lewandowski.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget
from traitlets import Unicode
from ._frontend import module_name
from ._version import version


class URLWidget(DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('URLModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(version).tag(sync=True)
    _view_name = Unicode('URLView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(version).tag(sync=True)

    value = Unicode('').tag(sync=True)
