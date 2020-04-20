#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import setup

current_dir = Path(__file__).parent.resolve()

with open(current_dir / 'README.md', encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name = 'memo',
    version = '0.1',
    author = 'furkanonder',
    author_email = 'furkanonder@protonmail.com',
    packages = ['memo'],
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/furkanonder/memo'
)
