#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="pytest-extra-durations",
    version="0.1.0",
    author="Gabriel de Marmiesse",
    author_email="gabrieldemarmiesse@gmail.com",
    maintainer="Gabriel de Marmiesse",
    maintainer_email="gabrieldemarmiesse@gmail.com",
    license="MIT",
    url="https://github.com/gabrieldemarmiesse/pytest-extra-durations",
    description="A pytest plugin to get durations on a per-function basis and per module basis.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    py_modules=["pytest_extra_durations"],
    python_requires=">=3.6",
    install_requires=["pytest>=3.5.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["extra-durations = pytest_extra_durations",],},
)
