# chat
import main

my_testbot = main.Bot()
my_testbot.debug()

tg = my_testbot.Telegram(
	api_id = 2687706, api_hash = 'c7065e07465c29c70ad16de91c0d6084',
	token = '498618464:AAE6RRnZWfQXRZEGZ5MSFkWW3R7kxgfCYjM',
	client_name = 'Gianpiertolda'
)

tg.on()
tg.send(
	chat = -1001155864201, text = f'test'
)