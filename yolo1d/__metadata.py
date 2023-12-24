#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__version.py
@author Luc Kusters
@date 24-12-2023
"""

VERSION = "0.1.0"
NAME = "Torch YOLO-1D"
DESCRIPTION = ("A PyTorch implementation of the YOLO network capable of"
               "handling 1D inputs.")
AUTHORS_AND_EMAILS = {"Luc Kusters": "ljbkusters@gmail.com",
                      }
AUTHORS = list(AUTHORS_AND_EMAILS.keys())
EMAILS = list(AUTHORS_AND_EMAILS.values())
DEPENDENCIES = [
    "torch",
    "numpy",
    "tqdm",
    "matplotlib",
    ]
DEV_DEPENDENCIES = [
    "pytest",
    "sphinx",
    "sphinx-rtd-theme",
    ]
