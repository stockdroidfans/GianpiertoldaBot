# GianpiertoldaBot
# © 2021 Stockdroid Fans

'''
	# [GianpiertoldaBot](https://github.com/stockdroidfans/Gianpiertolda)

	© 2019–2021 [Stockdroid Fans](https://github.com/stockdroidfans)
	Licensed under the MIT [MIT License](https://github.com/stockdroidfans/Gianpiertolda/blob/main/LICENSE)

	---

	Host for `gianpiertolda.Command`

	```
	from gianpiertolda import Command
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

class CommandManifest:
	def __init__(self,
		_list: list,
		prefix: list, triggers: list,
		needs_match: bool,
	*args, **kwargs):
		self.list: list = _list
		self.list: list = utils.get_true(self.list)

		self.prefix: list = prefix
		self.triggers: list = utils.get_true(triggers)
		self.needs_match: bool = needs_match

class Command:
	def __init__(self,
		name: str, _id: int = 00,
		description: str = None,
		config: CommandManifest = None,
	*args, **kwargs):
		self.id: int = _id

		self.config: CommandManifest = config
		if not config:
			self.config = CommandManifest(
				_list = [],
				prefix = ['/'], triggers = [self.name],
				needs_match = True
			)
		if not len(config.list): config.list = [self]
		
		if not _id: self.id = self.config.list.index(self)

		self.name: str = name
	
	def get_all(self,
	*args, **kwargs):
		return self.config.list
	
	def detect(self,
		text: str,
	*args, **kwargs):
		for i in range(len(self.config.list)):
			self.command = self.config.list[i]
			if self.command in text:
				if text in [self.command, self.config.prefix[i] + self.command]:
					return True
				if not self.config.needs_match:
					return True
			return False