#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

LONG_DESCRIPTION = """
""".strip()

SHORT_DESCRIPTION = """
A library for automatically debug sql in Django.
""".strip()

DEPENDENCIES = [
    'Pygments==2.2.0',
    'sqlparse==0.2.3'
]

TEST_DEPENDENCIES = [
    'coverage==4.4.1'
]


setup(
    name='ddquery',
    version='0.1',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url='https://github.com/elinaldosoft/ddquery.git',
    download_url='https://github.com/elinaldosoft/ddquery/archive/0.1.zip',
    author='Elinaldo Monteiro',
    author_email='elinaldo.java@gmail.com',
    license='GNU General Public License v3.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    py_modules=['ddquery'],
    install_requires=DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,
)
