#!/usr/bin/env python
import os
import subprocess
import sys
from setuptools import setup, find_packages

if os.path.exists('relic'):
    sys.path.insert(1, 'relic')
    import relic.release
else:
    try:
        import relic.release
    except ImportError:
        try:
            subprocess.check_call(['git', 'clone',
                'https://github.com/jhunkeler/relic.git'])
            sys.path.insert(1, 'relic')
            import relic.release
        except subprocess.CalledProcessError as e:
            print(e)
            exit(1)


version = relic.release.get_info()
relic.release.write_template(version, 'nictools')

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
