import sys
import acdc
from tools import timeit


data = open('science.txt').read().lower().encode('utf8')

with timeit('construction'):
    for _ in range(int(sys.argv[1])):
        machine = acdc.make(["science"])

with timeit('search'):
    for _ in range(int(sys.argv[2])):
        out = list(acdc.search(machine, data))

print(len(out))
