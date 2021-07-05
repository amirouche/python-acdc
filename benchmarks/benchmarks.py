import sys
from contextlib import contextmanager
from time import perf_counter_ns as time


PROGRAM_NAME = sys.argv[0]
ITERATION_COUNT = int(sys.argv[1])
CONSTRUCTION_ITERATION_COUNT = int(sys.argv[2])
SEARCH_ITERATION_COUNT = int(sys.argv[3])


@contextmanager
def timeit(name, count):
    print('start', PROGRAM_NAME, name, count)
    start = time()
    yield
    print('end', PROGRAM_NAME, name, (time() - start) / count, "average nanoseconds...")


def science(init, make, search):
    data = init()

    with timeit('science', ITERATION_COUNT):
        with timeit('construction', CONSTRUCTION_ITERATION_COUNT):
            for _ in range(CONSTRUCTION_ITERATION_COUNT):
                x = make(('science',))

        with timeit('search', SEARCH_ITERATION_COUNT):
            for _ in range(SEARCH_ITERATION_COUNT):
                out = search(x, data['science'])

    print(len(out))


def loremipsum(init, make, search):
    data = init()

    with timeit('loremipsum', ITERATION_COUNT):
        with timeit('construction', CONSTRUCTION_ITERATION_COUNT):
            for _ in range(CONSTRUCTION_ITERATION_COUNT):
                x = make(data['names'])

        with timeit('search', SEARCH_ITERATION_COUNT):
            for _ in range(SEARCH_ITERATION_COUNT):
                out = search(x, data['loremipsum'])

    print(out)
