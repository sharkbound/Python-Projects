import sys
import os
import logger


class DirectoryCrawler(object):
    def __init__(self):
        self.highest_chain = 0
        self.last_log = ''

    def printDir(self, path, iteration, arrowLength):
        if iteration > self.highest_chain: self.highest_chain = iteration
        # if not os.path.exists(path): return
        for dir in next(os.walk(path))[1]:
            self.last_log = f'{"-"*arrowLength}> {dir} : {iteration}'
            print(self.last_log)
            logger.logtofile(self.last_log, file='directoryOutput.txt')
            self.printDir(f'{path}\\{dir}', iteration + 1, arrowLength + 1)


if __name__ == "__main__":
    crawler = DirectoryCrawler()
    crawler.printDir(os.curdir, 0, 0)
    print(f'Highest chain for this run was: {crawler.highest_chain}')
