from collections import deque
from enum import Enum

from random import choice, shuffle

# noinspection PyArgumentList
(
    JUMP,
    DISPLAY,
    PUSH,
    POP,
    LABEL,
    JUMP_IF_TRUE,
    JUMP_IF_FALSE,
    PUSH_RANDOM,
    SHUFFLE,
    BRANCH_IF_TRUE,
    EXIT,
    PUSH_RANDOM_BOOL,
    SHOW,
    BRANCH_IF_FALSE,
    SHOW_STACK,
) = Enum('OPCODE',
         [
             'JUMP', 'DISPLAY', 'PUSH', 'POP', 'LABEL', 'JUMP_IF_TRUE', 'JUMP_IF_FALSE', 'PUSH_RANDOM',
             'SHUFFLE', 'BRANCH_IF_TRUE', 'EXIT', 'PUSH_RANDOM_BOOL', 'SHOW', 'BRANCH_IF_FALSE', 'SHOW_STACK'
         ])


def safe_get(items, index, default):
    return items[index] if 0 <= index < len(items) else default


def run(*codes):
    stack = deque()
    labels = {}

    def pop():
        return stack.pop()

    def push(value):
        stack.append(value)

    for i, (opcode, *args) in enumerate(codes):
        if opcode is LABEL:
            labels[args[0]] = i

    codes_length = len(codes)
    ptr = 0
    while 0 <= ptr < codes_length:
        code, *args = codes[ptr]
        if code is JUMP:
            ptr = labels[args[0]]
            continue
        elif code is PUSH:
            push(args[0])
        elif code is POP:
            pop()
        elif code is DISPLAY:
            print(pop(), end='\n' if safe_get(args, 0, True) else '')
        elif code is JUMP_IF_TRUE:
            if pop():
                ptr = labels[args[0]]
        elif code is JUMP_IF_FALSE:
            if not pop():
                ptr = labels[args[0]]
        elif code is PUSH_RANDOM:
            push(choice(args))
        elif code is SHUFFLE:
            shuffle(stack)
        elif code is BRANCH_IF_TRUE:
            ptr = labels[args[0] if pop() else args[1]]
        elif code is BRANCH_IF_FALSE:
            ptr = labels[args[0] if not pop() else args[1]]
        elif code is EXIT:
            quit(0)
        elif code is PUSH_RANDOM_BOOL:
            push(choice((True, False)))
        elif code is SHOW:
            print(' '.join(args))
        elif code is SHOW_STACK:
            if stack:
                print(list(stack))
        # print(stack)
        ptr += 1
