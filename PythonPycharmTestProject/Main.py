from Helper import Directory as Dir
from Helper import Logging as logger
from Helper import InputFuncs
from Helper import RandomFuncs
from Helper import FileFuncs
from datetime import datetime

import os
import sys
import math
'''
if os.getcwd().__contains__('a'):
    logger.log('%s' % ('true'))
else:
    logger.log('{}'.format('else'))
'''


now = datetime.now()
logger.log('%s/%s/%s' % (now.month, now.day, now.year))

#Dir.CreateOrDeleteDir('Tresh')
#FileFuncs.CreateFile('1337', 'py')

RandomFuncs.PrintRandNums(1, 100, 30)

num1 = InputFuncs.GetUserNumberInput(10)
num2 = InputFuncs.GetUserNumberInput(10)
product = float(num1 * num2)

SquareRoot = 'Sqrt of {} is {}.'.format(product, math.sqrt(product))
logger.log(SquareRoot)
