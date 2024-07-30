#!/usr/bin/env python

from distutils.core import setup

setup(
    name='sentinel2video',
    version='1.0',
    description='Convert images from Sentinel 2 satellite to video using Google Earth Engine',
    author='Eren Eroğlu',
    author_email='108634315+ereneroglum@users.noreply.github.com',
    url='https://github.com/ereneroglum/sentinel2video',
    scripts = [ 'sentinel2video.py' ],
    install_requires = [
        'earthengine-api',
        'setuptools'
    ]
)

