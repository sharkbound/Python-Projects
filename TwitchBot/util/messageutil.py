from data import R_MESSAGE, Message

def str_to_message(raw_str) -> Message:
    res, match = None, R_MESSAGE.match(raw_str)
    if match:
        res = Message(*(match['sender'], match['channel'], match['msg']))
    return res