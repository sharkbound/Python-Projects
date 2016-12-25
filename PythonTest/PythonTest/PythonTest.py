import sys
import os
import Methods
from datetime import datetime

print(sys.version)

now = datetime.now()
currentYear = now.year
Methods.log2('log msg')
print("Current year:", currentYear, ' \nCurrent month:', now.month, '\nCurrent day:', now.day)
print('Time: ', str(now.hour) + ':' + str(now.minute))
print('{}/{}/{}'.format(now.month, now.day, now.year))

