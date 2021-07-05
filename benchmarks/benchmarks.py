import platform
import sys
from contextlib import contextmanager
from time import perf_counter_ns as time


PYTHON_NAME = "{}-v{}-{}:".format(
    platform.python_implementation(),
    platform.python_version(),
    platform.python_build()[0]
)
PROGRAM_NAME = sys.argv[0]
ITERATION_COUNT = int(sys.argv[1])
CONSTRUCTION_ITERATION_COUNT = int(sys.argv[2])
SEARCH_ITERATION_COUNT = int(sys.argv[3])


@contextmanager
def timeit(name, count):
    print('start', PROGRAM_NAME, name, count)
    start = time()
    yield
    average = (time() - start) / count
    print('end', PROGRAM_NAME, name, average, "average nanoseconds...")
    with open('{}.{}'.format(name, 'benchmarks.txt'), 'a') as f:
        f.write("{}/{}/{} {}\n".format(PYTHON_NAME, name, PROGRAM_NAME, average))

def science(init, make, search):
    data = init()

    with timeit('science', ITERATION_COUNT):
        with timeit('science-construction', CONSTRUCTION_ITERATION_COUNT):
            for _ in range(CONSTRUCTION_ITERATION_COUNT):
                x = make(('science',))

        with timeit('science-search', SEARCH_ITERATION_COUNT):
            for _ in range(SEARCH_ITERATION_COUNT):
                out = search(x, data['science'])

    print(len(out))


def loremipsum(init, make, search):
    data = init()

    with timeit('loremipsum', ITERATION_COUNT):
        with timeit('lorem-ipsum-construction', CONSTRUCTION_ITERATION_COUNT):
            for _ in range(CONSTRUCTION_ITERATION_COUNT):
                x = make(data['names'])

        with timeit('lorem-ipsum-search', SEARCH_ITERATION_COUNT):
            for _ in range(SEARCH_ITERATION_COUNT):
                out = search(x, data['loremipsum'])

    print(out)
