#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='fuzzyraft',
    version='0.1.0',
    description="Fuzzy Raft is a Python implementation of Raft consensus algorithm",
    long_description=readme + '\n\n' + history,
    author="Elias Dorneles",
    author_email='eliasdorneles@gmail.com',
    url='https://github.com/eliasdorneles/fuzzyraft',
    packages=[
        'fuzzyraft',
    ],
    package_dir={'fuzzyraft':
                 'fuzzyraft'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='fuzzyraft',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
