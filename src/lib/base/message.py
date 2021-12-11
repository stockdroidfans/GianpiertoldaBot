# GianpiertoldaBot
# © 2021 Stockdroid Fans

'''
	# [GianpiertoldaBot](https://github.com/stockdroidfans/Gianpiertolda)

	© 2019–2021 [Stockdroid Fans](https://github.com/stockdroidfans)
	Licensed under the MIT [MIT License](https://github.com/stockdroidfans/Gianpiertolda/blob/main/LICENSE)

	---

	Host for `gianpiertolda.Message`

	```
	from gianpiertolda import Message
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

class Message:
	class Telegram(pyrogram.types.Message):
		def __init__(self,
		*args, **kwargs):
			self.id = self.message_id
			self.content = self.get_content()
			if len(self.content) is 1: self.content = self.content[0]
		
		def get_content(self,
		*args, **kwargs):
			valid_content = [
				self.text, self.photo, self.video, self.animation, self.voice,
				self.audio, self.video_note, self.document, self.game, self.dice,
				self.contact, self.location, self.venue, self.invoice, self.chat_action
			] # TODO: there's actually quite a lot more of these!
			self.content = utils.true(valid_content)
			return self.content
	
	class Discord(discord.Message):
		def __init__(self, *args, **kwargs):
			self.id = self.id
			self.content = self.content

		def get_content(self,
		*args, **kwargs):
			return self.content