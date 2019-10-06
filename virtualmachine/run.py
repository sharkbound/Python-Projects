from virtualmachine.vm import *

program = Program()
program.run([
    [Label('loop')],
    [Push(), "hello world!"],
    [Display()],
    [PushRand(), True, False],
    [JumpIfTrue('loop')]
])
