from virtualmachine.v2.vm import *

# run([
#     [OP.PUSH, 1],
#     [OP.STORE, 'number'],
#     [OP.SHOW_STACK],
#     [OP.LOAD, 'number'],
#     [OP.SHOW_STACK],
#     [OP.EXIT]
# ])

with ProgramBuilder() as p:
    p.exit()
