from functools import wraps, partial


def logger(func=None, log_args=True, log_name=True):
    if not func:
        return partial(logger, log_args=log_args, log_name=log_name)

    @wraps(func)
    def wrapper(*args, **kwargs):
        if log_name:
            print(func.__name__)

        if log_args:
            print(args, ', '.join(f'{key!r}={value!r}' for key, value in kwargs.items()))

        return func(*args, **kwargs)

    return wrapper


@logger(log_name=False)
def test(x=None):
    return x
