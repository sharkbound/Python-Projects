import time


class Timer:
    def __init__(self):
        self.start = time.time()
        self.const_start = time.time()

    def reset(self):
        self.start = time.time()

    def print_reset(self):
        print(f'Execution time: {time.time()-self.start}')
        self.reset()

    def print(self):
        print(f'Execution time: {time.time()-self.start}')

    def get_time(self):
        return time.time() - self.start

    def get_total_time(self):
        return time.time() - self.const_start

    def time_exec(self, func, times=1):
        self.reset()
        for x in range(times):
            func()
        self.print_reset()
