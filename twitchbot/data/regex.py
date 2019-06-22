# :userman2!userman2@userman2.tmi.twitch.tv PRIVMSG #userman2 :test
# :hammerheadb0t!hammerheadb0t@hammerheadb0t.tmi.twitch.tv PRIVMSG #userman2 :test
import re

R_MESSAGE = re.compile(
    r':(?P<sender>[\w\d]+)!(?P=sender)+@(?P=sender)+\.tmi\.twitch\.tv PRIVMSG #(?P<channel>[\w\d]+) :(?P<msg>.+)\r')

R_MENTIONS = re.compile(r'@[^\s]+')
