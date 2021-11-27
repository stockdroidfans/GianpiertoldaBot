# GianpiertoldaBot
# © 2021 Stockdroid Fans

'''
  # [GianpiertoldaBot](https://github.com/stockdroidfans/Gianpiertolda)
  
  © 2021 Stockdroid Fans
  Licensed under the [MIT License](https://github.com/stockdroidfans/Gianpiertolda/blob/main/LICENSE)\n\n

  ---

  ```bash
    python3 -m build
  ```
  ```powershell
    py -m build
  ```
'''

#——————————————————#———————————————————#——————————————————#———————————————————#———————————————————#

# Imports
''' System '''
import sys, os, time, logging, traceback

''' Libraries '''
import json, html, random, hashlib, rich
from rich import print
from rich.logging import RichHandler

''' setuptools '''
import setuptools

#——————————————————#———————————————————#——————————————————#———————————————————#———————————————————#

# Load settings
with open('README.md') as README: __README__ = README.read()
config = {
  'name': 'gianpiertolda',
  'author': 'Stockdroid Fans', 'author_email': 'stockdroidfans@gmail.com',
  'description': 'Il bot multipiattaforma marso',
  'long_description': __README__,
  'long_description_content_type': 'text/markdown',
  'url': 'https://bot.gianpiertolda.it/', 'project_urls': {
    'Home': 'https://bot.gianpiertolda.it/',
    'Telegram': 'https://t.me/GianpiertoldaBot',
    'Source': 'https://github.com/stockdroidfans/Gianpiertolda/',
    '.git repo': 'https://github.com/stockdroidfans/Gianpiertolda.git'
  },
  'classifiers': [
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  'package_dir': {'': 'src'}, 'python_requires': '>=3.8'
}

# Initialize
Setup = setuptools.setup(**config, packages = setuptools.find_packages(where = config['package_dir']['']))