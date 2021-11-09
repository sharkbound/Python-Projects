import time


def decorator(f):
    defaults = getattr(f, '__defaults__', None)
    doc = getattr(f, '__doc__', '<NO DOC>')

    def _decorate(decorated):
        def _call(*args, **kwargs):
            return f(decorated, *args, **kwargs)

        return _call

    _decorate.__defaults__ = defaults
    _decorate.__doc__ = doc
    return _decorate


@decorator
def time_exec(f, or_max=100, *a, **kw):
    start = time.time_ns()
    f(*a, **kw)
    print(f.__name__, 'completed in', time.time_ns() - start, 'NS')


@time_exec
def test():
    print(1)


test()
