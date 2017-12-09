from data import R_MENTIONS


class Message:
    def __init__(self, sender: str, channel: str, content: str):
        self.sender = sender
        self.channel = channel
        self.content = content
        self.mentions = R_MENTIONS.findall(content)
