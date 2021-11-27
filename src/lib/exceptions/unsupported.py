# GianpiertoldaBot
# © 2021 Stockdroid Fans

'''
	# [GianpiertoldaBot](https://github.com/stockdroidfans/Gianpiertolda)

	© 2019–2021 [Stockdroid Fans](https://github.com/stockdroidfans)
	Licensed under the MIT [MIT License](https://github.com/stockdroidfans/Gianpiertolda/blob/main/LICENSE)

	---

	Host for `gianpiertolda.exceptions.UnsupportedError`

	```
	from gianpiertolda import exceptions

	raise exceptions.unsupported.UnsupportedError(f'unsupported operation')
	```
'''

#——————————————————#———————————————————#——————————————————#———————————————————#———————————————————#

# Imports
''' System '''
import sys, os, time, logging, traceback

''' Libraries '''
import utils, json, html, random, hashlib, rich
from rich import print
from rich.logging import RichHandler

''' Platforms '''
import pyrogram
import discord

#——————————————————#———————————————————#——————————————————#———————————————————#———————————————————#

class UnsupportedError(Exception): pass