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

class Media:
	class Telegram(pyrogram.types.InputMedia):
		def __init__(self,
			uri: str,
			caption: str = '',
			supports_streaming: bool = True,
		*args, **kwargs):
			self.uri = uri
			self.caption = caption
			self.supports_streaming = supports_streaming

			self.media = super().__init__(self.uri, self.caption)