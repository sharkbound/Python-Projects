def encode(msg):
    return f'{msg}\r\n'.encode('utf-8')

def decode(byte_data: bytes, encoding='UTF8'):
    return byte_data.decode(encoding=encoding)