from icecream import ic
from timeit import timeit
from add import add_py

from cdefs import add_c

print('add_py:', timeit('add_py(100, 1000)', globals=globals(), number=1_000_000))
print('add_c:', timeit('add_c(100, 1000)', globals=globals(), number=1_000_000))
