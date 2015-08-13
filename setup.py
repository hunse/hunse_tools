#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    try:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup
    except Exception, e:
        print "Forget setuptools, trying distutils..."
        from distutils.core import setup

setup(
    name="hunse_tools",
    version="0.1.0",
    author="Eric Hunsberger",
    author_email="ehunsber@uwaterloo.ca",
    packages=['hunse_tools'],
    scripts=[],
    url="https://github.com/hunse/hunse_tools",
    license="MIT",
    description="Miscellaneous tools for Python",
    long_description=open('README.md').read(),
    setup_requires=[
        "numpy>=1.6",
    ],
    install_requires=[
        "numpy>=1.6",
    ],
)
