import re
import requests
import pygame


def start():
    regex = re.compile(r'\w\.\w+')
    match_str = "a quick brown русский fox jumped over a 970ft wall at 早上9點.sfasfsadasd."
    # match = re.findall(r'\w\.\w', match_str)
    match = regex.findall(match_str)
    print(*match, sep='')
    print()


if __name__ == '__main__':
    start()
