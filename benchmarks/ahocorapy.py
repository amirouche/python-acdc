from keywordtree import KeywordTree
import benchmarks as b


def init():
    science = open('data/science.txt').read().lower()
    names = open('data/names.txt').read().lower().splitlines()
    loremipsum = open('data/loremipsum.txt').read().lower()
    return dict(science=science, names=names, loremipsum=loremipsum)


def make(keywords):
    kwtree = KeywordTree()
    for keyword in keywords:
        kwtree.add(keyword)
    kwtree.finalize()
    return kwtree


def search(kwtree, data):
    out = kwtree.search_all(data)
    out = list(out)
    return out


b.science(init, make, search)
b.loremipsum(init, make, search)
