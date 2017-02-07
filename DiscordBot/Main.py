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
    @asyncio.coroutine
    def on_read():
        print('client logged in...')


    @bot.command()
    async def help1(*args):
        return await bot.say('Default help text')

    @bot.command()
    async def quit(*args):
        await bot.say("**__Swims deep into the ocean...__**")
        return await bot.logout()

    bot.run(cfg.token)

if __name__ == '__main__':
    main()
