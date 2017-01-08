import time


class Timer:
    def __init__(self):
        self.start = time.time()
        self.end = time.time()
        self.const_start = time.time()

    def start_time(self):
        self.start = time.time()

    def reset_all(self):
        self.start = time.time()
        self.end = time.time()

    def reset_end(self):
        self.end = time.time()

    def reset_start(self):
        self.start = time.time()

    def print_reset(self):
        self.end = time.time()
        print(f'Execution time: {self.end-self.start}')
        self.reset_all()

    def print(self):
        self.end = time.time()
        result = self.end - self.start
        print(f'Execution time: {self.end-self.start}')

    def get_time(self):
        return self.end - self.start

    def time_exec(self, func, times=1):
        self.reset_all()
        for x in range(times):
            func()
        self.print_reset()
