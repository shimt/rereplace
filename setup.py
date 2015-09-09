#! /usr/bin/env python3
# coding: utf-8

import platform

from setuptools import setup

setup_kwargs = dict(
    name='rereplace',
    version='1.0',
    description='Regex Replacing Tool',
    author='Shinichi MOTOKI',
    author_email='shinichi-motoki@overruns.org',
    url='http://gitlab.overruns.org/shinichi-motoki/rereplace',
    scripts=['rereplace.py'],
)

if platform.system() == 'Windows':
    import py2exe

    setup_kwargs.update(dict(
        options={
            "py2exe": {
                "bundle_files": 1,
                "includes": [
                ],
                "excludes": [
                    '_dummy_thread',
                    '_ssl',
                    '_threading_local',
                    'base64',
                    'bz2',
                    'calendar',
                    'distutils',
                    'doctest',
                    'dummy_threading',
                    'email',
                    'getopt',
                    'linecache',
                    'logging',
                    'optparse',
                    'pdb',
                    'pickle',
                    'posixpath',
                    'pyreadline',
                    'quopri',
                    'select',
                    'selectors',
                    'string',
                    'stringprep'
                    'subprocess'
                    'threading',
                    'traceback',
                    'unittest',
                ],
                "dll_excludes": [
                ],
            }
        },
        console=['rereplace.py'],
        zipfile=None,
    ))

setup(**setup_kwargs)
