import sys
from keywordtree import KeywordTree
from tools import timeit

data = open('science.txt').read().lower()

with timeit('construction'):
    for _ in range(int(sys.argv[1])):
        kwtree = KeywordTree()
        kwtree.add('science')
        kwtree.finalize()

with timeit('search'):
    for _ in range(int(sys.argv[2])):
        out = list(kwtree.search_all(data))

print(len(out))
