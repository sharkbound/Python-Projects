from string import ascii_letters, ascii_lowercase

def decyper(s, ignore, _print = False):
    ret = ''
    for c in s:
        if c in ignore:
            if _print:
                print(c, end='')
            ret += c
            continue

        try:
            match_index = ascii_letters.index(c)
        except:
            pass
        else:
            char = ascii_letters[match_index + 2]
            if _print:
                print(char, end='')
            ret += char
    return ret


# puzzle source: http://www.pythonchallenge.com/pc/def/map.html
def start():
    encrypted = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
                 bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
                sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"""

    # websites way
    table = str.maketrans(ascii_lowercase, ascii_lowercase[2:] + ascii_lowercase[:2])
    print(str.translate(encrypted, table))

    # my way of doing it
    # print(decyper(encrypted, ".'() "))
    # print(decyper('map',''))


if __name__ == '__main__':
    start()
