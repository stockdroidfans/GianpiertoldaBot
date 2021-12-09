# chat
import main
import argparse

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

TEST_CHAT_ID= args.chat if args.chat else -1001155864201
TEST_MSG_TXT =args.text if args.text else f'<code>This is an automated test performed by GianpiertoldaBotTest</code>'

tg.on()
tg.send(chat = TEST_CHAT_ID, text = TEST_MSG_TXT)

while True:
	mycommand = main.Command(
		name = 'test', description = 'Test command.',
		config = main.CommandManifest(
			_list = [],
			prefix = ['/', '.', '!'], triggers = ['test2'],
			needs_match = False
		)
	)

	@tg.client.on_message()
	def test(client, message):
		print(mycommand)
		print(mycommand.detect(text = 'test'))
		if mycommand.detect(text = message.text):
			print('got here')
			tg.send(chat = TEST_CHAT_ID, text = 'test was initiated')