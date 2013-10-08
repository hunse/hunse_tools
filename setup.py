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
    # packages=['hunse_tools'],
    py_modules=['', 'numpy'],
    scripts=[],
    url="https://github.com/hunse/hunse_tools",
    license="LICENSE",
    description="Miscellaneous tools for Python",
    long_description=open('README.md').read(),
    requires=[],
    # test_suite='hunse_tools.tests',
)
