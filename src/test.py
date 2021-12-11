# chat
import main
import argparse
import logging
from pyrogram import filters

# Instantiate the parser
parser = argparse.ArgumentParser(
	description = 'GianpiertoldaBot Test'
)

parser.add_argument('--chat', type = int, help = 'Test chat ID')
parser.add_argument('--text', type = str, help = 'Test message text')
parser.add_argument('--video', type = str, help = 'Test message video')
parser.add_argument('--caption', type = str, help = 'Test video caption')

args = parser.parse_args()

my_testbot = main.Bot()
my_testbot.debug()

tg = my_testbot.Telegram(
	api_id = 2687706, api_hash = 'c7065e07465c29c70ad16de91c0d6084',
	token = '498618464:AAE6RRnZWfQXRZEGZ5MSFkWW3R7kxgfCYjM',
	client_name = 'Gianpiertolda'
)

logger = my_testbot.logger

TEST_CHAT_ID = args.chat if args.chat else -1001155864201
TEST_MSG_TXT = args.text if args.text else f'<code>This is an automated test performed by GianpiertoldaBotTest</code>'

# tg.send(chat = TEST_CHAT_ID, text = TEST_MSG_TXT)

mycommand = main.Command(
	name = 'test', description = 'Test command.',
	config = main.CommandManifest(
		_list = [],
		prefix = ['/', '.', '!'], triggers = ['test2'],
		needs_match = False
	)
)

@tg.client.on_message(filters.command("test"))
def test(client, message):
	logger.debug('got here: tg.client.on_message(test)')
	print(mycommand)
	print(mycommand.detect(text = 'test'))
	if mycommand.detect(text = message.text):
		logger.debug('got here: mycommand.detect(text = message.text)')
		print('command detected')
		tg.send(chat = TEST_CHAT_ID, text = 'test was initiated')

tg.on()