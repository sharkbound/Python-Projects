import re
import sys

import pyperclip
import os

# 9/20	1hour 32mins	3:55 PM UTC	5:28 PM UTC	$38

while True:
    try:
        input('\npress enter to format clipboard... CTRL-C to exit...')
        data = re.search(r'(?P<date>\d+/\d+)\s*'
                         r'(?P<duration>\d+\s*hour[s]?\s*\d+\s*min[s]?)\s*'
                         r'(?P<start>\d+:\d+\s*(?:PM|AM|pm|am)\s*(?:UTC|utc))\s*'
                         r'(?P<end>\d+:\d+\s*(?:PM|AM|pm|am)\s*(?:UTC|utc))\s*'
                         r'(?P<charge>\$?\d+.?\d+)',
                         pyperclip.waitForPaste())

        if data is None:
            raise ValueError()
        date, duration, start, end, charge = data.groups()

        formatted = f'Python Tutoring\n\ndate: {date}/2021\nstart: {start}\nend: {end}\nduration: {duration}\n$ per hour: $25.00\n{charge}'
        pyperclip.copy(formatted)

        print(f'copied:\n\n{formatted}\n')
    except KeyboardInterrupt:
        sys.exit(0)
    except ValueError:
        print('\n\nimproperly formatted copy... copy the doc row then try again!\n\n')
        continue
