#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:37:42 2020

@author:
Maximilian N. Günther
MIT Kavli Institute for Astrophysics and Space Research, 
Massachusetts Institute of Technology,
77 Massachusetts Avenue,
Cambridge, MA 02109, 
USA
Email: maxgue@mit.edu
Web: www.mnguenther.com
"""

from setuptools import setup, find_packages





setup(
    name = 'tess_infos',
    packages = find_packages(),
    version = '0.1.0',
    description = 'A global inference framework for photometry and RV',
    author = 'Maximilian N. Günther & Tansu Daylan',
    author_email = 'maxgue@mit.edu',
    url = 'https://github.com/MNGuenther/allesfitter',
    download_url = 'https://github.com/MNGuenther/allesfitter',
    license='MIT',
    classifiers=['Development Status :: 4 - Beta', #3 - Alpha / 4 - Beta / 5 - Production/Stable
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python'],
    #install_requires=['feather-format>=0.4.1'],
    include_package_data = False
    )


