#!/usr/bin/env python
#
#  Copyright (c) 2013, Corey Goldberg (cgoldberg@gmail.com)
#
#  license: GNU LGPL
#
#  This file is part of: ystockquote
#  https://github.com/cgoldberg/ystockquote
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#


"""setup/install script for ystockquote"""


import os
from distutils.core import setup

from ystockquote import __version__

this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.rst')) as f:
    LONG_DESCRIPTION = '\n' + f.read()

setup(
    name='ystockquote',
    version=__version__,
    py_modules=['ystockquote'],
    author='Corey Goldberg',
    author_email='cgoldberg _at_ gmail.com',
    description='retrieve stock quote data from Yahoo Finance',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/cgoldberg/ystockquote',
    download_url='http://pypi.python.org/pypi/ystockquote',
    keywords='stocks stockmarket yahoo finance'.split(),
    license='Apache v2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Investment',
    ]
)
