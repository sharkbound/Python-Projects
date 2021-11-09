_running = True


def running(new_value=None):
    if new_value is not None:
        global _running
        _running = new_value
    return _running
