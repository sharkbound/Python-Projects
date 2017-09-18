def read_file_lines(fname):
    with open(fname, 'r') as read_file:
        yield from read_file

def write_to_file(fname, text=''):
    with open(fname, 'w') as write_file:
        write_file.write(text)
