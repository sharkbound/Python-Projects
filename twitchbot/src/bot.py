import shlex

from cfg import cfg
from socket import socket
from util import encode, decode, str_to_message
from data import R_MESSAGE, Event, Message, commands


# :userman2!userman2@userman2.tmi.twitch.tv PRIVMSG #userman2 :test
# :hammerheadb0t!hammerheadb0t@hammerheadb0t.tmi.twitch.tv PRIVMSG #userman2 :test


class Bot:
    def __init__(self, command_prefix='!'):
        self.socket = socket()
        self.connected = False
        self.command_prefix = command_prefix

        self.on_message_received = Event()
        self.on_message_sent = Event()

        self.on_whisper_received = Event()
        self.on_whisper_sent = Event()

        self.on_command_executed = Event()
        self.on_command_triggered = Event()

    def disconnect(self):
        self.socket.close()
        self.connected = False

    def run(self):
        if not self.connected:
            self._connect()

        while True:
            try:
                msg = self._get_next_socket_msg()
                self._process_message(msg)
            except Exception as e:
                print(f'exception occured in run():\n\t{e}')
                continue

    def send(self, content):
        self.send_raw(f'PRIVMSG #{cfg["channel"]} :{content}')

    def send_raw(self, content):
        self.socket.send(encode(content))

    def _process_message(self, raw_str):
        msg = str_to_message(raw_str)
        if msg is not None:
            if not self._process_command(msg):
                self.on_message_received.trigger(msg)

    def _process_command(self, msg: Message):
        if msg.content.startswith(self.command_prefix):
            parts = shlex.split(msg.content)
            parts[0] = parts[0][1:]
            cmd = ([c for c in commands if c.name == parts[0]] or (None,))[0]

            if cmd:
                try:
                    cmd(msg, parts[1:])
                except Exception as e:
                    print(f'error executing command {cmd.name}:\n\t{e}')
                return True
        return False

    def _connect(self, log_errors=True):
        try:
            self.socket.connect(('irc.chat.twitch.tv', 6667))
            self._login()
            self.connected = True
        except Exception as e:
            if log_errors:
                print(f'error occured when trying to connect to chat: \n\t{e}')

    def _login(self):
        self.socket.send(encode(f'PASS {cfg["oauth"]}'))
        self.socket.send(encode(f'NICK {cfg["username"]}'))
        self.socket.send(encode(f'JOIN #{cfg["channel"]}'))

    def _get_next_socket_msg(self):
        return decode(self.socket.recv(1024))
