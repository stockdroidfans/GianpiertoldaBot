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
	*args, **kwargs) -> logging.Logger:
		self.logger.level = logging.DEBUG

	'''
	def motd(self,
		text: str = None,
	*args, **kwargs):
		self.motd = text

		if en_UK['defaults']['styling']['ascii_art'] is not None:
			ascii_art = en_UK['defaults']['styling']['ascii_art']
		else: ascii_art = art.text2art(self.name, font = 'small slant')

		random_style = f\'''{
			random.choice(en_UK["defaults"]["styling"]["random_color"])
		} {
			random.choice(en_UK["defaults"]["styling"]["random_blink"])
		}\'''
		
		random_text = random.choice(en_UK['defaults']['motd'])

		if not text: self.motd = en_UK['defaults']['startup_text'].format(
			ascii_art = ascii_art,
			random_style = random_style,
			random_text = random_text
		)

		separator_text = en_UK["defaults"]["styling"]["separator"]

		terminal_width = shutil.get_terminal_size((100, 25))[0]
		separators = round((terminal_width / len(en_UK['defaults']['styling']['separator'])))

		separator = []
		for sep in range(separators)[:-1]:
			if not len(separator):
				separator.append(f'[{random_style}]{separator_text}[/{random_style}]')
			if separator[sep - 1].endswith(en_UK["defaults"]["styling"]["separator"][-1]):
				separator.append(f'[{random_style}]{separator_text[1:-1]}[/{random_style}]')
			if sep == len(separator) - 1:
				separator.append(f'[{random_style}]{separator_text[1:]}[/{random_style}]')

		print(self.motd, end = '\n\n')
		print(*separator, sep = '', end = f'\n\n')
	'''

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
		
		def on(self,
		*args, **kwargs):
			return self.client.start(*args, **kwargs)
		
		def off(self,
		*args, **kwargs):
			return self.client.stop(*args, **kwargs)
		
		def get(self,
		*args, **kwargs) -> pyrogram.types.User:
			return self.client.get_me(*args, **kwargs)
		
		def send(self,
			chat: pyrogram.types.Chat or int,
			parser: str = 'html',
			entities: list = None,
			embed: bool = True, notification: bool = True,
			reply_to: pyrogram.types.Message or int = None, markup: str = '',
		*args, **kwargs) -> pyrogram.types.Message:
			chat_id: int
			if type(chat) == pyrogram.types.Chat: chat_id = chat.id
			if type(chat) == int: chat_id = chat
			else: chat_id = None

			reply_to_message_id: int
			if type(reply_to) == pyrogram.types.Message: reply_to_message_id = reply_to.message_id
			if type(reply_to) == int: reply_to_message_id = reply_to
			else: reply_to_message_id = None

			kwargs = dict(
				chat_id = chat_id,
				parse_mode = parser,
				entities = entities,
				disable_web_page_preview = not embed, disable_notification = not notification,
				reply_to_message_id = reply_to_message_id,
				**kwargs
			)

			while not self.client.is_connected: pass
			self.client.send_message(*args, **kwargs)

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
		
		def get_me(self,
		*args, **kwargs) -> discord.User:
			return self.user
		
		def send(self,
			chat: discord.User or discord.Guild or discord.TextChannel or int,
			parser: str = 'html',
			entities: list = None,
			embed: discord.Embed or bool = True, notification: bool = True,
			reply_to: discord.Message = None,
		*args, **kwargs) -> discord.Message:
			if type(chat) == int: utils.get_true([
				self.get_user(chat), self.get_guild(chat), self.get_channel(chat)
			])
			
			if type(embed) == discord.Embed: embed = embed
			if type(embed) == bool: embed = None

			kwargs = dict(
				embed = embed,
				**kwargs
			)

			return type(chat).send(*args, **kwargs)