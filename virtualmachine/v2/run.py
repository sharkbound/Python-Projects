from virtualmachine.v2.vm import *

run(
    [LABEL, '1'],
    [SHOW, 'LABEL 1'],
    [PUSH_RANDOM_BOOL],
    [BRANCH_IF_TRUE, '1', '2'],
    [LABEL, '2'],
    [SHOW, 'LABEL 2'],
    [PUSH_RANDOM_BOOL],
    [BRANCH_IF_TRUE, '1', 'end'],
    [LABEL, 'end'],
    [EXIT]
)
