from collections import deque
from enum import Enum, auto

from random import choice, shuffle


# noinspection PyArgumentList
class OP(Enum):
    JUMP = auto()
    DISPLAY = auto()
    PUSH = auto()
    POP = auto()
    LABEL = auto()
    JUMP_IF_TRUE = auto()
    JUMP_IF_FALSE = auto()
    PUSH_RANDOM = auto()
    SHUFFLE = auto()
    BRANCH_IF_TRUE = auto()
    EXIT = auto()
    PUSH_RANDOM_BOOL = auto()
    PRINT_JOIN = auto()
    BRANCH_IF_FALSE = auto()
    SHOW_STACK = auto()
    STORE = auto()
    LOAD = auto()
    DUPLICATE = auto()
    PRINT = auto()
    CLEAR = auto()


def safe_get(items, index, default):
    return items[index] if 0 <= index < len(items) else default


def run(codes):
    stack = deque()
    labels = {}
    variables = {}

    def pop():
        return stack.pop()

    def push(value):
        stack.append(value)

    for i, (opcode, *args) in enumerate(codes):
        if opcode is OP.LABEL:
            labels[args[0]] = i

    codes_length = len(codes)
    ptr = 0
    while 0 <= ptr < codes_length:
        code, *args = codes[ptr]
        if code is OP.JUMP:
            ptr = labels[args[0]]
            continue
        elif code is OP.PUSH:
            push(args[0])
        elif code is OP.POP:
            pop()
        elif code is OP.DISPLAY:
            print(pop(), end='\n' if safe_get(args, 0, True) else '')
        elif code is OP.JUMP_IF_TRUE:
            if pop():
                ptr = labels[args[0]]
        elif code is OP.JUMP_IF_FALSE:
            if not pop():
                ptr = labels[args[0]]
        elif code is OP.PUSH_RANDOM:
            push(choice(args))
        elif code is OP.SHUFFLE:
            shuffle(stack)
        elif code is OP.BRANCH_IF_TRUE:
            ptr = labels[args[0] if pop() else args[1]]
        elif code is OP.BRANCH_IF_FALSE:
            ptr = labels[args[0] if not pop() else args[1]]
        elif code is OP.EXIT:
            quit(0)
        elif code is OP.PUSH_RANDOM_BOOL:
            push(choice((True, False)))
        elif code is OP.PRINT_JOIN:
            print(' '.join(args))
        elif code is OP.SHOW_STACK:
            print(list(stack))
        elif code is OP.STORE:
            variables[args[0]] = pop()
        elif code is OP.LOAD:
            push(variables[args[0]])
        elif code is OP.DUPLICATE:
            value = pop()
            push(value)
            push(value)
        elif code is OP.PRINT:
            print(args[0], end='\n' if safe_get(args, 1, True) else '')
        elif code is OP.CLEAR:
            del variables[args[0]]
        ptr += 1
