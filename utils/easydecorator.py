from functools import partial


class Call:
    __slots__ = 'func', 'args', 'kwargs'

    def __init__(self, func, args, kwargs):
        self.kwargs = kwargs
        self.args = args
        self.func = func

    def __len__(self):
        return len(self.args)

    def get(self, key, default=None):
        return self.kwargs.get(key, default)

    @property
    def arg_count(self):
        return len(self)

    @property
    def kwarg_count(self):
        return len(self.kwargs)

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.args[item]
        return self.kwargs[item]

    def __repr__(self):
        return f'<Call func={self.func} args={self.args} kwargs={self.kwargs}>'

    def __call__(self):
        return self.func(*self.args, **self.kwargs)


def decorator(wrapped_func):
    def deco_wrapper(func):
        def wrapped_call(*args, **kwargs):
            return wrapped_func(Call(func, args, kwargs))

        return wrapped_call

    return deco_wrapper


if __name__ == '__main__':
    @decorator
    def function(call: Call):
        print(call.get('a'))
        return call()


    @function
    def decorated(a, b):
        return a + b


    print(decorated(a=1, b=2))
