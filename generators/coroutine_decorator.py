

def coroutine(func):
    # Automate the creation of the priming
    def preparation(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return preparation
