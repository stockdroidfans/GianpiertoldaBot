# GianpiertoldaBot
# © 2021 Stockdroid Fans

'''
	# [GianpiertoldaBot](https://github.com/stockdroidfans/Gianpiertolda)

	© 2019–2021 [Stockdroid Fans](https://github.com/stockdroidfans)
	Licensed under the MIT [MIT License](https://github.com/stockdroidfans/Gianpiertolda/blob/main/LICENSE)
'''

#——————————————————#———————————————————#——————————————————#———————————————————#———————————————————#

# Imports
''' System '''
import sys, os, time, logging, asyncio, traceback, shutil

''' Libraries '''
import utils, gbot, json, html, random, hashlib, rich
from rich import print
from rich.logging import RichHandler

''' Platforms '''
import pyrogram
import discord

''' Objects '''
from lib import *
from lib.base import *
from lib.ui import *

from lib.base.message import Message
from lib.base.media import Media
from lib.base.user import User
from lib.base.chat import Chat

from lib.ui.command import CommandManifest, Command
from lib.ui.gui import Buttons, Gui

#——————————————————#———————————————————#——————————————————#———————————————————#———————————————————#

class Bot:
	def __init__(self,
		name: str = 'GianpiertoldaBot',
		logger = {
			'format': '%(asctime)s | %(name)s: [%(levelname)s] %(message)s',
			'level': logging.INFO,
			'handlers': [RichHandler()]
		},
		motd: str = None,
	*args, **kwargs):
		self.name = name
		self.logging = logging.basicConfig(**logger)
		self.logger = logging.getLogger(__name__)
	
	def debug(self,
	*args, **kwargs):
		self.logger.level = logging.DEBUG

	class Telegram(pyrogram.client.Client):
		def __init__(self,
			api_id: int, api_hash: str,
			client_name: str,
			token: str = None,
		*args, **kwargs):
			self.api_id = api_id
			self.api_hash = api_hash
			self.token = token
			self.client_name = client_name
			self.client = pyrogram.client.Client(
				api_id = self.api_id, api_hash = self.api_hash,
				bot_token = self.token,
				session_name = self.client_name,
				*args, **kwargs
			)
		
		def get(self,
		*args, **kwargs) -> pyrogram.client.Client:
			return self.client
		
		def on(self,
		*args, **kwargs):
			return self.client.start(*args, **kwargs)
		
		def off(self,
		*args, **kwargs):
			return self.client.stop(*args, **kwargs)
		
		def user(self,
		*args, **kwargs) -> User:
			return User.Telegram(
				self.client.get_me(*args, **kwargs)
			)
		
		def send(self,
			chat: pyrogram.types.Chat or int or str,
			text: str = '', media: Media or str = None,
			parser: str = 'html',
			entities: list = None,
			embed: bool = True, notify: bool = True,
			reply_to: pyrogram.types.Message or int = None, markup: str = '',
		*args, **kwargs) -> Message:
			chat_id: int = None
			if type(chat) == pyrogram.types.Chat: chat_id = chat.id
			if type(chat) == int: chat_id = chat

			if type(media) == str: media = Media.Telegram(media)

			reply_to_message_id: int = None
			if type(reply_to) == pyrogram.types.Message: reply_to_message_id = reply_to.message_id
			if type(reply_to) == int: reply_to_message_id = reply_to

			caption: str = text
			if media and media.caption: caption = media.caption
			
			kwargs = dict(
				chat_id = chat_id,
				text = text,
				parse_mode = parser,
				entities = entities,
				disable_web_page_preview = not embed,
				disable_notification = not notify,
				reply_to_message_id = reply_to_message_id,
				**kwargs,
			)

			while not self.client.is_connected: self.logger.info(f'Connecting...\r')
			return self.client.send_message(*args, **kwargs)

	class Discord(discord.Client):
		def __init__(self,
			token: str,
		*args, **kwargs):
			self.token = token
		
		def on(self,
		*args, **kwargs):
			return self.run(token = self.token, *args, **kwargs)
		
		def off(self,
		*args, **kwargs):
			return self.clear(*args, **kwargs)
		
		def user(self,
		*args, **kwargs) -> User:
			return User.Discord(
				self.user
			)

		def send(self,
			chat: discord.User or discord.Guild or discord.TextChannel or int,
			parser: str = 'html',
			entities: list = None,
			embed: discord.Embed or bool = True, notification: bool = True,
			reply_to: discord.Message = None,
		*args, **kwargs) -> Message:
			if type(chat) == int: chat = utils.true([
				self.get_user(chat), self.get_guild(chat), self.get_channel(chat)
			])[0]
			
			if type(embed) == discord.Embed: embed = embed
			if type(embed) == bool: embed = None

			kwargs = dict(
				embed = embed,
				**kwargs
			)

			return type(chat).send(*args, **kwargs)