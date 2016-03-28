#!/usr/bin/env python
import recon.release
from setuptools import setup, find_packages


version = recon.release.get_info()
recon.release.write_template(version, 'nictools')


setup(
    name = 'nictools',
    version = version.pep386,
    author = 'Vicki Laidler, David Grumm',
    author_email = 'help@stsci.edu',
    description = 'Python Tools for NICMOS Data',
    url = 'https://github.com/spacetelescope/nictools',
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'astropy',
        'nose',
        'numpy',
        'pytools',
        'scipy',
        'sphinx',
        'stsci.sphinxext',
        'stsci.tools',
    ],
    packages = find_packages(),
    package_data = {
        'nictools': [
            'pars/*',
            'tests/*.fits',
            '*.rules',
            'LICENSE.txt'
        ]
    },
)
