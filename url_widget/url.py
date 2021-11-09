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
from ._version import __version__

class URLWidget(DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('URLModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(__version__).tag(sync=True)
    _view_name = Unicode('URLView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(__version__).tag(sync=True)

    value = Unicode('URL not updated Python-side yet. To update URL,  display(url_widget_object)').tag(sync=True)
