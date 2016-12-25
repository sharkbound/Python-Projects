from Helper import Directory as Dir
from Helper import Logging as logger
from Helper import InputFuncs
from Helper import RandomFuncs
from datetime import datetime

import os
import math
import random as r

now = datetime.now()
logger.log('%s/%s/%s' % (now.month, now.day, now.year))


'''
if os.getcwd().__contains__('a'):
    logger.log('%s' % ('true'))
else:
    logger.log('{}'.format('else'))
'''

#Dir.CreateOrDeleteDir('Tresh')

RandomFuncs.PrintRandNums(1, 100, 30)

num1 = InputFuncs.GetUserNumberInput(10)
num2 = InputFuncs.GetUserNumberInput(10)
product = str(num1 * num2)
logger.log(product)
