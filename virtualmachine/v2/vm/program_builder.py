from .program import *


class ProgramBuilder:
    def __init__(self):
        self.codes = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        run(self.codes)

    def append(self, *args):
        self.codes.append(args)

    def push(self, value):
        self.append(OP.PUSH, value)

    def show_stack(self):
        self.append(OP.SHOW_STACK)

    def display(self, newline=True):
        self.append(OP.DISPLAY, newline)

    def clear(self, variable_name):
        self.append(OP.CLEAR, variable_name)

    def jump_if_true(self, label):
        self.append(OP.JUMP_IF_TRUE, label)

    def jump_if_false(self, label):
        self.append(OP.JUMP_IF_FALSE, label)

    def branch_if_true(self, label_true, label_false):
        self.append(OP.BRANCH_IF_TRUE, label_true, label_false)

    def branch_if_false(self, label_false, label_true):
        self.append(OP.BRANCH_IF_FALSE, label_false, label_true)

    def push_random(self, *args):
        self.append(OP.PUSH_RANDOM, *args)

    def push_random_bool(self):
        self.append(OP.PUSH_RANDOM_BOOL)

    def jump(self, label):
        self.append(OP.JUMP, label)

    def pop(self):
        self.append(OP.POP)

    def label(self, label_name):
        self.append(OP.LABEL, label_name)

    def shuffle(self):
        self.append(OP.SHUFFLE)

    def exit(self):
        self.append(OP.EXIT)

    def print_join(self, *args):
        self.append(OP.PRINT_JOIN, *args)

    def print(self, value, newline=True):
        self.append(OP.PRINT, value, newline)

    def duplicate(self):
        self.append(OP.DUPLICATE)

    def load(self, variable_name):
        self.append(OP.LOAD, variable_name)

    def store(self, variable_name):
        self.append(OP.STORE, variable_name)
