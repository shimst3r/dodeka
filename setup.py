#!/usr/bin/env python3
"""
Copyright (c) 2019, Nils P. Müller <shimst3r@gmail.com>
All rights reserved.

This file is part of dodeka.

License: MIT, see https://opensource.org/licenses/MIT
"""

from setuptools import setup

__version__ = "0.1.1"

with open("README.md", "r", encoding="utf-8") as f_in:
    LONG_DESCRIPTION = f_in.read()

PACKAGES = ["dodeka"]

REQUIRES = ["Click", "jinja2"]

setup(
    author="Nils P. Müller",
    author_email="shimst3r@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    description="Twelve-Factor App Checker",
    download_url="https://github.com/shimst3r/dodeka/archive/0.1.1.tar.gz",
    install_requires=REQUIRES,
    keywords=["cli", "tool", "twelvefactor"],
    license="MIT",
    long_description=LONG_DESCRIPTION,
    name="dodeka",
    packages=PACKAGES,
    url="https://github.com/shimst3r/dodeka",
    version=__version__,
)
