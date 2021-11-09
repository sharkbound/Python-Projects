import pickle, urllib.request
from msvcrt import getch


def entry():
    # Had to look up solution for this one, had no clue how to use pickle module
    # after trying for ~1 hour
    handle = open('../files/banner.p', 'rb')
    data = pickle.load(handle)
    handle.close()

    for elt in data:
        print("".join([e[0] * e[1] for e in elt]))


if __name__ == '__main__':
    entry()
