import discord
import asyncio
import sys
import os

from Util.config import BotConfig
from Bot.DiscordBot import Bot

# sys.path.append(".\\Bot")
# sys.path.append(".\\Util")


def main():
    cfg = BotConfig()
    bot = Bot()


if __name__ == '__main__':
    main()
