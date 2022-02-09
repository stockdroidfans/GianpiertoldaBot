# GianpiertoldaBot
# © 2021 Stockdroid Fans

'''
	# [GianpiertoldaBot](https://github.com/stockdroidfans/Gianpiertolda)
	© 2019–2021 [Stockdroid Fans](https://github.com/stockdroidfans)
	Licensed under the MIT [MIT License](https://github.com/stockdroidfans/Gianpiertolda/blob/main/LICENSE)
	---
	Host for `gianpiertolda.Chat`
	```
	from gianpiertolda import Chat
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

class Chat:
	class Telegram(pyrogram.types.Chat):
		def __init__(self,
		*args, **kwargs):
			self.id = self.id
			self.name = self.username
			self.title = self.title

		@property
		def link(self,
			name: str = None,
			primary: bool = False,
			timeout: int = None, max_uses: int = None,
		*args, **kwargs) -> str:
			kwargs = dict(
				is_primary = primary,
				expire_date = timeout, member_limit = max_uses,
				**kwargs
			)