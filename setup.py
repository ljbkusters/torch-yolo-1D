#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup.py
@author Luc Kusters
@date 24-12-2023
"""

import setuptools

from yolo1d import __metadata

with open("README.md", "r") as fhandle:
    long_description = fhandle.read()

setuptools.setup(
        name=__metadata.NAME,
        version=__metadata.VERSION,
        description=__metadata.DESCRIPTION,
        long_description=long_description,
        author=", ".join(__metadata.AUTHORS),
        email=", ".join(__metadata.EMAILS),
        url="https://github.com/ljbkusters/torch-yolo-1D",
        packages=["yolo1d"],
        requires=__metadata.DEPENDENCIES,
        extras_require={
            "dev": __metadata.DEV_DEPENDENCIES,
            },
        )
