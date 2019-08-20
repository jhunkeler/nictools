#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

PACKAGENAME = 'nictools'

setup(
    name=PACKAGENAME,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'astropy>=1.0',
        'numpy>=1.9',
        'scipy>=0.16',
        'stsci.imagestats',
        'stsci.tools',
    ],
    extras_require={
        'docs': [
            'sphinx',
            'numpydoc',
        ]
    },
    packages=find_packages(),
    package_data={
        '': ['LICENSE.txt'],
        PACKAGENAME: ['SP_LICENSE'],
    },
    entry_points={
        'console_scripts': [
            '{0}_CalTempFromBias = {0}.CalTempFromBias:main'.format(PACKAGENAME),
            '{0}_rnlincor = {0}.rnlincor:main'.format(PACKAGENAME),
            '{0}_makemedmask = {0}.makemedmask:main'.format(PACKAGENAME),
            '{0}_nic_rem_persist = {0}.nic_rem_persist:main'.format(PACKAGENAME),
            '{0}_finesky = {0}.finesky:main'.format(PACKAGENAME),
        ],
    },
    author='Vicki Laidler, David Grumm',
    author_email='help@stsci.edu',
    description='Python Tools for NICMOS Data',
    url='https://github.com/spacetelescope/nictools',
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
