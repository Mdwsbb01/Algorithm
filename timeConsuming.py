#decorator
import time

def timeConsuming(func):
    def wrapper(*args, **kw):
        t1 = time.time()
        result = func(*args, **kw)
        t2 = time.time()
        print('{} running time {:e} secs'.format(func.__name__, (t2 - t1)))
        return result
    return wrapper
