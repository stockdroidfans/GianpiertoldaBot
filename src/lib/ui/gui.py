# GianpiertoldaBot
# © 2021 Stockdroid Fans

'''
	# [GianpiertoldaBot](https://github.com/stockdroidfans/Gianpiertolda)

	© 2019–2021 [Stockdroid Fans](https://github.com/stockdroidfans)
	Licensed under the MIT [MIT License](https://github.com/stockdroidfans/Gianpiertolda/blob/main/LICENSE)

	---

	Host for `gianpiertolda.GUI`

	```
	from gianpiertolda import GUI
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

class Buttons:
	class Telegram:
		def __init__(self,
			markup_type: str('inline') or str('reply') = 'reply',
		*args, **kwargs):
			Button: pyrogram.types.KeyboardButton
			if markup_type == 'inline':
				Button = pyrogram.types.InlineKeyboardButton
				for button in kwargs:
					self.table = []
					self.table.append(
						Button(
							text = button,
							url = kwargs[button]
						)
					)
			if markup_type == 'reply':
				Button = pyrogram.types.KeyboardButton
				for button in args:
					self.table = []
					self.table.append(Button(text = button))
		
		def get(self,
		*args, **kwargs) -> list:
			return self.table

class Gui:
	class Telegram:
		class keyboard:
			def reply(self,
				table: Buttons,
			*args, **kwargs) -> pyrogram.types.ReplyKeyboardMarkup:
				return pyrogram.types.ReplyKeyboardMarkup(table.get())
			
			def inline(self,
				table: Buttons,
			*args, **kwargs) -> pyrogram.types.InlineKeyboardMarkup:
				return pyrogram.types.InlineKeyboardMarkup(table.get())