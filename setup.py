#!/usr/bin/env python3
"""Setup file for pyjacklib."""

from os.path import dirname, join

from setuptools import setup


def read(*args):
    return open(join(dirname(__file__), *args)).read()


PKGDIR = 'jacklib'
version = {}
exec(read(PKGDIR, 'version.py'), {}, version)
setup(version=version["__version__"], packages=[PKGDIR])
