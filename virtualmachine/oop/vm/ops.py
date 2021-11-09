from random import choice
from typing import Deque
from .result import Result, DEFAULT_RESULT

if False:
    from .program import Program


class OP:
    def __init__(self, pop_argc: int = 0, call_argc: int = 0):
        self.call_argc = call_argc
        self.pop_argc = pop_argc
        self.ptr = -1

    def pop_args_from_stack(self):
        return tuple(stack.pop() for _ in range(self.pop_argc))

    def execute(self, program: 'Program', args: Deque):
        return DEFAULT_RESULT


class Push(OP):
    def __init__(self):
        super().__init__(call_argc=1)

    def execute(self, program: 'Program', args: Deque):
        program.push(args[0])
        return DEFAULT_RESULT


class Jump(OP):
    def __init__(self, label_name: str):
        super().__init__()
        self.label_name = label_name

    def execute(self, program: 'Program', args: Deque):
        program.goto_label(self.label_name)
        return DEFAULT_RESULT


class JumpIfFalse(Jump):
    def execute(self, program: 'Program', args: Deque):
        if not program.pop():
            program.goto_label(self.label_name)
        return DEFAULT_RESULT


class JumpIfTrue(Jump):
    def execute(self, program: 'Program', args: Deque):
        if program.pop():
            program.goto_label(self.label_name)
        return DEFAULT_RESULT


class Display(OP):
    def __init__(self, newline=True):
        super().__init__(pop_argc=1)
        self.newline = newline

    def execute(self, program: 'Program', args: Deque):
        print(program.pop(), end='\n' if self.newline else '')
        return DEFAULT_RESULT


class Label(OP):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.ptr = -1


class Debug(OP):
    def execute(self, program: 'Program', args: Deque):
        print(program.stack)


class PushRand(OP):
    def execute(self, program: 'Program', args: Deque):
        program.push(choice(args))
        return DEFAULT_RESULT
