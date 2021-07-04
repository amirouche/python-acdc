import sys
from contextlib import contextmanager
from time import perf_counter as time


@contextmanager
def timeit(name):
    start = time()
    yield
    print(sys.argv[0], name, time() - start)
