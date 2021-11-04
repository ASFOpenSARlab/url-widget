url-widget
===============================

A Jupyter widget to fetch the current notebook's URL

Installation
------------

To install use pip:

    $ pip install url_widget

For a development installation (requires [Node.js](https://nodejs.org) and [Yarn version 1](https://classic.yarnpkg.com/)),

    $ git clone https://github.com/ASFOpenSARlab/url-widget.git
    $ cd url-widget
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --overwrite --sys-prefix url_widget
    $ jupyter nbextension enable --py --sys-prefix url_widget

When actively developing your extension for JupyterLab, run the command:

    $ jupyter labextension develop --overwrite url_widget

Then you need to rebuild the JS when you make a code change:

    $ cd js
    $ yarn run build

You then need to refresh the JupyterLab page when your javascript changes.
