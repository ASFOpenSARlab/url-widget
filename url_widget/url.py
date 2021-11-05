import ipywidgets as widgets
from traitlets import Unicode

from ._version import version

# See js/lib/widget.js for the frontend counterpart to this file.

@widgets.register
class URLWidget(widgets.DOMWidget):
    """A widget to fetch the current notebook URL."""

    # Name of the widget view class in front-end
    _view_name = Unicode('URLView').tag(sync=True)

    # Name of the widget model class in front-end
    _model_name = Unicode('URLModel').tag(sync=True)

    # Name of the front-end module containing widget view
    _view_module = Unicode('url-widget').tag(sync=True)

    # Name of the front-end module containing widget model
    _model_module = Unicode('url-widget').tag(sync=True)

    # Version of the front-end module containing widget view
    _view_module_version = Unicode(version).tag(sync=True)
    # Version of the front-end module containing widget model
    _model_module_version = Unicode(version).tag(sync=True)

    # Widget specific property.
    # Widget properties are defined as traitlets. Any property tagged with `sync=True`
    # is automatically synced to the frontend *any* time it changes in Python.
    # It is synced back to Python from the frontend *any* time the model is touched.
    value = Unicode('').tag(sync=True)
