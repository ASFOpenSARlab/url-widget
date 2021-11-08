#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function
from glob import glob
import os
from os.path import join as pjoin
import re
from setuptools import setup, find_packages


from jupyter_packaging import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    combine_commands,
    get_version,
)

HERE = os.path.dirname(os.path.abspath(__file__))




# The name of the project
name = 'url_widget'

# # Get the version
# version = get_version(pjoin(name, '_version.py'))

def update_version():
    # read setuptools-scm version file
    with open("url_widget/_v.py", 'r') as f:
        scm_lines = f.readlines()

    # read old _version.py
    with open("url_widget/_version.py", 'r') as f:
        old_version_lines = f.readlines()

    # Find new scm version
    for line in scm_lines:
        regex = "(?<=version_tuple = )\(.{7,50}\)"
        version = re.search(regex, line)
        if version:
            version = version.group(0)
            break

    # Update version to new scm version
    new_version_lines = list()
    for line in old_version_lines:
        if "version_info = " in line:
            line = f"version_info = {version}\n"
        new_version_lines.append(line)
    with open("url_widget/_version.py", 'w') as f:
        f.writelines(new_version_lines)


# Representative files that should exist after a successful build
jstargets = [
    pjoin(HERE, name, 'nbextension', 'index.js'),
    pjoin(HERE, 'lib', 'plugin.js'),
]


package_data_spec = {
    name: [
        'nbextension/**js*',
        'labextension/**'
    ]
}


data_files_spec = [
    ('share/jupyter/nbextensions/url_widget', 'url_widget/nbextension', '**'),
    ('share/jupyter/labextensions/url-widget', 'url_widget/labextension', '**'),
    ('share/jupyter/labextensions/url-widget', '.', 'install.json'),
    ('etc/jupyter/nbconfig/notebook.d', '.', 'url_widget.json'),
]


cmdclass = create_cmdclass('jsdeps', package_data_spec=package_data_spec,
    data_files_spec=data_files_spec)
cmdclass['jsdeps'] = combine_commands(
    install_npm(HERE, build_cmd='build:prod'),
    ensure_targets(jstargets),
)


setup_args = dict(
    name            = name,
    description     = 'A custom Jupyter widget that provides thecurrent url of the notebook',
    use_scm_version = True,
    setup_requires  = ['setuptools_scm'],
    # update_version  = update_version(),
    # version         = version,
    scripts         = glob(pjoin('scripts', '*')),
    cmdclass        = cmdclass,
    packages        = find_packages(),
    author          = 'Alex Lewandowski',
    author_email    = 'aflewandowski@alaska.edu',
    url             = 'https://github.com/ASFOpenSARlab/url_widget',
    license         = 'BSD',
    platforms       = "Linux, Mac OS X, Windows",
    keywords        = ['Jupyter', 'Widgets', 'IPython'],
    classifiers     = [
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Jupyter',
    ],
    include_package_data = True,
    python_requires=">=3.6",
    install_requires = [
        'ipywidgets>=7.0.0',
    ],
    extras_require = {
        'test': [
            'pytest>=4.6',
            'pytest-cov',
            'nbval',
        ],
        'examples': [
            # Any requirements for the examples to run
        ],
        'docs': [
            'jupyter_sphinx',
            'nbsphinx',
            'nbsphinx-link',
            'pytest_check_links',
            'pypandoc',
            'recommonmark',
            'sphinx>=1.5',
            'sphinx_rtd_theme',
        ],
    },
    entry_points = {
    },
)


if __name__ == '__main__':
    setup(**setup_args)
    update_version()
