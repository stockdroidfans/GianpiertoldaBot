# GianpiertoldaBot
# © 2021 Stockdroid Fans

'''
	# [GianpiertoldaBot](https://github.com/stockdroidfans/Gianpiertolda)

	© 2019–2021 [Stockdroid Fans](https://github.com/stockdroidfans)
	Licensed under the MIT [MIT License](https://github.com/stockdroidfans/Gianpiertolda/blob/main/LICENSE)

	---

	Host for `gianpiertolda.User`

	```
	from gianpiertolda import User
	```
'''

#——————————————————#———————————————————#——————————————————#———————————————————#———————————————————#

# Imports
''' System '''
import sys, os, time, logging, traceback
from ..exceptions.unsupported import UnsupportedError

''' Libraries '''
import utils, json, html, random, hashlib, rich
from rich import print
from rich.logging import RichHandler

''' Platforms '''
import pyrogram
import discord

#——————————————————#———————————————————#——————————————————#———————————————————#———————————————————#

class User:
	class Telegram(pyrogram.types.User):
		def __init__(self,
		*args, **kwargs):
			self.id = self.id
			self.username = self.username
			self.first_name = self.first_name
			self.last_name = self.last_name
			self.full_name = self.first_name, self.last_name if self.last_name else self.first_name
		
		@property
		def title(self,
		*args, **kwargs) -> str:
			if self.username: return f'@{self.username}'
			return self.full_name
		
		@property
		def is_bot(self,
		*args, **kwargs) -> bool:
			if self.is_bot: return True
			return False
		
		def bot(self,
		*args, **kwargs):
			if self.bot: return self.bot
			return None
		
		@property
		def permissions(self,
		*args, **kwargs) -> dict:
			return {
				'can_join_groups': self.can_join_groups,
				'group_privacy': self.can_read_all_group_messages,
				'inline_queriable': self.supports_inline_queries
			}

	class Discord(discord.User):
		def __init__(self,
		*args, **kwargs):
			self.id = self.id
			self.username = self.name
			self.first_name = self.name
			self.last_name = ''
			self.full_name = self.name
		
		@property
		def title(self,
		*args, **kwargs) -> str:
			if self.display_name: return self.display_name
			return self.name
		
		@property
		def is_bot(self,
		*args, **kwargs) -> bool:
			if self.bot: return True
			return False
		
		def bot(self,
		*args, **kwargs) -> discord.Client:
			if self.bot: return self.bot
			return None
		
		@property
		def permissions(self,
		*args, **kwargs):
			raise UnsupportedError(f'discord does not provide sufficient information for user permissions')