from collections import deque
from typing import Deque, Dict, List, Any
from .result import Result

if False:
    from .ops import Label


class Program:
    def __init__(self):
        from .ops import OP

        self.ptr = 0
        self.codes: Deque[List[OP, Any, ...]] = deque()
        self.stack = deque()
        self.label_pointers: Dict[str, 'Label'] = dict()

    def get_label(self, label_name: str) -> 'Label':
        return self.label_pointers[label_name]

    def goto_label(self, label_name: str):
        self.ptr = self.get_label(label_name).ptr

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def pop_many(self, count: int):
        return tuple(self.stack.pop() for _ in range(count))

    def setup(self):
        from .ops import Label
        for i, (op, *_) in enumerate(self.codes):
            if isinstance(op, Label):
                self.label_pointers[op.name] = op
            op.ptr = i

    def run(self, codes):
        self.codes = codes
        self.setup()

        while 0 <= self.ptr < len(self.codes):
            code = self.codes[self.ptr]
            op, args = code[0], deque(code[1:])
            result = op.execute(self, args)

            if result is Result.INCREMENT_PTR:
                self.ptr += 1
