from data import Message, command
from src.bot import Bot

bot = Bot()

@bot.on_message_received
def msg(msg: Message):
    print(f'{msg.sender}: {msg.content}')

@command()
def test(msg: Message, args):
    bot.send(f'cmd test command triggered by {msg.sender} with args: {args}')
    raise Exception("testing")

bot.run()