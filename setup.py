#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Frootlab
# Copyright (C) 2013-2019 Patrick Michl
#
# This file is part of Frootlab Vivid Node, https://www.frootlab.org/rian
#
#  Vivid Node is free software: you can redistribute it and/or modify it under
#  the terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Vivid Node is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License along with
#  Vivid Node. If not, see <http://www.gnu.org/licenses/>.
#
"""Setuptools based installation."""

__copyright__ = '2019 Frootlab'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

import pathlib
import re
import setuptools

def install() -> None:
    """Setuptools based installation script."""

    # Parse top level module for attributes
    text = pathlib.Path('./vivid/node/__init__.py').read_text()
    pattern = r"^[ ]*__([^\d\W]\w*)__[ ]*=[ ]*['\"]([^'\"]*)['\"]"
    matches = re.finditer(pattern, text, re.M)
    pkg = {str(m.group(1)): str(m.group(2)) for m in matches}

    # Install package
    setuptools.setup(
        name='vivid_node',
        version=pkg['version'],
        description=pkg['description'],
        long_description=pathlib.Path('.', 'README.md').read_text(),
        long_description_content_type='text/markdown',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3',
    		'Programming Language :: Python :: 3.7',
            'Operating System :: OS Independent',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'Topic :: Scientific/Engineering :: Information Analysis',
            'Topic :: Database :: Database Engines/Servers',
            'Topic :: Software Development :: Libraries :: Python Modules'],
        keywords=(
            'data-analysis '
            'enterprise-data-analysis '
            'data-science '
            'collaborative-data-science '
            'data-visualization '
            'machine-learning '
            'artificial-intelligence '
            'artificial-neural-networks '
            'deep-learning '
            'probabilistic-graphical-model '),
        url=pkg['url'],
        author=pkg['author'],
        author_email=pkg['email'],
        license=pkg['license'],
        packages=setuptools.find_namespace_packages(include=['vivid.*']),
        python_requires='>=3.7',
        install_requires=['rian>=' + pkg['version']],
        zip_safe=True)

if __name__ == '__main__':
    install()
