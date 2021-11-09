import discord
import asyncio
import sys
import os

from Util.config import BotConfig
from discord.ext.commands import Bot

sys.path.append(".\\Bot")
sys.path.append(".\\Util")


def main():
    cfg = BotConfig()
    bot = Bot(command_prefix=cfg.command_prefix)

    @bot.event
    async def on_ready():
        print('client logged in...')
        print(f'Set command prefix to : {cfg.command_prefix}')

    @bot.command()
    async def help1(*args):
        return await bot.say('Default help text')

    @bot.command()
    async def quit(*args):
        await bot.say("**__Swims deep into the ocean...__**")
        return await bot.logout()

    @bot.command()
    async def dm_me(*args):
        await bot.say('Sending dm...')
        # bot.send_message()

    @bot.event
    async def on_message(msg: discord.Message):
        if (msg.author == Bot.get_user_info): return;
        print(msg.content)
        print(msg.author)
        # await bot.say(msg.channel, f'Received message from: \nChannel: {msg.channel} \nText: {msg.content}')

    bot.run(cfg.token)


if __name__ == '__main__':
    main()
