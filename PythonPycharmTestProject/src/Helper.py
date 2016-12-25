import os
import random

class Directory:
    def CreateOrDeleteDir(DirName: str):
        if not os.path.exists(DirName):
            os.mkdir(DirName)
            print('Created directory: %s\\%s' % (os.getcwd(), DirName))
        else:
            try:
                os.rmdir(DirName)
                print('Removed directory: %s\\%s' % (os.getcwd(), DirName))

            except:
                print('Error trying to remove directory:  %s\\%s' % (os.getcwd(), DirName))


class Logging:
    def log(msg: str):
        print(msg)


class InputFuncs:
    def GetUserNumberInput(defaultValue: float):
        try:
            userInput = float(input('Enter a number...\n'))
            return userInput

        except:
            Logging.log('Error trying to parse number!')
            return defaultValue

class RandomFuncs:
    def RandomIntStr(a: int, b):
        return str(random.randrange(a, b+1))

    def RandomInt(a: int, b):
        return random.randrange(a, b+1)

    def PrintRandNums(minNum: int, maxNum, amtOfNums):
        loopCount = 0;
        result = ''

        while loopCount < amtOfNums:
            if loopCount == 0:
                result += '{}'.format(RandomFuncs.RandomIntStr(minNum, maxNum))
            else:
                result += ', {}'.format(RandomFuncs.RandomIntStr(minNum, maxNum))
            loopCount += 1

        Logging.log(result)