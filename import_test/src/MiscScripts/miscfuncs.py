import time

def getrange(start, stop=None, step=1, includezero=False):
    if stop == None:
        # if start == 1 and stop == None:
        #     start = 2

        result = []
        if includezero:
            if start > 1:
                result = range(start + 1)
            else:
                result = range(start)
                # result = range(start)
        else:
            if start > 1:
                result = range(1, start + 1)
            else:
                result = range(1, 2)
                # result = range(1, start+1)
        return result

    else:
        return range(start, stop + 1, step)


def sleep(sleepseconds):
    time.sleep(sleepseconds)